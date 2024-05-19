#!/bin/bash
# A simple variable example
#python reddit.py
python googlescraper.py 
python instagramscraper.py 
echo 'Instagram Completed'
python googlescraper.py 
echo 'Google News Completed'
python reddit.py
echo 'Reddit Completed'
#python links.py
python combined.py
echo 'Final File is Completed'