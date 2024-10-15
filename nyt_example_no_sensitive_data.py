import requests
from urllib.parse import quote_plus

# app URL example
# https://developer.nytimes.com/my-apps/address

API_KEY = "your key here"
ARTICLE_SEARCH_BASE = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"
#q=portugal&api-key=your_key_here"

def build_query(
    p_exp:str,
    p_key:str=API_KEY
):
    p_exp = quote_plus(p_exp)
    ret: str = f"{ARTICLE_SEARCH_BASE}q={p_exp}&begin_date=20240101&api-key={p_key}"
    # e.g.
    # https://api.nytimes.com/svc/search/v2/articlesearch.json?q=Portugal&begin_date=20240101&api-key=your_key_here

    # ret:str = f"{ARTICLE_SEARCH_BASE}q={p_exp}&api-key={p_key}"
    return ret
# def build_query

q=build_query(
    p_exp="Portugal"
)
print(q)

# Make the API call
response = requests.get(q)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # data is a Python dictionary
    # articles are the 'docs' in 'response'
    articles = data['response']['docs']

    # each article as a 'main' 'headline'
    for article in articles:
        print(article['headline']['main'])
else:
    print(f"Error: {response.status_code}")
