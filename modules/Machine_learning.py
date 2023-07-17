# IMPORT LIBRARIES

import math
from pandas_datareader import data as pdr
import numpy as np
import pandas as pd
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

    #if i <= 60:
        #print(x_train)
        #print("")
        #print(y_train)
        
# CONVERTING THE TRAINING DATA/RESHAPING THE DATA

x_train, y_train = np.array(x_train), np.array(y_train) # Converting the 2 lists to nupy arrays

# RESHAPING THE DATASET
# For the recurrent neural network, the input has to be 3-dimensional(samples, time steps and features)
# Currently only in 2 dimensions, as seen with df.shape
# x_train = 2258 rows
# Features for us is just the closing price

#print(x_train.shape)

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1)) # taking the 2258 samples and the 60 columns(2258, 60, 1)
#print(x_train.shape)

# BUILDING THE NEURAL NETWORK
# Consists of 4 layers, 2 LSTM layers and 2 dense layers
# LSTM layers each have 50 neurons and the Dense layers have 25 and 1 neuron

model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1))) # First layer of the neural networ, 50 neurons, return sequencs is true, because we have a second layer, the input shape is the time steps(60) and features being 1
model.add(LSTM(50, return_sequences=False)) # No more LSTM layers so return sequences is False
model.add(Dense(25)) 
model.add(Dense(1))

# COMPILING THE MODEL
# Optimizer improves the loss function
# Loss function measures how well the model does on the training

model.compile(optimizer='adam', loss='mean_squared_error') # Optimization and loss function

# TRAIN THE MODEL
# epoch is the number of iterations you want to test when the model is going through a neural network

model.fit(x_train, y_train, batch_size=1, epochs=1)


# THE TESTING DATASET

test_data = new_data[amount_training_data - 60: , :] # Gets the data from 2318 to 2897

# X_TEST AND Y_TEST

x_test = []
y_test = dataset[amount_training_data: , :] # All the values we want our model to predict, remember before the many x_values and 1 value, we are collecting all those y_values

for i in range(60, len(test_data)):
    x_test.append(test_data[i-60:i, 0]) # Contains the past 60 values

# CONVEST TEST DATA TO A NUMPY ARRAY

x_test = np.array(x_test)

# RESHAPE THE TEST DATA

x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# GET THE PREDICTED PRICE VALUES FOR X_TEST

predictions = model.predict(x_test) # We want these values to be as similar to that of the values in y_test
predictions = scaler.inverse_transform(predictions) # Unscaling the values

# MODEL EVALUATION
# RMSE, is an error method, lower values indicate a better fit

rmse = np.sqrt(np.mean(predictions-y_test)**2)
#print(rmse)

# PLOT THE DATA

train = data[:amount_training_data] # From 0 to the len of the training data
valid = data[amount_training_data:] # From the len of training data to the end of the dataset
valid['Predictions'] = predictions

# DRAW THE GRAPH

'''

def Graph():
    plt.figure(figsize=(5, 4))
    plt.title("Machine learning")
    plt.xlabel('Date', fontsize=8)
    plt.ylabel('Closing price', fontsize=8)
    plt.plot(train['Close']) # The training data
    plt.plot(valid[['Close', 'Predictions']])
    plt.legend(['Train', 'Validations', 'Predictions'], loc='lower right')
    plt.show()
    
'''

# Run the graph

#Graph()

# SHOW THE ACTUAL AND PREDICTED PRICE  
# Shows the data of the actual and predicted values

#print(valid)

