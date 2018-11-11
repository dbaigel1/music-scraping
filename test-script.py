from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime as dt

#get the date
today = dt.today()

newFile = newsTable.read_csv("new_csv.csv")

with open('main_file.csv', 'a') as mf:
    newFile.to_csv(mf, header=False)