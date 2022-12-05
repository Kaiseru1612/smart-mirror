import json
from turtle import title
import requests
import pandas as pd

url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=4f8b83aec5a847eb9fbd29815900104f')
response = requests.get(url)

# print(response.json())
articles={}
articles=response.json()
# print(type(article))
# article=json.loads(response.json())
# print(article[title])
# for article in articles:
#     print (article)
#     for y in articles[article]:
#         print (y,':',article[article][y])
print(json.dumps(articles, indent=4))

# import pandas as pd
# apikey = '4f8b83aec5a847eb9fbd29815900104f'

# #instantiate an article object
# from newsapi.articles import Articles
# a = Articles(API_KEY=apikey)
# data = a.get(source="bbc-news", sort_by='top')
# data = pd.DataFrame.from_dict(data)
# data = pd.concat([data.drop(['articles'], axis=1), data['articles'].apply(pd.Series)], axis=1)
# data.head()