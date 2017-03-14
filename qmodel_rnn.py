'''
Training a basic RNN on Quandl's WIKI EOD pricing, 3/14/2017
Uses Keras with tensorflow backend
'''
from __future__ import print_function
import numpy as np
import pandas as pd

DATA_DIR = '~/Downloads/WIKI_PRICES_212.csv'
TICKER_COL = 'ticker'
NPARRAY_COLUMNS = ['date', 'open', 'close', 'high', 'low', 'volume']
MIN_DAYS_ACTIVE = 1000
CUT_FIRST_DAYS = 100

# Preprocessing-----------------------------------------------------------------
raw_df = pd.read_csv(DATA_DIR)
raw_df = raw_df[[TICKER_COL] + NPARRAY_COLUMNS]
unique_tickers = raw_df[TICKER_COL].unique()
# Transfer from pandas to dict of tickers to numpy arrays (dtype=float32)
data_dict = {}
for ticker in unique_tickers:
    temp_data = raw_df[raw_df.ticker == ticker].as_matrix()
    if temp_data.shape[0] > MIN_DAYS_ACTIVE:
        temp_data = temp_data[CUT_FIRST_DAYS:]
        data_dict[ticker] = temp_data.astype(np.float32)

print('Starting columns: ' + str(len(raw_df.columns)))
print('Ending columns: ' + str(len([TICKER_COL] + NPARRAY_COLUMNS)))
print('Start tickers: ' + str(len(unique_tickers)))
print('End tickers: ' + str(len(data_dict)))
