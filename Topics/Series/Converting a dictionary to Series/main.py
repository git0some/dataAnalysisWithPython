import pandas as pd

def create_series(capitals_dict):
    capitals_series = pd.Series(capitals_dict, name='Capitals of the world')
    return capitals_series

#capitals = {'Czech Republic': 'Prague',
#            'Russia': 'Moscow',
#            'Australia': 'Canberra'}
#
#capitals_series = create_series(capitals)
#print(capitals_series)