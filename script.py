#Created by Daniel Baigel 11/10/18

from bs4 import BeautifulSoup
import requests
import pandas as pd
#create a bunch of soup, one for each news source
#then scrape the headlines and see how they trend each day
#further applications:
#	create categories for types of news: sports, politics, environment, current events
#   and then label them as positive, neutral, or negative using machine learning

##########################Get the soup ready##################################################

############################CNN#################################################
urlCNN = requests.get("https://edition.cnn.com/")
if urlCNN.status_code != 200:
    print(urlCNN.status_code + "\n")
    print("Something is wrong with CNN...")
    sys.exit("Check website status code")

soupCNN = BeautifulSoup(urlCNN.content, 'html.parser')
####TESTING
bodyTag = soupCNN.body
#print(bodyTag.contents)
#for tag in bodyTag.children:
#	print(tag)
#	input("Next Tag press Enter..." + "\n\n\n")
	#add a counter so we know which div to dive into!

#CNNcontainer = soupCNN.find_all('h2')
#CNNheadline = CNNcontainer[0].find('section')
#CNNheadline2 = CNNheadline.find(class_='l-container')

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
print(FOXheadline)
print("Done with FOX")

##########################NBC#################################################
urlNBC = requests.get("https://www.nbcnews.com/")
if urlNBC.status_code != 200:
    print(urlNBC.status_code + "\n")
    print("Something is wrong with NBC...")
    sys.exit("Check website status code")

soupNBC = BeautifulSoup(urlNBC.content, 'html.parser')

NBCcontainer = soupNBC.find('article', class_="teaseCard content___3FGvZ")
NBCcontainer2 = NBCcontainer.find('h2', class_="teaseCard__headline title___1T2jw title___1Fy4v")

NBCheadline = NBCcontainer2.find('a').get_text()
print(NBCheadline)
print("Done with NBC")

# ##########################WP#################################################
urlWP = requests.get("https://www.washingtonpost.com/?noredirect=on")
if urlWP.status_code != 200:
    print(urlWP.status_code + "\n")
    print("Something is wrong with Washington Post...")
    sys.exit("Check website status code")

soupWP = BeautifulSoup(urlWP.content, 'html.parser')

WPcontainer = soupWP.find(class_="headline normal normal-style text-align-inherit ")
WPheadline = WPcontainer.find('a').get_text()
print(WPheadline)
print("Done with WP")

####################################################################################


