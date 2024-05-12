import requests
from bs4 import BeautifulSoup
import pandas as pd 
import urllib.parse
links = [] 
#queries = ["site:instagram.com+toxic+algae","site:instagram.com+cyanobacteria","site:instagram.com+algal+bloom","site:instagram.com+algae+bloom","site:instagram.com+blue-green+algae","site:instagram.com+red+tide"]
#def instagram_query(query):
    #print(message)
    #params = {'q': query}
    #safe = urllib.parse.quote_plus(query)
url = 'https://www.google.com/search?q={"site:instagram.com+cyanobacteria"}+after:2023-04-20+before:2024-04-20&ceid=US:en&hl=en-US&gl=US'

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
data = requests.get(url, headers=header)
#print(data)

#links = [] 
if data.status_code == 200:
    soup = BeautifulSoup(data.content, "html.parser")
    results = []
    for g in soup.find_all('div',  {'class':'g'}):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            links.append(link)
                #title = g.find('h3').text
                #try:
                #    description = g.find('div', {'data-sncf':'2'}).text
                #except Exception as e:
                #    description = "-"
                #results.append(str(title)+";"+str(link)+';'+str(description))

#queries = ["site:instagram.com+toxic+algae","site:instagram.com+cyanobacteria","site:instagram.com+algal+bloom","site:instagram.com+algae+bloom","site:instagram.com+blue-green+algae","site:instagram.com+red+tide"]
#for query in queries:
#instagram_query('site:instagram.com+toxic+algae')
print(links)
df = pd.DataFrame(links)
df.to_csv('instagram1.csv')
"""
with open("serp1.csv", "w") as f:
    f.write("Title; Link; Description\n")

for result in results:
    with open("serp1.csv", "a", encoding="utf-8") as f:
        f.write(str(result)+"\n")
"""