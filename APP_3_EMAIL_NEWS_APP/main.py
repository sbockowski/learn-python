import requests
from send_email import send_email

api_key = "0a54312f6f634acd9c153f8b6df338e8"

topic = "tesla"

url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2025-12-23&" \
      "sortBy=publishedAt&" \
      "apiKey=0a54312f6f634acd9c153f8b6df338e8&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body = "Subject: Today's news" \
        + body + article["title"] + "\n" \
        + article["description"] + "\n" \
        + article["url"] + 2*"\n"

body = body.encode("utf-8")
print(body)
# send_email(message=body)

