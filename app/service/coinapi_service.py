# import json
# import requests
# import pandas as pd
#
# from app.exception.response_exception import ResponseException
# from config.api_config import COIN_API_KEY, COIN_API_BASE_URL
#
#
# class CoinApiService:
#
#     def __init__(self):
#         self.base_url = COIN_API_BASE_URL
#         self.headers = {'X-CoinAPI-Key': COIN_API_KEY}
#
#     def get_all_assets(self):
#         try:
#             response = requests.get(self.base_url + '/v1/assets', headers=self.headers)
#             data = json.loads(response.text)
#             return data
#         except Exception as e:
#             print(e)
#
#     #
#     # data frame column
#     #   time_open -> Date d'ouverture
#     #   time_close -> Date de fermeture
#     #   rate_open -> La valeur à la date d'ouverture
#     #   rate_high -> La valeur la plus haute
#     #   rate_low -> La valeur minipale
#     #   rate_close -> La valeur du cour à la fermeture
#     def get_exchange_rates(self, asset_id_base, asset_id_quote, period_id, time_start, time_end) -> pd.DataFrame:
#
#         response = requests.get(
#             url=self.base_url + '/v1/exchangerate/' + asset_id_base + '/' + asset_id_quote + '/history',
#             params={'period_id': period_id, 'time_start': time_start, 'time_end': time_end},
#             headers=self.headers
#         )
#         json_response = json.loads(response.text)
#         if response.status_code == 200:
#             data_frame = pd.DataFrame(json_response)
#             data_frame[['time_period_start', 'time_period_end', 'time_open', 'time_close']] = \
#                 data_frame[['time_period_start', 'time_period_end', 'time_open', 'time_close']].apply(pd.to_datetime)
#             return data_frame
#         else:
#             raise ResponseException(str(response.status_code), json_response['error'])
