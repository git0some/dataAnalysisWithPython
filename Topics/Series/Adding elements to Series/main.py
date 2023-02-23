import pandas as pd

def add_records(olympics):
    new_data = {2021: 'Tokyo', 2024: 'Paris', 2028: 'Los Angeles'}
    # create a new Series with the new data
    new_series = pd.Series(new_data, name='olympics')
    # append the new Series to the original Series
    updated_series = olympics.append(new_series)
    # return the updated Series
    return updated_series

# olympics = pd.Series(['Sydney', 'Athens', '...', 'Rio de Janeiro'], index=[2000, 2004, ..., 2016], name='olympics')
# updated_olympics = add_records(olympics)
# print(updated_olympics)
