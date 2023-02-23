#  write your code here
import pandas as pd

merged_df = pd.read_csv('data/dataset/input.txt')
print(len(merged_df), len(merged_df.dropna()))
