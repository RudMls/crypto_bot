import unittest

from app.service.binance_service import BinanceService


class BinanceServiceTest(unittest.TestCase):

    def test_binance_service_is_instance_of_binance_service(self):
        binance_service = BinanceService()
        self.assertIsInstance(binance_service, BinanceService)
