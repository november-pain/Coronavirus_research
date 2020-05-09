from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

api.dataset_download_files('imdevskp/corona-virus-report', unzip=True)

api.dataset_download_files('sudalairajkumar/covid19-in-usa', unzip=True)
