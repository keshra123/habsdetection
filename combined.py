import pandas as pd
import requests
import bs4
from bs4 import BeautifulSoup
from time import sleep
import random
import concurrent.futures
links = []
df1 = pd.read_csv('googlenews.csv',index_col=0)
df1 = df1.head(30)
#num = 0

num = 0
for link in range(len(df1['links'])):
    #redirect_link = requests.get(df1['links'][link],timeout=60)
    sleep(random.randint(15, 30))
    s = requests.Session()
    redirect_link = s.get(df1['links'][link],timeout=60)
    #df1['links'][link] = redirect_link.url
    #print(redirect_link.url)
    
    if redirect_link.status_code == requests.codes.ok:
        df1['links'][link] = redirect_link.url
        soup = bs4.BeautifulSoup(redirect_link.text, 'lxml')
        df1['texts'][link] = soup.body.get_text(' ',strip=True)
    #else: 
    #    raise Exception("Something broke it")
    num +=1 
    if num == 10: 
        sleep(60)
        num = 0
    print(link)
df1['source type'] = "google"
df2 = pd.read_csv('reddit.csv',index_col=0)
df2['source type'] = "reddit"
df = pd.read_csv('instagram.csv',index_col=0)
#print(df)
for link in range(len(df['links'])):
    redirect_link = requests.get(df['links'][link])
    df['links'][link] = redirect_link.url
    #print(redirect_link.url)
#print(df['links'])
#df.to_csv('list.csv')
df['source type'] = "instagram"
frames = [df1,df2,df]
#frames = [df1,df2]
results = pd.concat(frames)
#results.drop()
results.reset_index(inplace=True, drop=True)
#results.drop(['index'], axis=1)
results.to_csv('combined.csv')
print(results)