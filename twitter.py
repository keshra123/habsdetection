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
text= "site:twitter.com -site:m.twitter.com algal blooms"
url = 'https://google.com/search?q=' + text

# Fetch the URL data using requests.get(url),
# store it in a variable, request_result.
request_result=requests.get( url )
#content = request_result.text



# Creating soup from the fetched request
soup = bs4.BeautifulSoup(request_result.text,
                        "html.parser")
#print(soup)


def text():
    result_tl = soup.select('article VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc.lEBKkf')
    title = [t.text for t in result_tl]
    print(title)
    print(len(title))

def datetime():
    result_dt = soup.select('span')
    #print(result_dt)
    #print(len(result_dt))

def links():
    links = []
    base_url = url
    #base_url = 'https://www.google.com/'
    for i in soup.select('article .egMi0.KCrYT'):
        ss = urljoin(base_url, i.get('href'))
    # put all absolute links into empty list
        links.append(ss)
    #for x in range(6):
    #    webbrowser.open(links[x])
    #print(weburl)
    #println(links)
#text()
#datetime()
#links()

"""
#join = []
elements = soup.find_all('div', id=True)
for element in elements:    
    print(element)
"""

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

