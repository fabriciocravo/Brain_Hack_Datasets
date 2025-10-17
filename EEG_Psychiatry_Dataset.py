import pandas as pd

# Dataset from - https://www.kaggle.com/datasets/shashwatwork/eeg-psychiatric-disorders-dataset?resource=download

# EEG dataset with ~1,150 features per subject extracted from 19-electrode 10-20 system
# Features include:
# - Demographics: sex, age, education, IQ, disorder info
# - AB (Absolute power): Mean power in 6 frequency bands (delta, theta, alpha, beta, highbeta, gamma)
#   across 19 electrodes = 114 features
# - COH (Coherence): Mean pairwise coherence between all electrode pairs for each band
#   = 171 pairs × 6 bands = 1,026 features
# Each row = 1 subject with summary statistics (no time series), classic p >> n problem

df = pd.read_csv('./data/EEG.machinelearing_data_BRMH.csv')

for feature in df.columns:
    print(feature)

# It has 1149 features .....
# All summary from collections not time series data
print(len(df.columns))

# 945 subjects - I don't know if they are unique or not
print(df['no.'])

# main.disorder and specific.disorder




