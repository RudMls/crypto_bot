import pandas as pd

from app.service.binance_service import BinanceService
from app.enums import Asset
from enum import Enum


class Action(Enum):
    BUY = 'BUY'
    SELL = 'SELL'
    NOTHING = 'NOTHING'


class StrategyParameters:

    def __init__(self, start_time: str, lookback: str, interval: str, fiat_asset: Asset, crypto_asset: Asset) -> None:
        self.start_time: str = start_time
        self.lookback: str = lookback
        self.fiat_asset: Asset = fiat_asset
        self.cryto_asset: Asset = crypto_asset
        self.interval: str = interval


class StrategyService:

    def __init__(self, binance_service: BinanceService, strategy_parameters: StrategyParameters) -> None:
        self.binance_service: BinanceService = binance_service
        self.strategy_parameters: StrategyParameters = strategy_parameters
        self.short_mobile_average: int = 10
        self.long_mobile_average: int = 50
        self.mobile_averages: tuple[int, int] = (10, 50)
        self.initial_amount: dict[Asset, float] = {
            Asset.EURO: 200,
            Asset.BITCOIN: 0
        }

    def run(self) -> None:
        fiat_amount: float = self.binance_service.get_amount(self.strategy_parameters.fiat_asset)
        crypto_amount: float = self.binance_service.get_amount(self.strategy_parameters.cryto_asset)
        historical_klines = self.binance_service.get_historical_klines(
            self.strategy_parameters.cryto_asset.value + self.strategy_parameters.fiat_asset.value,
            self.strategy_parameters.interval,
            self.strategy_parameters.start_time,
            self.strategy_parameters.lookback
        )
        close_values: pd.Series = historical_klines['close']
        for mobile_average in self.mobile_averages:
            historical_klines[f'ma_{mobile_average}'] = self.__get_moving_average(close_values.tolist(), mobile_average)

        print(historical_klines)

    @staticmethod
    def __get_moving_average(values: list[float], inteval: int) -> list[float]:
        averages: list[float] = []
        sum_values: float = 0
        for index in range(len(values)):
            sum_values += values[index]
            if index >= inteval:
                sum_values -= values[index - inteval]
                average: float = sum_values / inteval
            else:
                average: float = sum_values / (index + 1)
            averages.append(average)
        return averages

    @staticmethod
    def __buy_and_sell(short_mobile_average: list, long_mobile_average: list, threshold: int = 0) -> list:
        bayable: bool = True
        threshold_percent = 1 + threshold / 100
        action_list: list[Action] = []
        for index in range(len(short_mobile_average)):
            sma_value = short_mobile_average[index]
            lma_value = long_mobile_average[index]
            if bayable and sma_value > lma_value + threshold_percent:
                action_list.append(Action.BUY)
                bayable = False
            elif not bayable and sma_value < lma_value / threshold_percent:
                action_list.append(Action.SELL)
                bayable = True
            else:
                action_list.append(Action.NOTHING)
        return action_list
