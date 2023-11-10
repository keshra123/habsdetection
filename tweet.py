# 1. READING HTML
# load libraries
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import pandas as pd

# specify url to scrape
url = 'https://www.google.com/search?q=site:twitter.com -site: algal blooms'


# alternative-1 (online parsing)
page = requests.get(url).text

# create an object to scrape various data later
soup = BeautifulSoup(page, 'html.parser')
print(soup)

"""
#2. PARSING HTML
#text 
result_tl = soup.select('article .VwiC3b.yXK7lf.yDYNvb.W814ac.lyLwlc.lEBKkf')
text = [t.text for t in result_tl]
print(text)

#date-time
#result_dt = soup.select('[datetime]')
result_dt = soup.select('article .r0bn4c.rQMQod')
timedate = [d['datetime'] for d in result_dt]
print(timedate)

#source
result_src = soup.select('article .LC20lb.MBeuO.DKV0MD')
source = [s.text for s in result_src]
print(source)
#3. PARSING RELATIVE URL INTO ABSOLUTE URL
link = []
# let's turn all relative-url into absolute-url by iterating all links
#base_url = 'https://news.google.com/'
#for i in soup.select('article .yuRUbf'):
for g in soup.find_all('div', {'class':'g'}):
	if anchors:
		link = anchors[0]['href'] 
    #ss = urljoin(base_url, i.get('href'))
    # put all absolute links into empty list
 		#links.append(ss)
print(link)
#4. DATAFRAME TO CSV
# putting all of data into a list
all_data = list(zip(source, text, timedate, link))

# convert the list into dataframe
df = pd.DataFrame(all_data, columns=['source', 'text', 'timedate', 'link'])
print(df)
"""
