import pandas as pd


# EMA (Ecological Momentary Assessment) dataset - repeated daily surveys
# 4,372 responses from 79 users over ~2 weeks (March 16-29, 2020)
#
# Structure:
# - 4 scheduled assessments per day (beepvar 1-4): 12pm, 3pm, 6pm, 9pm
# - 18 EMA questions (Q1-Q18): likely mood, stress, context, behavior items
# - Timestamps: Scheduled (target time), Issued (sent), Response (completed)
# - Duration: time to complete survey
# - 7,886 total NaNs (~14% missing data) - common in EMA due to non-response
#
# Typical EMA use case: Capturing momentary states/behaviors in natural settings,
# studying within-person variability, temporal dynamics of psychological processes

df = pd.read_csv('./data/clean_ema.csv')

print(df)

# The questions are labeled as Q1, Q2, ....., etc
for feature in df.columns:
    print(feature)

# (4372, 26)
print(df.shape)

# Number of users - It has 79 different users
print(len(df['ID'].unique()))

# Total number of NaNs - 7886 in entire dataset
print(df.isna().sum().sum())