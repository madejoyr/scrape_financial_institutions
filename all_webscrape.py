#python -m nltk.downloader stopwords

import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


#Sustainability: The future of investing
blackrock_urls = ['https://www.blackrock.com/us/individual/insights/blackrock-investment-institute/sustainability-the-future-of-investing', 'https://www.blackrock.com/us/individual/insights/blackrock-investment-institute/esg-fixed-income', 'https://www.blackrock.com/us/individual/insights/sustainable-investing-beyond-compliance', 'https://www.blackrock.com/us/individual/investment-ideas/sustainable-investing', 'https://www.blackrock.com/corporate/sustainability/committed-to-sustainability', 'https://www.blackrock.com/corporate/insights/blackrock-investment-institute/publications/troubled-waters', 'https://www.blackrock.com/corporate/about-us/sustainability-resilience-research', 'https://www.blackrock.com/corporate/insights/blackrock-investment-institute/publications/sustainability-in-portfolio-construction', 'https://www.blackrock.com/corporate/investor-relations/larry-fink-ceo-letter', 'https://www.blackrock.com/corporate/insights/blackrock-investment-institute/publications/physical-climate-risks', 'https://www.blackrock.com/corporate/sustainability', 'https://www.blackrock.com/corporate/responsibility/human-capital', 'https://www.blackrock.com/corporate/responsibility/environmental-sustainability', 'https://www.blackrock.com/corporate/responsibility/ethics-and-integrity', 'https://www.blackrock.com/corporate/about-us/investment-stewardship#engagement-priorities', 'https://www.blackrock.com/corporate/about-us/social-impact', 'https://www.blackrock.com/corporate/responsibility/health-and-safety']

citi_urls = ['https://www.citigroup.com/citi/sustainability/', 'https://www.citigroup.com/citi/sustainability/policies.htm', 'https://www.citigroup.com/citi/sustainability/evolution.htm', 'https://www.citigroup.com/citi/about/esg/', 'https://www.citigroup.com/citi/about/esg/citi-at-a-glance.html', 'https://www.citigroup.com/citi/about/esg/citizenship-approach.html', 'https://www.citigroup.com/citi/about/esg/citi-the-sustainable-development-goals.html', 'https://www.citigroup.com/citi/about/esg/citi-impact-fund.html']

ubs_urls = ['https://www.ubs.com/global/en/wealth-management/sustainable-investing.html', 'https://www.ubs.com/global/en/wealth-management/sustainable-investing/education.html', 'https://www.ubs.com/global/en/wealth-management/our-service/sustainable-investing-solutions.html', 'https://www.ubs.com/global/en/wealth-management/chief-investment-office/investment-opportunities/sustainable-investing/2020/sustainable-investing-after-covid19.html']


def word_freq(url_list):
    # Initialize new list
    words_ns = []

    for url in url_list:
        # Make the request and check object type
        r = requests.get(url)
        type(r)

        # Extract HTML from Response object and print
        html = r.text
        #print(html)

        # Create a BeautifulSoup object from the HTML
        soup = BeautifulSoup(html, features="html.parser")
        type(soup)

        text = soup.findAll('p')
        #[31:40]

        paragraphs = []

        for p in text:
            paragraph = p.text
            paragraphs.append(paragraph)

        all_text = ' '.join(paragraphs)


        tokens = re.findall('[A-Za-z]+', all_text)

        # Initialize new list
        words = []

        # Loop through list tokens and make lower case
        for word in tokens:
            words.append(word.lower())

        # Get English stopwords and print some of them
        sw = nltk.corpus.stopwords.words('english')


        # Add to words_ns all words that are in words but not in sw
        for word in words:
            if word not in sw:
                words_ns.append(word)


    sns.set()

    # Create freq dist and plot
    freqdist1 = nltk.FreqDist(words_ns)
    #print(freqdist1)
    freqdist1.plot(50)




#word_freq(blackrock_urls)
#word_freq(citi_urls)
word_freq(ubs_urls)
