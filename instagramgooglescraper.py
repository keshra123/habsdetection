import feedparser
import pandas as pd
import time
from datetime import datetime
import sys
titles = []
links = []
timestamp = []
texts = [] 
instagram = False

def scrape_google_news_feed(self,instagram):
    #rss_url = f'https://news.google.com/rss/search?q={query1}+after:2023-06-11+before:2024-06-11&hl=en-US&gl=US&ceid=US:en'
    rss_url = f'https://news.google.com/rss/search?q={query1}&tbs=qdr:y&hl=en-US&gl=US&ceid=US:en'
    feed = feedparser.parse(rss_url)
    if feed.entries:
        for entry in feed.entries:
            if(instagram == False or entry.source.title !='Instagram' or "Instagram photos and videos" not in entry.title):
                title = entry.title
                titles.append(title)
                link = entry.link
                #link = link.replace('rss/', '')
                links.append(link)
                description = entry.description
                texts.append(description)
                pubdate = entry.published
                pubdate = pubdate[5:]
                pubdate = pubdate[:20]
                date_format = '%d %b %Y %H:%M:%S'
                date_obj = datetime.strptime(pubdate,date_format)
                date_string = date_obj.strftime(date_format) 
                timestamp.append(date_string)
                source = entry.source


if __name__ == "__main__":
    queries = ["site:instagram.com+toxic+algae"]
    for i in range(len(queries)):
        query1 = queries[i]
        if("instagram" in query1):
            instagram = True
        results1 = scrape_google_news_feed(query1,instagram)
        dict = {'links': links, 'titles': titles, 'texts': texts, 'timestamp':timestamp}
        df = pd.DataFrame(dict)
        df.to_csv('googlenews2.csv')
