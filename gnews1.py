# load libraries
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import pandas as pd

# specify url to scrape
url = 'https://news.google.com/search?q=algal blooms'

# alternative-1 (online parsing)
page = requests.get(url).text

# create an object to scrape various data later
soup = BeautifulSoup(page, 'html.parser')

#title
result_tl = soup.select('article .DY5T1d.RZIKme')
title = [t.text for t in result_tl]
print(title)
#date-time
result_dt = soup.select('[datetime]')
timedate = [d['datetime'] for d in result_dt]
print(timedate)
#source
result_src = soup.select('article .wEwyrc.AVN2gc.uQIVzc.Sksgp.slhocf')
source = [s.text for s in result_src]
#print(source)
links = []
# let's turn all relative-url into absolute-url by iterating all links
base_url = 'https://news.google.com/'
for i in soup.select('article .DY5T1d.RZIKme'):
    ss = urljoin(base_url, i.get('href'))
    # put all absolute links into empty list
    links.append(ss)
print(links)
# putting all of data into a list
all_data = list(zip(source, title, timedate, links))

# convert the list into dataframe
df = pd.DataFrame(all_data, columns=['source', 'title', 'timedate', 'links'])

print(df)
# save to csv
#df.to_csv(r'/Users/keshra123', index=False)
#df.head()

