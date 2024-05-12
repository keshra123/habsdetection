import random
from spacy.training import Example
import csv
import pandas as pd  
import spacy
     
nlp = spacy.load('en_core_web_sm')
docs = [] 
# making data frame  
df = pd.read_csv('reddit.csv')
print(df)
list = df['texts'][0]
print(list)
for i in range(0,len(df)):
    doc = nlp(str(df['texts'][i]))
    docs = [docs, doc]
for j in range(len(docs)):
    for entity in docs[j].ents:
        print(entity.text, entity.label_)
