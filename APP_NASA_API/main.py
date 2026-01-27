import requests
import streamlit as st

st.title("NASA Picture of the day")

url = "https://api.nasa.gov/planetary/apod?" \
      "api_key=KEY&" \
      "date"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# print(content["url"])

st.image(content["url"])
st.caption(f"Date: {content["date"]}, Copyright: {content["copyright"]}")
st.write(content["explanation"])


