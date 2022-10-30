import requests

url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=4f8b83aec5a847eb9fbd29815900104f')
response = requests.get(url)

print(response.json())



# import pandas as pd
# apikey = '4f8b83aec5a847eb9fbd29815900104f'

# #instantiate an article object
# from newsapi.articles import Articles
# a = Articles(API_KEY=apikey)
# data = a.get(source="bbc-news", sort_by='top')
# data = pd.DataFrame.from_dict(data)
# data = pd.concat([data.drop(['articles'], axis=1), data['articles'].apply(pd.Series)], axis=1)
# data.head()