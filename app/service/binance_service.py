from binance.client import Client
import pandas as pd
import os

from app.enums import Asset


class BinanceService:

    def __init__(self):
        self.client = Client(
            os.environ.get('binance_key'),
            os.environ.get('binance_secret')
        )

    def get_all_symbols(self):
        return [s['symbol'] for s in (self.client.get_exchange_info())['symbols']]

    def get_historical_klines(self, symbol: str, interval: str, start_time: str, lookback: str) -> pd.DataFrame:
        try:
            historical_klines = self.client.get_historical_klines(symbol, interval, start_time, f'{lookback} ago UTC')
            data_frame = pd.DataFrame(historical_klines, columns=[
                'open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume',
                'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
            ])
            data_frame[['open_time', 'close_time']] = data_frame[['open_time', 'close_time']].apply(pd.to_datetime,
                                                                                                    unit='ms')
            data_frame[['open', 'high', 'low', 'close']] = data_frame[['open', 'high', 'low', 'close']].apply(
                pd.to_numeric)
            return data_frame
        except Exception as e:
            print(e)

    def get_symbol_ticker(self, symbol: str):
        return self.client.get_symbol_ticker(symbol=symbol)

    def __get_account(self):
        return self.client.get_account()

    def __get_balance(self, asset: Asset) -> list:
        try:
            return [index for index in self.__get_account()['balances'] if index['asset'] == asset.value]
        except Exception as e:
            print(e)

    def get_amount(self, asset: Asset) -> float:
        return self.__get_balance(asset)[0]['free']
