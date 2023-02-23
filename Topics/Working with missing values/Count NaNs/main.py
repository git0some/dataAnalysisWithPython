#  write your code here 
import pandas as pd
import numpy as np

merged_df = pd.read_csv('data/dataset/input.txt')
print(merged_df.isna().sum())
