from newsapi import NewsApiClient
import pandas as pd
newsapi = NewsApiClient(api_key='53be5151176c46fa9b69d0281dd74184')
all_articles = newsapi.get_everything(q='algal+blooms',
                                      from_param='2024-03-21',
                                      to='2024-04-21',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)

#print(all_articles.dtype)
dictionary = pd.DataFrame.from_dict(all_articles)
print(dictionary)
dictionary.to_csv('news2.csv')