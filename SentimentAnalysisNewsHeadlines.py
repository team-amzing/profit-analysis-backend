import requests
import re
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup
StringArray = []
def showCurrentPrice():
    page = requests.get('https://oilprice.com/Latest-Energy-News/World-News')
    soup = BeautifulSoup(page.text, 'html.parser')
    currentPrices = soup.findAll(class_='categoryArticle')
    for price in currentPrices:
        rawArticle = price.find('div', attrs={'class': 'categoryArticle__content'})
        #print(bar.text)
        StringArray.append(rawArticle.text)
        #print(price)
def fillStringArrayTest():
    StringArray.append("The oil price is rising, it's reaching never before seen levels.")
    StringArray.append("This is a great time to sell oil, you should definitely sell your oil today.")
    StringArray.append("Oil price is high.")
def run():
    #Web Scraper
    showCurrentPrice()
    #Test
    #fillStringArrayTest()

    for eachString in StringArray:
        result = re.sub(r'[^a-zA-Z]', " ", eachString)
        StringArray.remove(eachString)
        StringArray.append(result)

    for eachString in StringArray:
        if "oil" in eachString or "wti" in eachString:
            print ("")
        else:
            StringArray.remove(eachString)


    #print (StringArray)
    sid = SentimentIntensityAnalyzer()
    overallScore = 0
    for eachString in StringArray:
        ss = sid.polarity_scores(eachString)
        #Remove the comment below to find what the text in the articles consists of
        #print (eachString, " has a score of ", ss['compound'])
        overallScore += ss['compound']
        #print("\n")

    print ("Overall score: ", overallScore / len(StringArray))
    return overallScore

run()