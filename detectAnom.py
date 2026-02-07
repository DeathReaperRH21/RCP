import pandas as pd

# Read your Excel file (sheet might need to be specified)
df = pd.read_excel('twoDataSets.xlsx')

# Drop rows where 'event' is missing
df_events = df[df['event'].notnull()]

# Convert to numbers and fill missing with 0 for math
df_events['depth [%]'] = pd.to_numeric(df_events['depth [%]'], errors='coerce').fillna(0)
df_events['ID Reduction [%]'] = pd.to_numeric(df_events['ID Reduction [%]'], errors='coerce').fillna(0)
df_events['width [in]'] = pd.to_numeric(df_events['width [in]'], errors='coerce').fillna(0)
df_events['length [in]'] = pd.to_numeric(df_events['length [in]'], errors='coerce').fillna(0)

# Flag CLUSTER anomalies
clusters = df_events[
    (df_events['event'].str.lower() == 'cluster') &
    (
        (df_events['ID Reduction [%]'] > 10) |
        (df_events['width [in]'] > 5) |
        (df_events['length [in]'] > 5)
    )
]

# Flag METAL LOSS anomalies
metalloss = df_events[
    (df_events['event'].str.lower() == 'metal loss') &
    (df_events['depth [%]'] > 20)
]

# Combine for review
anomalies = pd.concat([clusters, metalloss])

print(anomalies[['log dist. [ft]', 'event', 'depth [%]', 'ID Reduction [%]', 'length [in]', 'width [in]', 'comment']])

def is_anomaly(row):
    if row['event'] is None:
        return False
    event = str(row['event']).lower()
    if event == 'cluster':
        if row['ID Reduction [%]'] > 10 or row['width [in]'] > 5 or row['length [in]'] > 5:
            return True
    elif event == 'metal loss':
        if row['depth [%]'] > 20:
            return True
    return False

df_events['anomaly'] = df_events.apply(is_anomaly, axis=1)
print(df_events[df_events['anomaly']])

df_events[df_events['anomaly']].to_excel('anomalies.xlsx', index=False)