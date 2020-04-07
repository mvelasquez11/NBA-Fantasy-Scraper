import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.basketball-reference.com/players/h/hardeja01/gamelog/2019/'
page = requests.get(url)
page

page.content