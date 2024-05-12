import feedparser
import pandas as pd 
from datetime import datetime
#import time
from dateutil import parser
import requests
from bs4 import BeautifulSoup
import bs4
import time

feed = ''

titles = []
links = []
timestamp = []
link = []
texts = [] 


def scrape_google_news_feed(query):
    rss_url = f'https://news.google.com/rss/search?q={query}+after:2023-04-20+before:2024-04-20&ceid=US:en&hl=en-US&gl=US'
    feed = feedparser.parse(rss_url)
    if feed.entries:
            for entry in feed.entries:
                title = entry.title
                titles.append(title)
                #df = pd.DataFrame(data)
                link = entry.link
                #links.append(link)
                redirect_link = requests.get(link)
                links.append(redirect_link.url)
                response = requests.get(redirect_link.url,headers = {'User-Agent': 'Mozilla/5.0'})
               # proxies= {"http": 'http://167.99.124.118:8080',"https":'http://34.122.187.196:8080'})
                soup = bs4.BeautifulSoup(response.text, 'lxml')
                texts.append(soup.body.get_text(' ',strip=True))
                #link = pd.DataFrame(entry.link)
                #description = entry.description
                pubdate = entry.published
                pubdate = pubdate[5:]
                pubdate = pubdate[:20]
                date_format = '%d %b %Y %H:%M:%S'
                #date_obj = datetime.strptime(pubdate)
                date_obj = datetime.strptime(pubdate,date_format)
                date_string = date_obj.strftime(date_format) 
                #timestamp.append(parser)
                timestamp.append(date_string)
    else:
        print("Nothing Found!")
        #titles.append('')
        #links.append('')
        #timestamp.append('')
        #return titles, links, timestamp

def text1(links): 
    for link in links:
        page = requests.get(link)
        soup = bs4.BeautifulSoup(page.content,features="lxml")
        results = soup.findAll("p")
        texts.append(results)
        results2 = soup.findAll("h1")
        texts.append(results2)

if __name__ == "__main__":
    #queries = ["toxic+algae","cyanobacteria","algal+bloom","algae+bloom","blue-green+algae","red+tide"]
    #queries = ["toxic+algae"]
    #for query in range(len(queries)):
    #query = "cyanobacteria"
    results1 = scrape_google_news_feed("toxic+algae")
    time.sleep(40)
    results2 = scrape_google_news_feed("cyanobacteria")
    time.sleep(40)
    results3 = scrape_google_news_feed("algal+bloom")
    time.sleep(40)
    results4 = scrape_google_news_feed("algae+bloom")
    time.sleep(40)
    results5 = scrape_google_news_feed("blue-green+algae")
    time.sleep(40)
    results6 = scrape_google_news_feed("red+tide")
    time.sleep(40)
    for link in range(len(links)):
        print(links[link])
        print(titles[link])
        print(texts[link])
        print(timestamp[link])
        print(links[link])
        #time.sleep(40)
    """
    dict = {'links': links, 'titles': titles, 'texts': texts, 'timestamp':timestamp}
    df = pd.DataFrame(dict)
    df.to_csv('googlenews2.csv')
    """
    #time.sleep(40)