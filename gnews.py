# Import the beautifulsoup
# and request libraries of python.
import requests
import bs4
import feedparser
import urllib.request
from urllib.parse import urljoin
import os
import webbrowser

# Make two strings with default google search URL
# 'https://google.com/search?q=' and
# our customized search keyword.
# Concatenate them
text= "algal blooms"
url = 'https://news.google.com/search?q=' + text

# Fetch the URL data using requests.get(url),
# store it in a variable, request_result.
request_result=requests.get( url )
#print(request_result.content)
#content = request_result.text



# Creating soup from the fetched request
soup = bs4.BeautifulSoup(request_result.text,
                        "html.parser")
#print(soup)

def title():
    result_tl = soup.select('article .DY5T1d.RZIKme')
    title = [t.text for t in result_tl]
    print(title)
    print(len(title))

def datetime():
    result_dt = soup.select('[datetime]')
    timedate = [d['datetime'] for d in result_dt]
    print(timedate)
    print(len(timedate))

def links():
    links = []
    base_url = 'https://news.google.com/'
    for i in soup.select('article .DY5T1d.RZIKme'):
        ss = urljoin(base_url, i.get('href'))
    # put all absolute links into empty list
        links.append(ss)
    #for x in range(6):
    #    webbrowser.open(links[x])
    #print(weburl)
    print(links)

title()
datetime()
links()


#join = []
#for link in soup.find_all('a', href=True):
#    if "./articles" in link['href']:
#        news = url + link['href']
#        join.append(news)
#print(join)


#print(link['href'])
#soup = bs4(request_result.content, 'lxml')
#listings = [i['href'] for i in soup.select('.hz-pro-search-result__name-rating > a:first-child')]

#soup.find.all( h3 ) to grab
# all major headings of our search result,
#heading_object=soup.find_all( '<p>' )
#links = soup.select(".dsbr a")

#heading_object1=soup.find_all('./articles/')
#print

# Iterate through the object
# and print it as a string.
#for info in heading_object:
#    print(info.getText())
#    print("-----")
#print ("Part 2")
#for l in links:
#    print(l.get("href"))

