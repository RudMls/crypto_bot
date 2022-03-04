from app.enums import Asset
from app.service.binance_service import BinanceService
from app.service.strategy_service import StrategyService, StrategyParameters
from datetime import datetime, timedelta
from binance.client import Client, BaseClient


def coinapi_example():
    try:
        current_date = datetime.now()
        # time_start = (current_date - timedelta(30)).strftime('%Y-%m-%dT%H:%M:%S')
        # time_end = current_date.strftime("%Y-%m-%dT%H:%M:%S")
        # asset_id_base = Asset.ELROND.value
        # asset_id_quote = Asset.TETHER.value
        # period_id = '1HRS'
        # coinapi_service = CoinApiService()
        # data_frame = coinapi_service.get_exchange_rates(asset_id_base, asset_id_quote, period_id, time_start, time_end)
        # print(data_frame)
    except Exception as e:
        print(e)


def binance_service_example():
    try:
        binance_service = BinanceService()
        strategy_service = StrategyService(binance_service)

        # balance = binance_service.get_balance(Asset.EURO)
        # symbol = Symbol.ELROND_EURO
        kline_interval = Client.KLINE_INTERVAL_1MINUTE
        # _30_min_ago = '30 minutes ago UTC'
        # current_date = datetime.now()
        # start_time = datetime(2021, 6, 1).strftime('%d %B, %Y')
        # end_time = datetime.now().strftime('%d %B, %Y')
        # lookback = '30 m'
        # historical_klines = binance_service.get_historical_klines(symbol, kline_interval, lookback)
        # print(historical_klines)
        #
        # mobile_average_intervals = [10, 50]
        # mobile_averages = []
        #
        # for interval in mobile_average_intervals:
        #     ma = algorithm_service.get_moving_average(historical_klines['close'], interval)
        #     historical_klines['ma_' + str(interval)] = ma
        #     mobile_averages.append((ma, interval))
        # historical_klines['action'] = algorithm_service.buy_and_sell(mobile_averages[0][0], mobile_averages[1][0], 10)
        # # matplotlib
        # open_time_values = historical_klines['open_time']
        # close_values = historical_klines['close']
        # plt.figure(figsize=(10, 5))
        # plt.ylabel(symbol.value)
        # plt.plot(open_time_values, close_values)
        # for mobile_average in mobile_averages:
        #     plt.plot(open_time_values, mobile_average[0], label=f'MA{mobile_average[1]}')
        # for row in historical_klines[historical_klines['action'] != Action.NOTHING].\
        #         filter(items=['open_time', 'action']).iterrows():
        #     plt.axvline(x=row[1]['open_time'], color='r' if row[1]['action'] == Action.BUY else 'y')
        # plt.legend()
        # plt.show()
    except Exception as e:
        print(e)


if __name__ == '__main__':

    start_time: str = (datetime.now() - timedelta(15)).strftime('%d %B, %Y')
    end_time: str = '1 minute'
    interval: str = BaseClient.KLINE_INTERVAL_1HOUR
    fiat_asset: Asset = Asset.EURO
    crypto_asset: Asset = Asset.BITCOIN
    binance_service: BinanceService = BinanceService()
    test = binance_service.get_amount(Asset.EURO)
    strategy_parameters: StrategyParameters = StrategyParameters(start_time, end_time, interval, fiat_asset, crypto_asset)
    strategy_service: StrategyService = StrategyService(binance_service, strategy_parameters)
    strategy_service.run()