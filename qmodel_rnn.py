'''
Training a basic RNN on Quandl's WIKI EOD pricing, 3/14/2017
Uses Keras with tensorflow backend
'''
from __future__ import print_function
import numpy as np
import pandas as pd

DATA_DIR = '~/Downloads/WIKI_PRICES_212.csv'
TICKER_COL = 'ticker'
DATE_COL = 'date'
NPARRAY_COLUMNS = ['open', 'close', 'high', 'low', 'volume']
MIN_DAYS_ACTIVE = 1000
CUT_FIRST_DAYS = 100

# Preprocessing-----------------------------------------------------------------
raw_df = pd.read_csv(DATA_DIR)
raw_df = raw_df[[TICKER_COL, DATE_COL] + NPARRAY_COLUMNS]
unique_tickers = raw_df[TICKER_COL].unique()
# Transfer from pandas to dict of tickers to numpy arrays (dtype=float32)
data_dict = {}
for (i, ticker) in enumerate(unique_tickers):
    temp_data = raw_df[raw_df.ticker == ticker].drop([TICKER_COL, DATE_COL], 1).as_matrix()
    if temp_data.shape[0] > MIN_DAYS_ACTIVE:
        temp_data = temp_data[CUT_FIRST_DAYS:]
        data_dict[ticker] = temp_data.astype(np.float32)
    if i % 100 == 0:
	print(i)

print('Starting columns: ' + str(len(raw_df.columns)))
print('Ending columns: ' + str(len([TICKER_COL, DATE_COL] + NPARRAY_COLUMNS)))
print('Start tickers: ' + str(len(unique_tickers)))
print('End tickers: ' + str(len(data_dict)))
