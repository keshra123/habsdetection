#This will not run on online IDE 
import requests 
import csv
from bs4 import BeautifulSoup 
import pandas as pd

df = pd.read_csv('file1.csv')
print(df) 
df1 = df ['links']
print(df1)
data = []
for link in df1: 
    #print(link)
    r = requests.get(link) 

    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
    #print(soup)
    table = soup.findAll('p')
    data = table 
    #print(table)  
pd.DataFrame(data).to_csv('file2.csv') 

#URL = "https://bladenonline.com/public-advised-to-avoid-algal-bloom-near-bay-tree-lake/"
#r = requests.get(URL) 

#soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
#print(soup)
#table = soup.findAll('p')
#print(table)  
