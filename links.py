import requests
import pandas as pd 
from urllib.parse import urlencode
df = pd.read_csv('instagram.csv',index_col=0)
#df1 = pd.read_csv('googlenews2.csv.csv',index_col=0)
redirect_links = []
for link in range(len(df)):
    redirect_link= str(df.iloc[link][0])
    print(redirect_link)
    link1 = urlencode(redirect_link)
    #url = urlretrieve(redirect_link)
    #print(url)
    #webbrowser.open(url)
    print(link1)
    #response = requests.get(url1,headers = {'User-Agent': 'Mozilla/5.0'})
    #redirect_links.append(response)
#print(redirect_links)