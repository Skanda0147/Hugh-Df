import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#Import large dataframe 1 for power and fuel flow
filename = '/Users/skanda/Desktop/data/merged.csv'

df = pd.read_csv(filename)

df = pd.read_csv(filename, usecols=['POWER', 'FUEL_FLOW'])

print(df.mean)


#Import smaller dataframe 2 for fuel lhv
filename2 = '/Users/skanda/Desktop/hackathon/site_metadata-7fc535965d0c074cea0be6786fc9518e.csv'

df1 = pd.read_csv(filename2)

df2 = pd.read_csv(filename2, usecols=['FUEL_LHV'])
print(df2.describe())

#compute realistic average via outliers mentioned by function above
avg_power = (13905.170113666487 +  13948.422258375154 + 13915.43013198364 + 13924.413251462029 + 13951.96104056358 + 10810.204483179057 + 10767.152156142249 + 10782.802431228314 + 10871.84466777456 + 10832.466988434317)/10
avg_fuelflow = (1.7758341984035289 + 1.7776042398102652 + 1.7751226468089785 + 1.776513778829521 + 1.7766576910212637 + 1.6654014852353027 + 1.6628371623150042 + 1.661486919932626 + 1.6689819821512686 +  1.6642119344785267)/10

therm_eff = (21507.259316/(avg_power * avg_fuelflow))*100
print(therm_eff)


