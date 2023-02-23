#  write your code here
import pandas as pd

merged_df = pd.read_csv('data/dataset/input.txt')
print(merged_df.isnull().any().sum())
