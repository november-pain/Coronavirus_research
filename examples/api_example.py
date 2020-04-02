from kaggle.api.kaggle_api_extended import KaggleApi
import zip_processor as zp

api = KaggleApi()
api.authenticate()

api.dataset_download_files('imdevskp/corona-virus-report')

zp.ZipProcessor('corona-virus-report.zip').unzip_files()
