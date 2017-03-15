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
USE_PERCENTAGES = True
TICKERS_NAME_FILENAME = 'tickerNames_pct.npy'
TICKERS_DATA_FILENAME = 'tickerData_pct.npy'

# Training variables


# Prediction variables

def make_percentages(data_mtx):
    return (data_mtx[1:] - data_mtx[:-1]) / data_mtx[:-1]

def preprocessing_daily():
    raw_df = pd.read_csv(DATA_DIR)
    raw_df = raw_df[[TICKER_COL, DATE_COL] + NPARRAY_COLUMNS]
    unique_tickers = raw_df[TICKER_COL].unique()
    # Transfer from pandas to dict of tickers to numpy arrays (dtype=float32)
    ticker_names = []
    data_in = []
    for (i, ticker) in enumerate(unique_tickers):
        temp_data = raw_df[raw_df.ticker == ticker]
        if temp_data.shape[0] > MIN_DAYS_ACTIVE:
            temp_data = temp_data[CUT_FIRST_DAYS:] \
                .drop([TICKER_COL, DATE_COL], 1) \
                .as_matrix()
            temp_data = temp_data.astype(np.float32)
            if USE_PERCENTAGES:
                temp_data = make_percentages(temp_data)

            ticker_names.append(ticker)
            data_in.append(temp_data)
        if (i % 100) == 0:
            print(i)
            print("Memory used: " + str(psutil.virtual_memory()[2]) + '%')
    np.save(TICKERS_NAME_FILENAME, np.array(ticker_names))
    np.save(TICKERS_DATA_FILENAME, np.array(data_in))
    print('Start tickers: ' + str(len(unique_tickers)))
    print('End tickers: ' + str(len(data_dict)))

def create_sequence():
    print('Creating sequences...')
    seq_in = []
    exp_out = []
    for i in range(0, len(int_data) - WINDOW_SIZE):
        seq_in.append(int_data[i:(i + WINDOW_SIZE)])
        exp_out.append(int_data[i + WINDOW_SIZE])
    print('Memory used: ' + str(psutil.virtual_memory()[2]) + '%')


#def train_test_split():


def begin_training():
    model = Sequential()
    model.add(LSTM)

preprocessing_daily()
