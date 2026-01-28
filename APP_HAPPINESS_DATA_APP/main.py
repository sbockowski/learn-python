import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("happy.csv")

st.title("In Search for Happiness")

option_x = st.selectbox("Select data to view for the X-axis", ("GDP", "Happiness", "Generosity"))
option_y = st.selectbox("Select data to view for the Y-axis", ("GDP", "Happiness", "Generosity"))
st.subheader(f"{option_x} and {option_y}")

figure = px.scatter(x=df[option_x.lower()], y=df[option_y.lower()], labels={"x": option_x, "y": option_y})
st.plotly_chart(figure)
