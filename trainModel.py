# Data wrangling libraries
import pandas as pd
import numpy as np
import cudf # GPU version of pandas
from numba import cuda
import os

# ML Libraries
from cuml import KMeans # GPU version of scikit-learn

# Plotting libraries
import multiprocessing as mp

# wrapper functions
from resultHelperClass import Result
from open_source_algo.cvxEDA import wrapperCVXEDA


def extract_onset_offset(phasic: list):
    pass


if __name__ == "__main__":
    os.system("nvcc --version")

