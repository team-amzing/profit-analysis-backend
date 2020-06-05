import pandas as pd
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import string
from bs4 import BeautifulSoup
from get_data.get_data import get_current_value
import SentimentAnalysisNewsHeadlines
#nltk.download('vader_lexicon')
 
#xl_file = pd.read_excel("NewsHeadlinesJan2020.xlsx", sheet_name=None, Index=None)
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#stop_words = open("C:\\Users\\infec\\Desktop\\NLTK's list of english stopwords.txt")
StringArray = []
negative = 0
positive = 1
positive_words = []
negative_words = []
def phrases_sa():
    diff_from_previous_day = 0
    for i in range(len(xl_file['Sheet1']['Articles (spaced with commas)'])):
        result = re.sub(r'[^a-zA-Z]', " ", xl_file['Sheet1']['Articles (spaced with commas)'][i])
        StringArray.append(result)
        if int(xl_file['Sheet1']['Difference from previous day'][i]) < diff_from_previous_day:
            s = xl_file['Sheet1']['Articles (spaced with commas)'][i]
            no_punct = ""
            for char in s:
                if char not in punctuations:
                    no_punct = no_punct + char
            no_punct = no_punct.lower()
            string_to_array = no_punct.split(" ")
            with open("C:\\Users\\infec\\Desktop\\NLTK's list of english stopwords.txt") as f:
                lines = f.read().splitlines()
                #print (lines)
                for word in string_to_array:
                    #print ("word = ", word)
                    if word not in lines:
                        negative_words.append(word)
        else:
            s = xl_file['Sheet1']['Articles (spaced with commas)'][i]
            no_punct = ""
            for char in s:
                if char not in punctuations:
                    no_punct = no_punct + char
            no_punct = no_punct.lower()
            string_to_array = no_punct.split(" ")
            with open("C:\\Users\\infec\\Desktop\\NLTK's list of english stopwords.txt") as f:
                lines = f.read().splitlines()
                #print (lines)
                for word in string_to_array:
                    #print ("word = ", word)
                    if word not in lines:
                        positive_words.append(word)
        diff_from_previous_day == float(xl_file['Sheet1']['Difference from previous day'][i])
    #Positive words that have seen an increase in the price of oil
    print ("Counting positive words...")
    CountFrequency(positive_words)
    #print ("Counting negative words...")
    #CountFrequency(negative_words)  
 
def CountFrequency(my_list):
  
    # Creating an empty dictionary 
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        if(value > 10):
            print ("% s : % d"%(key, value))
 
