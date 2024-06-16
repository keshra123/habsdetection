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
#queries = ["toxic+algae","cyanobacteria","algal+bloom","algae bloom","blue-green+algae","red+tide"]
queries = ["blue-green+algae"]
for query in queries:
	for post in reddit.subreddit("all").search(query=query,time_filter="year"):
		titles.append(post.title)
		posts.append(post.selftext)
		tz = pytz.timezone('America/New_York')
		timestamp.append(datetime.fromtimestamp(post.created_utc).replace(tzinfo=tz).strftime("%d %b %Y %H:%M:%S"))
		links.append(post.url)
	#print(titles)
	#print(links)
	#print(posts)
	#print(timestamp)
	dict = {'links': links, 'titles': titles, 'texts': posts, 'timestamp':timestamp}
	df = pd.DataFrame(dict)
	df.to_csv('reddit.csv')
#print("Reddit Completed")

