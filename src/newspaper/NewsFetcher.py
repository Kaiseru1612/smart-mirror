import requests
class NewsFetcher:
    url = "https://newsapi.org/v1/articles"
    apiKey = ""
    def __init__(self, apiKey):
        self.apiKey = apiKey
    def FetchFromBBC(self):
        query_params = {
            "source": "bbc-news",
            "sort-by": "top",
            "apiKey": self.apiKey
        }
        res = requests.get(self.url, params=query_params)
        open_bbc_page = res.json()
        article = open_bbc_page["articles"]
        results = []    
        for ar in article:
            results.append(ar["title"])      
        return results

# news = NewsFetcher("523505cd243b45d599b136431677a833")
# print(news.FetchFromBBC())