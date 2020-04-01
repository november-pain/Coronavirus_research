import requests
from bs4 import BeautifulSoup

url = "https://www.kaggle.com/imdevskp/corona-virus-report"

rget = requests.get(url)
content = rget.content
soup = BeautifulSoup(content, 'html.parser')

covid_clean = soup.find_all("a")

print(covid_clean)
