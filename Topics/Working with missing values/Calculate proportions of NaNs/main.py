#  write your code here
import pandas as pd

merged_df = pd.read_csv('data/dataset/input.txt')
missing_proportions = merged_df.isna().mean().round(2)
print(missing_proportions)

