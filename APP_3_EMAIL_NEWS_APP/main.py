import requests

api_key = "0a54312f6f634acd9c153f8b6df338e8"

url = "https://newsapi.org/v2/everything?q=tesla&"\
      "from=2025-12-23&sortBy=publishedAt&apiKey="\
      "0a54312f6f634acd9c153f8b6df338e8"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])