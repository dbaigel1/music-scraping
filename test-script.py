from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime as dt
from textblob import TextBlob



text = '''
13 Dogs With Vitiligo Who Will Warm Your Cold, Unloving Heart
'''

blob = TextBlob(text)

#sentiment analysis -- tuple of (polarity, subjectivity).
# polarity is range -1 to 1, -1 being polar negative, 1 being polar positive
#subjectivity is range 0 to 1, 1 being subjective, 0 being objective
print(blob.sentiment)