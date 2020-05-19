from kaggle.api.kaggle_api_extended import KaggleApi

if __name__ == '__main__':
    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files('sudalairajkumar/covid19-in-usa', unzip=True)