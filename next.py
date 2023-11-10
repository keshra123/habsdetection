# 1. READING HTML
# load libraries
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import pandas as pd

# specify url to scrape
url = 'https://news.google.com/q=harmful algal blooms'

# alternative-1 (online parsing)
page = requests.get(url).text

# create an object to scrape various data later
soup = BeautifulSoup(page, 'html.parser')
#print(soup)
#2. PARSING HTML
#title
result_tl = soup.select('article .JtKRv.iTin5e')
title = [t.text for t in result_tl]
print(title)

#date-time
result_dt = soup.select('[datetime]')
timedate = [d['datetime'] for d in result_dt]
print(timedate)

#source
result_src = soup.select('article .vr1PYe')
source = [s.text for s in result_src]
print(source)
#3. PARSING RELATIVE URL INTO ABSOLUTE URL
links = []
# let's turn all relative-url into absolute-url by iterating all links
base_url = 'https://news.google.com/'
for i in soup.select('article .WwrzSb'):
    ss = urljoin(base_url, i.get('href'))
    # put all absolute links into empty list
    links.append(ss)
print(links)
#4. DATAFRAME TO CSV
# putting all of data into a list
all_data = list(zip(source, title, timedate, links))

# convert the list into dataframe
df = pd.DataFrame(all_data, columns=['source', 'title', 'timedate', 'links'])
print(df)
