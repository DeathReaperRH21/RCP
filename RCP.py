import pandas as pd
import numpy as np

# Load data
df = pd.read_excel("ILIDataV2.xlsx", sheet_name=0)

# Step 1: Handle missing values (example: fill with NaN for consistency)
df = df.replace({'': np.nan, 'N/A': np.nan})

# Step 2: Normalize feature names for consistency
def clean_feature_type(val):
    if pd.isnull(val): return val
    val = val.strip().lower().replace('-', ' ').replace('_', ' ')
    # Example mappings, extend as needed
    if 'girth weld' in val:
        return 'girth weld'
    if 'field bend' in val or 'bend' in val:
        return 'field bend'
    if 'metal loss' in val:
        if 'manufacturing' in val:
            return 'metal loss manufacturing anomaly'
        else:
            return 'metal loss'
    if 'seam weld' in val:
        return 'seam weld manufacturing anomaly'
    if 'cluster' in val:
        return 'cluster'
    return val
df['feature_type'] = df['feature_type'].apply(clean_feature_type)

# Step 3: Standardize clock position (handle decimal vs time strings)
def normalize_clock(clock_val):
    # Accepts float, or string in 'H:MM' format
    if pd.isnull(clock_val):
        return np.nan
    if isinstance(clock_val, float) or isinstance(clock_val, int):
        return float(clock_val)
    if ':' in str(clock_val):
        parts = str(clock_val).split(':')
        h = float(parts[0])
        m = float(parts[1]) / 60
        return h + m
    try:
        return float(clock_val)
    except:
        return np.nan
df['clock_pos_norm'] = df['clock_pos'].apply(normalize_clock)

# Step 4: Flag anomalies by type and comment keywords
anomaly_terms = ['metal loss', 'cluster', 'manufacturing anomaly', 'seam weld']
def is_anomaly(row):
    if pd.isnull(row['feature_type']):
        return False
    for term in anomaly_terms:
        if term in row['feature_type']:
            return True
    return False
df['is_anomaly'] = df.apply(is_anomaly, axis=1)

# Step 5: Detect outliers in measurements (e.g., for 'depth')
for col in ['depth', 'length', 'width']:
    if col in df.columns:
        col_mean = df[col].mean()
        col_std = df[col].std()
        df[f'{col}_outlier'] = (df[col] - col_mean).abs() > 2 * col_std

# Step 6: (Optional) Standardize units if needed
# For example, if you find inches ("in") and mm ("mm"), convert as desired

# Step 7: Filter results
anomalies = df[df['is_anomaly'] | df.filter(like='_outlier').any(axis=1)]
print(anomalies)

# Save anomalies for review
anomalies.to_csv("ILI_detected_anomalies.csv", index=False)