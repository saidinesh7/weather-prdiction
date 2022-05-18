# importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# read the data in a pandas dataframe
data = pd.read_csv("austin_weather.csv")
#seeing head values
data.head(5)
#seeing shape of the dataset
data.shape
#filling missing NULL values by column means
data.fillna(data.mean())
# drop or delete the unnecessary columns in the data.
data=data.drop(['Events','Date','SeaLevelPressureHighInches', 'SeaLevelPressureLowInches'],
axis = 1)
# some values have 'T' which denotes trace rainfall
# we need to replace all occurrences of T with 0
# so that we can use the data in our model
data = data.replace('T', 0.0)
# the data also contains '-' which indicates no
# or NIL. This means that data is not available
# we need to replace these values as well.
data = data.replace('-', 0.0)
# save the data in a csv file
data.to_csv(‘austin_final_final.csv')

CMRTC 15

Weather