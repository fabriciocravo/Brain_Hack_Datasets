import pandas as pd

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

# Too much for the hackaton, we need to cut this a little