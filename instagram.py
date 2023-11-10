import pandas as pd
import praw

reddit = praw.Reddit(
client_id = "qnWzLjlO2zONMJ5JnOptxQ",
client_secret="OcKFWXcyCP4PeSkQA46EWapZP5eQiA",
user_agent = "Test App by u/keshra123",
user_name="keshra123",
)

print(reddit.auth.authorize(code))
print(reddit.user.me())
