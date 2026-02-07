import pandas as pd

# Load your two datasets
df1 = pd.read_excel('dataset1.xlsx')
df2 = pd.read_excel('dataset2.xlsx')

# Make column names consistent/lowercase for easier reference
df1.columns = df1.columns.str.lower()
df2.columns = df2.columns.str.lower()

df1_welds = df1[df1['event'].str.lower().str.contains('girthweld', na=False) | df1['event'].str.lower().str.contains('girth weld', na=False) | df1['event description'].str.lower().str.contains('girthweld', na=False) | df1['event description'].str.lower().str.contains('girth weld', na=False)]

df2_welds = df2[df2['event'].str.lower().str.contains('girthweld', na=False) | df2['event'].str.lower().str.contains('girth weld', na=False) | df2['event description'].str.lower().str.contains('girthweld', na=False) | df2['event description'].str.lower().str.contains('girth weld', na=False)]