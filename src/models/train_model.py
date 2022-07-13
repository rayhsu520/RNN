from keras.layers.core import Dense, Activation, Dropout
from keras.layers import LSTM, GRU
from keras.models import Sequential
from keras import optimizers

def create_model(feature_shape):
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(feature_shape[1],1)))
    model.add(Dropout(0.2))
    model.add(LSTM(100, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation = "linear"))

    model.compile(loss='mse', optimizer='adam')
    print ('model compiled')
    print (model.summary())

    return model