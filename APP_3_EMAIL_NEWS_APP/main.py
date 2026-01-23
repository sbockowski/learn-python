import requests
from send_email import send_email

api_key = "0a54312f6f634acd9c153f8b6df338e8"

url = "https://newsapi.org/v2/everything?q=tesla&"\
      "from=2025-12-23&sortBy=publishedAt&apiKey="\
      "0a54312f6f634acd9c153f8b6df338e8"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
        
send_email(message=body)

