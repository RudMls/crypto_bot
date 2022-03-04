from enum import Enum


class Asset(Enum):
    BITCOIN = 'BTC'
    ETHEREUM = 'ETH'
    TETHER = 'USDT'
    ELROND = 'EGLD'
    EURO = 'EUR'

    
class Symbol(Enum):
    BITCOIN_TETHER = 'BTCUSDT'
    BITCOIN_EURO = 'BTCEUR'
    ETHEREUM_TETHER = 'ETHUSDT'
    ETHEREUM_EURO = 'ETHEURO'
    ELROND_TETHER = 'EGLDUSDT'
    ELROND_EURO = 'EGLDEUR'
    TETHER = 'USDT'
    EURO = 'EUR'



