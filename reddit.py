import pandas as pd
import praw
import csv
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pytz

reddit = praw.Reddit(
client_id = "qnWzLjlO2zONMJ5JnOptxQ",
client_secret="OcKFWXcyCP4PeSkQA46EWapZP5eQiA",
user_agent = "Test App by u/keshra123",
user_name="keshra123",
)

posts = []
titles = []
links = []
timestamp = []
link = []
queries = ["toxic+algae","cyanobacteria","algal+bloom","algae bloom","blue-green+algae","red+tide"]
for query in queries:
	for post in reddit.subreddit("all").search(query=query,sort="new"):
		titles.append(post.title)
		posts.append(post.selftext)
		tz = pytz.timezone('America/New_York')
		timestamp.append(datetime.fromtimestamp(post.created_utc).replace(tzinfo=tz).strftime("%d %b %Y %H:%M:%S"))
		links.append(post.url)
	print(titles)
	print(links)
	print(posts)
	print(timestamp)
	dict = {'links': links, 'titles': titles, 'texts': posts, 'timestamp':timestamp}
	df = pd.DataFrame(dict)
	df.to_csv('reddit.csv')



"""
#or 'tank' or 'farm'
links = []
checks = ['Aquariums','tank','farm']
for i in range(100):
	for check in range(len(checks)): 
		if checks[check] in headlines[0][i]: 
			headlines = headlines.pop(headlines[i])
			#if 'https://www.reddit.com/r/Aquariums'in headlines[0][i]: 
			#continue
		else:
			continue
links.append(headlines[0][i])
#print(links)
print(len(links))
"""
"""
results1 = []
for link in range(len(links)):
	page = requests.get(links[link])
	soup = BeautifulSoup(page.content,features="lxml")
	#soup = BeautifulSoup(open(links[links], 'r'),"html.parser",from_encoding="iso-8859-1")
	#soup = BeautifulSoup(page.content, "html.parser").decode(encoding="iso-8859-1")
	if 'reddit' in links[link]:
		results = soup.findAll("p")
		results2 = soup.findAll("h1")
		results1 =[results1, results]
		results1 =[results1, results2]
	else:
		results = soup.findAll("p")
		results = soup.findAll("title")
df = pd.DataFrame(links)
df.to_csv('file.csv')


print(results1)
"""
