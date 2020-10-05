import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


#file = open("blackrock_sustainability_pdf_text.txt","r")
#file = open("citi_whitepaper.txt","r")
# file = open("citi_sust_whitepaper.txt","r")
file = open("ubs_climate_whitepaper_text.txt","r")

all_text = file.read()


tokens = re.findall('[A-Za-z]+', all_text)

# Initialize new list
words = []

# Loop through list tokens and make lower case
for word in tokens:
    words.append(word.lower())

# Get English stopwords and print some of them
sw = nltk.corpus.stopwords.words('english')

# Add to words_ns all words that are in words but not in sw
words_ns = []
for word in words:
    if word not in sw:
        words_ns.append(word)

sns.set()

# Create freq dist and plot
freqdist1 = nltk.FreqDist(words_ns)
#print(freqdist1)
freqdist1.plot(50)
