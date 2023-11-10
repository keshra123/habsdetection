import pandas as pd
import praw

reddit = praw.Reddit(
client_id = "qnWzLjlO2zONMJ5JnOptxQ",
client_secret="OcKFWXcyCP4PeSkQA46EWapZP5eQiA",
user_agent = "Test App by u/keshra123",
user_name="keshra123",
)

posts = []
#headlines = set ()
for post in reddit.subreddit('all').search("harmful algal blooms"):
	#headlines.add()	
	#print(post.title)
	#print(post.id)
	#print(post.author)
	print(post.created)
	posts.append(post.url)
headlines = pd.DataFrame(posts)
print(headlines)
#print(reddit.auth.authorize(code))
#print(reddit.user.me())
