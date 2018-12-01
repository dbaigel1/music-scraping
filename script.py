#Created by Daniel Baigel 11/10/18

from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime as dt
import csv
from textblob import TextBlob
#create a bunch of soup, one for each news source
#then scrape the headlines and see how they trend each day
#dataframe should have column names of: date, 4 news sources, type of headline, positive/neutral/negative trend
#further applications:
#	create categories for types of news: sports, politics, environment, current events
#   and then label them as positive, neutral, or negative using machine learning
# add breitbart and buzzfeed

#get the date
today = dt.today()


##########################Get the soup ready##################################################

###########################FOX#################################################
urlFOX = requests.get("https://www.foxnews.com/")
if urlFOX.status_code != 200:
    print(urlFOX.status_code + "\n")
    print("Something is wrong with Fox...")
    sys.exit("Check website status code")

soupFOX = BeautifulSoup(urlFOX.content, 'html.parser')

FOXcontainer = soupFOX.find(class_="collection collection-spotlight has-hero")
FOXcontainer2 = FOXcontainer.find('header', class_='info-header')

FOXheadline = FOXcontainer2.find('a').get_text()
foxBlob = TextBlob(FOXheadline)
foxPolarity = foxBlob.sentiment.polarity
print(FOXheadline)
print(foxPolarity)
print("Done with FOX")

##########################NBC#################################################
urlNBC = requests.get("https://www.nbcnews.com/")

if urlNBC.status_code != 200:
    print(urlNBC.status_code + "\n")
    print("Something is wrong with NBC...")
    sys.exit("Check website status code")

soupNBC = BeautifulSoup(urlNBC.content, 'html.parser')

NBCcontainer = soupNBC.find('article', class_="teaseCard content___3FGvZ")

NBCcontainer2 = NBCcontainer.find_all('h2')

NBCheadline = NBCcontainer2[1].find('a').get_text()
nbcBlob = TextBlob(NBCheadline)
nbcPolarity = nbcBlob.sentiment.polarity
print(NBCheadline)
print(nbcPolarity)
print("Done with NBC")

# ##########################WP#################################################
urlWP = requests.get("https://www.washingtonpost.com/?noredirect=on")
if urlWP.status_code != 200:
    print(urlWP.status_code + "\n")
    print("Something is wrong with Washington Post...")
    sys.exit("Check website status code")

soupWP = BeautifulSoup(urlWP.content, 'html.parser')

WPcontainer = soupWP.find(class_="headline small normal-style text-align-inherit ")
WPheadline = WPcontainer.find('a').get_text()
print(WPheadline)
wpBlob = TextBlob(WPheadline)
wpPolarity = wpBlob.sentiment.polarity

print(wpPolarity)
print("Done with WP")

# ##########################WP#################################################
urlABC = requests.get("https://abcnews.go.com/")
if urlABC.status_code != 200:
    print(urlABC.status_code + "\n")
    print("Something is wrong with ABC...")
    sys.exit("Check website status code")

soupABC = BeautifulSoup(urlABC.content, 'html.parser')

ABCcontainer = soupABC.find(id="row-1", class_="rows")

ABCheadline = ABCcontainer.find('h1').get_text().strip()
print(ABCheadline)
abcBlob = TextBlob(ABCheadline)
abcPolarity = abcBlob.sentiment.polarity
print(abcPolarity)
print("Done with ABC")


####################################################################################

urlBB = requests.get("https://www.breitbart.com/")
if urlBB.status_code != 200:
    print(urlBB.status_code + "\n")
    print("Something is wrong with Breitbart...")
    sys.exit("Check website status code")

soupBB = BeautifulSoup(urlBB.content, 'html.parser')

BBcontainer = soupBB.find(class_="top_article_main")

BBheadline = BBcontainer.find('h2').get_text().strip()
print(BBheadline)
bbBlob = TextBlob(BBheadline)
bbPolarity = bbBlob.sentiment.polarity
print(bbPolarity)
print("Done with BB")

####################################################################################


urlBF = requests.get("https://www.buzzfeed.com/")
if urlBF.status_code != 200:
    print(urlBF.status_code + "\n")
    print("Something is wrong with BuzzFeed...")
    sys.exit("Check website status code")

soupBF = BeautifulSoup(urlBF.content, 'html.parser')

BFcontainer = soupBF.find(class_="featured-card__body")

BFheadline = BFcontainer.find('h1').get_text().strip()
print(BFheadline)
bfBlob = TextBlob(BFheadline)
bfPolarity = bfBlob.sentiment.polarity
print(bfPolarity)
print("Done with BF")

####################################################################################

#Create a pandas dataframe
columnNames = ["Date", "Fox Headline", "Fox Polarity", 
"NBC Headline", "NBC Polarity", "Wash Post Headline", "Wash Post Polarity",
 "ABC Headline", "ABC Polarity", "Breitbart Headline", "Breitbart Polarity",
 "Buzzfeed Headline", "Buzzfeed Polarity"]

newsTable = pd.DataFrame(columns = columnNames)
newsTable.loc[0] = [today, FOXheadline, foxPolarity, NBCheadline, nbcPolarity,
 WPheadline, wpPolarity, ABCheadline, abcPolarity, BBheadline, bbPolarity, 
 BFheadline, bfPolarity]
print(newsTable)

#append csv onto main csv file
newFile = newsTable.to_csv('new_csv.csv', index = None, header=False)

sourceFile = open('new_csv.csv', 'r')
data = sourceFile.read()
with open('test_file.csv', 'a') as destFile:
    destFile.write(data)












