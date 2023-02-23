import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

general_df = pd.read_csv('test/general.csv')
prenatal_df = pd.read_csv('test/prenatal.csv')
sports_df = pd.read_csv('test/sports.csv')


def all_df_manipulations():
    # change column names in prenatal and sports dataframe to match general dataframe columns
    prenatal_df.columns = sports_df.columns = general_df.columns
    # Concatenate all dataframes
    global merged_df
    merged_df = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)
    # drop column Unnamed
    merged_df.drop(columns="Unnamed: 0", inplace=True)
    # drop all empty rows
    merged_df.dropna(axis=0, how="all", inplace=True)
    # in column gender replace
    merged_df["gender"].replace(["man", "male", "woman", "female"], ["m", "m", "f", "f"], inplace=True)
    # one hospital does not fill f
    merged_df["gender"].replace(np.nan, "f", inplace=True)
    # fill given columns with 0
    columns = ["bmi", "diagnosis", "blood_test", "ecg", "ultrasound", "mri", "xray", "children", "months"]
    for col in columns:
        merged_df[col] = merged_df[col].fillna(0)


all_df_manipulations()

# Stage 5 Question 1: What is the most common age of a patient among all hospitals?
# Plot a histogram and choose one of the following age ranges: 0-15, 15-35, 35-55, 55-70, or 70-80.
# define the age range bins
age_bins = [0, 15, 35, 55, 70, 80]

# create a new column 'age_range' that specifies the age range for each patient
common_age = merged_df['age'].value_counts().index[0]
merged_df['age_range'] = pd.cut(merged_df['age'], bins=age_bins, labels=['0-15', '15-35', '35-55', '55-70', '70-80'])
age_range = merged_df.loc[merged_df['age'] == common_age, 'age_range'].values[0]

# create a histogram of ages in the subset
age_subset = merged_df[merged_df['age_range'] == age_range]
plt.hist(age_subset['age'], bins=20)

# set the title and labels for the plot
plt.title('Age distribution of patients (' + age_range + ')')
plt.xlabel('Age')
plt.ylabel('Frequency')

# display the plot
plt.show()
print('The answer to the 1st question:', age_range)


# Stage 5 Question 2: What is the most common diagnosis among patients in all hospitals? Create a pie chart.
# count the frequency of each diagnosis and select the most common one
diagnosis_counts = merged_df['diagnosis'].value_counts()
most_common_diagnosis = diagnosis_counts.index[0]

# create a pie chart of diagnosis counts
plt.pie(diagnosis_counts, labels=diagnosis_counts.index)

# set the title for the plot
plt.title('Diagnosis distribution of patients')

# display the plot
plt.show()
print('The answer to the 2nd question:', most_common_diagnosis)


# Stage 5 Question 3: Build a violin plot of height distribution by hospitals.
# Try to answer the questions.
#   a) What is the main reason for the gap in values?
#   b) Why there are two peaks, which correspond to the relatively small and big values?
plt.violinplot(merged_df['age'])
plt.title('Age distribution of patients (' + age_range + ')')
plt.xlabel('Frequency')
plt.ylabel('Age')
# set the title for the plot
plt.title('Age distribution of patients')

# display the plot
plt.show()

answer1 = "pregnant women have a certain age"
answer2 = "young people are sick all the time"
print("The answer to the 3rd question: It's because", answer1, "and", answer2)
# The answer to the 1st question: 0-15
# The answer to the 2nd question: flu
# The answer to the 3rd question: It's because...

