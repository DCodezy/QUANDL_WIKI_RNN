'''
Training a basic RNN on Quandl's WIKI EOD pricing, 3/14/2017
Uses Keras with tensorflow backend
'''
from __future__ import print_function
import numpy as np
import pandas as pd
import psutil

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
from keras.callbacks import ModelCheckpoint

DO_PREPROCESSING = False
DO_TRAINING = True
DO_PREDICTION = False

# Preprocessing variables
DATA_DIR = '~/Downloads/WIKI_PRICES_212.csv'
TICKER_COL = 'ticker'
DATE_COL = 'date'
NPARRAY_COLUMNS = ['open', 'close', 'high', 'low', 'volume']
MIN_DAYS_ACTIVE = 1000
CUT_FIRST_DAYS = 100
TICKERS_NAME_FILENAME = 'tickerNames.npy'
TICKERS_DATA_FILENAME = 'tickerData.npy'

# Training variables


# Prediction variables


def preprocessing(csv_dir):
    raw_df = pd.read_csv(DATA_DIR)
    raw_df = raw_df[[TICKER_COL, DATE_COL] + NPARRAY_COLUMNS]
    unique_tickers = raw_df[TICKER_COL].unique()
    # Transfer from pandas to dict of tickers to numpy arrays (dtype=float32)
    ticker_names = []
    data_in = []
    for (i, ticker) in enumerate(unique_tickers):
        temp_data = raw_df[raw_df.ticker == ticker] \
            .drop([TICKER_COL, DATE_COL], 1) \
            .as_matrix()
        if temp_data.shape[0] > MIN_DAYS_ACTIVE:
            temp_data = temp_data[CUT_FIRST_DAYS:]
            ticker_names.append(ticker)
            data_in.append(temp_data.astype(np.float32))
        if (i % 100) == 0:
            print(i)
            print("Memory used: " + str(psutil.virtual_memory()[2]) + '%')
    np.save(TICKERS_NAME_FILENAME, np.array(ticker_names))
    np.save(TICKERS_DATA_FILENAME, np.array(data_in))
    print('Start tickers: ' + str(len(unique_tickers)))
    print('End tickers: ' + str(len(data_dict)))

def train_test_split():


def begin_training():
    model = Sequential()
    model.add(LSTM)
