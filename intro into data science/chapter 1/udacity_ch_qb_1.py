import numpy
import pandas
import statsmodels.api as sm

def simple_heuristic():

    predictions = {}
    df = pandas.read_csv('titanic_data.csv')
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if passenger['Sex'] == 'male':
            predictions[passenger_id] = 0
        if passenger['Sex'] == 'female':
            predictions[passenger_id] = 1
        
        
    return predictions

simple_heuristic()