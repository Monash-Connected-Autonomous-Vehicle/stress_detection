# Data wrangling libraries
import cudf  # GPU version of pandas
import cupy
import numpy
from numba import cuda

# console stuff
import contextlib
import sys

# ML Libraries
from cuml import KMeans  # GPU version of scikit-learn

# Plotting libraries
import multiprocessing as mp

# wrapper functions
from resultHelperClass import Result
from open_source_algo.cvxEDA import wrapperCVXEDA


class OutFile(object):
    def write(self, x):
        pass


@contextlib.contextmanager
def no_std_out():
    temp_stdout = sys.stdout
    sys.stdout = OutFile()
    yield
    sys.stdout = temp_stdout


def extract_onset_offset(ph: cupy.ndarray, threshold: float = 0.1):
    onset_offset = cupy.zeros(len(ph), dtype=bool)
    onset = False

    for i, elem in enumerate(ph):
        if onset:
            if elem > threshold:
                onset_offset[i] = True
            else:
                onset = False
        else:
            if elem > threshold:
                onset = True

    return onset_offset


def extract_phasic(gsr: numpy.ndarray, sample_rate: int):
    with no_std_out():
        extracted = wrapperCVXEDA(gsr, 1/sample_rate)
    return extracted


if __name__ == "__main__":
    # reading data
    file_dir = "resources/csv/default_exp_Session1_Shimmer_92E8_Calibrated_PC_Session2.csv"
    delim = "\t"
    Fs = 150
    gsr_data: cudf.DataFrame = cudf.read_csv(file_dir, delimiter=delim, header=1)

    # cleaning specific data
    gsr_data.drop(columns=gsr_data.columns[-1], axis=1, inplace=True)
    gsr_data.drop(index=0, axis=0, inplace=True)
    gsr_data.reset_index(drop=True, inplace=True)
    gsr_data = gsr_data.astype("float64")

    # normalizing timestamp
    first_time = gsr_data.loc[0, gsr_data.columns[0]]


    def normalized_timestamp(element):
        return element - first_time


    gsr_data[gsr_data.columns[0]] = gsr_data[gsr_data.columns[0]].apply(normalized_timestamp)

    # calculate onset_offset
    cuda_series: cudf.Series = cudf.Series()
    index = 0
    for s_index in range(0, len(gsr_data), 100000):
        cuda_series = cudf.concat([cuda_series,
                                   cudf.Series(
                                       extract_phasic(
                                           gsr_data.loc[index:index+100000-1, gsr_data.columns[1]].to_numpy(), Fs)[0])],
                                  ignore_index=True)
        index = s_index
    if index < len(gsr_data):
        cuda_series = cudf.concat([cuda_series,
                                   cudf.Series(extract_phasic(
                                       gsr_data.loc[index:len(gsr_data)-1, gsr_data.columns[1]].to_numpy(), Fs)[0])],
                                  ignore_index=True)
    gsr_data["PhasicComponent"] = cuda_series

    # create offset and onset data
    gsr_data["OnsetOffset"] = extract_onset_offset(gsr_data["PhasicComponent"].to_cupy())

    # plotting and putting it into image
    pass
