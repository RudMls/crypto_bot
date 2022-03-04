import pandas as pd
import requests
import json
import ta
# https://github.com/bukosabino/ta/
from datetime import datetime, timedelta
from binance.client import Client
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta

url = 'https://api.binance.com/api/v3/klines'

api_key = ''
api_secret = ''

# binance client
client = Client()

# symbol = 'BTCUSDT'
# interval = client.KLINE_INTERVAL_1HOUR
# current_date = datetime.now()
# start_time = (current_date - timedelta(15)).strftime('%d %B, %Y')
# end_time = current_date.strftime('%d %B, %Y')
#
# exchange_info = client.get_exchange_info()
# symbols = [s['symbol'] for s in exchange_info['symbols']]
#
# historical_klines = Client().get_historical_klines(symbol, interval, start_time)
#
# data_frame = pd.DataFrame(historical_klines, columns=[
#     'open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume',
#     'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
# ])
#
# # set index value
# data_frame['open_time'] = pd.to_datetime(data_frame['open_time'], unit='ms')
# data_frame['open'] = pd.to_numeric(data_frame['open'])
#
# # data_frame = data_frame.set_index(data_frame['open_time'])
# # convert index to time
# # data_frame.index = pd.to_datetime(data_frame.index, unit='ms')
# # del data_frame['open_time']
#
# # define indicators
# data_frame['SMA7'] = ta.trend.sma_indicator(data_frame['close'], 7)
# data_frame['SMA25'] = ta.trend.sma_indicator(data_frame['close'], 25)
#
# fig = plt.figure(figsize=(10, 5))
# ax = fig.add_axes([0.1, 0.2, 0.85, 0.7])
# data_frame.plot(kind='line', color='green', x='open_time', y='open', ax=ax)
# data_frame.plot(kind='line', color='yellow', x='open_time', y='SMA7', ax=ax)
# data_frame.plot(kind='line', color='blue', x='open_time', y='SMA25', ax=ax)
# plt.show()
# print(data_frame)
