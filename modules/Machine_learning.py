# IMPORT LIBRARIES

import math
from pandas_datareader import data as pdr
import numpy as np
import pandas as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yfin

# GET THE STOCK INFORMATION
# I'll be using the online dataset for apple stocks for this program

yfin.pdr_override()

start = dt.datetime(2012, 1, 1)
end = dt.datetime(2023, 7, 11) # Current date

df = pdr.get_data_yahoo('AAPL', start, end)
#print(df)

# VIEW THE ROWS AND COLUMNS
# 2897 rows and 6 columns up until today's date being the 11 July

#print(df.shape)

# VISUALIZE THE DATE

#plt.title('History of Closing Prices')
#plt.plot(df['Close'])
#plt.xlabel("Date")
#plt.ylabel("Closing Prices")
#plt.show()

# ISOLATE THE CLOSED PRICES SECTION

data = df.filter(['Close']) # Only keeping the Close column

# DATE COMVERRION
# We need the data in the apprporiate unit, or format, so I would convert it to a numpy array

dataset = data.values

# DATA TRAINING TRIMMING
# Since we're using 1 column, we need to decide how many rows we want to use for the training data, we'll do 80% in our case

amount_training_data = math.ceil(len(dataset) * .8) # 80%

#print(amount_training_data) 2318 when printed(80/100 * 2897)

# SCALING THE DATA
# This included preprocess, scaling, normalizations and other stuff to the input data, before going into the network
# This is basically preparing the data

scaler = MinMaxScaler(feature_range=(0, 1)) # Values before 0 and 1
new_data = scaler.fit_transform(dataset) # Transforms the data based on the minimum and max values used for scaling

#print(new_data)

# THE TRAINING DATASET

train_data = new_data[0:amount_training_data, :] # Colon at the end gets back all the columns

# SPLITTING THE TRAINING DATA
# Into x_train and y_train
# x_train is the independent training data
# y_train is the dependent training data or target variable

x_train = []
y_train = []

for i in range(60, len(train_data)):
    # append past 60 values to the x_train dataset
    x_train.append(train_data[i-60:i, 0]) # Not including i, has 60 values(to 59 according to python index)
    y_train.append(train_data[i, 0]) # The 61'st data value
    
    if i <= 60:
        print(x_train)
        print("")
        print(y_train)
