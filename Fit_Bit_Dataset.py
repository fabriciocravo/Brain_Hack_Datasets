import pandas as pd

# LifeSnaps Fitbit Dataset - Two related dataframes:

# 1. Daily sensor data (7,410 rows × 63 cols): Time-series of Fitbit metrics per user
#    - Sleep: duration, efficiency, stages (deep/light/REM/wake), SpO2, breathing rate
#    - Activity: steps, calories, distance, active minutes (light/moderate/vigorous)
#    - Physiological: heart rate (resting/active), HRV (RMSSD), temperature, stress score
#    - Context labels: mood states (HAPPY, SAD, TENSE, TIRED, etc.) and locations
#      (HOME, GYM, WORK/SCHOOL, OUTDOORS, etc.)
#    - Demographics: age, gender, BMI, fitness goals

# 2. BREQ questionnaire (92 rows × 10 cols): Exercise motivation assessments per user
#    - Behavioral Regulation in Exercise Questionnaire scores across motivation spectrum:
#      amotivation → external → introjected → identified → intrinsic regulation
#    - Multiple submissions per user (longitudinal survey data)

# Structure: Multiple daily records per user_id (first df) + periodic surveys (second df)
# Useful for: Physical activity behavior modeling, sleep-mood-activity relationships,
#             motivation dynamics, personalized health interventions

df = pd.read_csv('./data/rais_anonymized/csv_rais_anonymized/daily_fitbit_sema_df_unprocessed.csv')

print(df)

for feature in df.columns:
    print(feature)

# (7410, 63) - a good amount of data!
print(df.shape)

# Questionare dataset
df = pd.read_csv('./data/rais_anonymized/scored_surveys/breq.csv')
print(df)

# Features are different
for feature in df.columns:
    print(feature)

# You're supposed to match id to questionnaire answer
print(df.shape)
print(df['user_id'])

# Too much for the Hackaton, we need to cut this a little
