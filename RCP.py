import pandas as pd
import numpy as np

# Load your spreadsheet (adjust sheet_name if necessary)
df_2022 = pd.read_excel('ILIDataV2.xlsx', sheet_name='2022')
df_2015 = pd.read_excel('ILIDataV2.xlsx', sheet_name='2015')

# Standardize the feature type column
df_2022.rename(columns={'Event Description': 'feature_type'}, inplace=True)
df_2015.rename(columns={'Event Description': 'feature_type'}, inplace=True)

# --- Extract Girth Welds from Each Sheet ---

#print(df_2015.columns.tolist())

# For 2022: use the odometer field 'ILI Wheel Count  [ft.]'
girth_welds_2022 = df_2022[df_2022['feature_type'].str.contains('Girth', case=False, na=False)]
positions_2022 = girth_welds_2022['ILI Wheel Count \n[ft.]'].astype(float).tolist()

# For 2015: use absolute position 'log dist'
girth_welds_2015 = df_2015[df_2015['feature_type'].str.contains('Girth', case=False, na=False)]
positions_2015 = girth_welds_2015['Log Dist. [ft]'].astype(float).tolist()

# --- Alignment Function ---

def align_welds(reference_positions, target_positions, tolerance=2.0):
    """Align positions from target to reference if they are within a set tolerance"""
    mapping = []
    for tgt_pos in target_positions:
        diffs = np.abs(np.array(reference_positions) - tgt_pos)
        min_diff = np.min(diffs)
        if min_diff <= tolerance:
            match_pos = reference_positions[np.argmin(diffs)]
            mapping.append((tgt_pos, match_pos))
    return mapping

# Align the 2022 welds to 2015 welds (change tolerance as needed)
aligned_welds = align_welds(positions_2015, positions_2022, tolerance=2.0)

# Print the result
for us_pos, log_pos in aligned_welds:
    print(f"2022 Weld at {us_pos:.2f} ft aligned to 2015 Weld at {log_pos:.2f} ft")

aligned_welds_df = pd.DataFrame(aligned_welds, columns=['2022 Position', '2015 Position'])
aligned_welds_df.to_csv('GirthWelds.csv', index=False)

# You can use these mapping points to align/analyze anomalies or features across the datasets.