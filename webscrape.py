
#Sustainability: The future of investing
url = 'https://www.blackrock.com/us/individual/insights/blackrock-investment-institute/sustainability-the-future-of-investing'

import requests

# Make the request and check object type
r = requests.get(url)
type(r)

# Extract HTML from Response object and print
html = r.text
#print(html)

# Import BeautifulSoup from bs4
from bs4 import BeautifulSoup

# Create a BeautifulSoup object from the HTML
soup = BeautifulSoup(html, features="html.parser")
type(soup)

text = soup.findAll('p')[31:40]

paragraphs = []

for p in text:
    paragraph = p.text
    paragraphs.append(paragraph)

all_text = ' '.join(paragraphs)

# Import regex package
import re

tokens = re.findall('\w+', all_text)

# Initialize new list
words = []

# Loop through list tokens and make lower case
for word in tokens:
    words.append(word.lower())

import nltk
from nltk.corpus import stopwords

# Get English stopwords and print some of them
sw = nltk.corpus.stopwords.words('english')

# Initialize new list
words_ns = []

# Add to words_ns all words that are in words but not in sw
for word in words:
    if word not in sw:
        words_ns.append(word)

#Import datavis libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Figures inline and set visualization style
import matplotlib.pyplot as plt

sns.set()

# Create freq dist and plot
freqdist1 = nltk.FreqDist(words_ns)
freqdist1.plot(50)
