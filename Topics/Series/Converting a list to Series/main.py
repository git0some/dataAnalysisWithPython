import pandas as pd

def create_series(foods, calories):
    calorie_series = pd.Series(calories, index=foods, name='Calorie content')
    return calorie_series

# foods = ['bagel', 'pasta', 'rice']
# calories = [310, 110, 140]
#
# calorie_series = create_series(foods, calories)
# print(calorie_series)

