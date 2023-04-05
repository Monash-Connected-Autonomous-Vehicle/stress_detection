# Shimmer3 GSR+ Stress Detection
Using the Shimmer3 GSR+ to extract skin conductance data and use that to detect stress after certain stimulus.

## Packages requirement
- Required conda as a package management tool
- Required python libraries is in the 'requirements.txt' or you can ```pip install git+https://github.com/Monash-Connected-Autonomous-Vehicle/stress_detection.git```
- Required CUDA (Needs NVIDIA GPU) [installation](https://docs.rapids.ai/install?_gl=1*19w40ax*_ga*MjExNzQ0NTAyOS4xNjgwNjU2MTQ4*_ga_RKXFW6CM42*MTY4MDcxOTk2OS4zLjAuMTY4MDcxOTk2OS4wLjAuMA)```conda create -n rapids-23.02 -c rapidsai -c conda-forge -c nvidia rapids=23.02 python=3.10 cudatoolkit=11.8```

### Project Tree
```
stress_detection/
├── data_viz.ipynb
├── LICENSE
├── live_data_viz.ipynb
├── README.md
├── requirements.txt
├── resultHelperClass.py
├── train_model.ipynb
├── trainModel.py
├── open_source_algo
│   ├── cvxEDA.py
│   └── LICENSE.txt
└── resources
    ├── csv
    │   ├── default_exp_Session1_Shimmer_92E8_Calibrated_PC.csv
    │   ├── default_exp_Session1_Shimmer_92E8_Calibrated_PC_Session2.csv
    │   ├── default_exp_Session1_Shimmer_92E8_Calibrated_SD.csv
    │   ├── driving_session.csv
    │   └── train
    │       ├── EDA_10.csv
    │       ├── EDA_11.csv
    │       ├── EDA_13.csv
    │       ├── EDA_14.csv
    │       ├── EDA_15.csv
    │       ├── EDA_16.csv
    │       ├── EDA_17.csv
    │       ├── EDA_2.csv
    │       ├── EDA_3.csv
    │       ├── EDA_4.csv
    │       ├── EDA_5.csv
    │       ├── EDA_6.csv
    │       ├── EDA_7.csv
    │       ├── EDA_8.csv
    │       └── EDA_9.csv
    └── db
        └── 1679375961.db

7 directories, 34 files
```
