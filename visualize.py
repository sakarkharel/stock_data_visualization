import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.graph_objects as go



def load_data(company):
    return pd.read_csv(f'{company}_weekly_data.csv')


companies = ["IBM", "AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "NVDA", "CSCO", "INTC"]

st.title("Stock Market Data Visualization")
st.sidebar.title("Select a Company")

company = st.sidebar.selectbox("Choose a company", companies)

df = load_data(company)

st.subheader(f"Weekly Data for {company}")
st.write(df.tail())  

st.subheader(f"{company} Close Price Trend")
st.line_chart(df.set_index('Date')['Close'])


# st.subheader(f"{company} Weekly Volume")
# fig, ax = plt.subplots()
# ax.bar(df['Date'], df['Volume'], color='orange')
# ax.set_xticklabels(df['Date'], rotation=90)
# ax.set_xlabel('Date')
# ax.set_ylabel('Volume')
# st.pyplot(fig)

st.subheader(f"{company} Candlestick Chart")
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    increasing_line_color='green',
    decreasing_line_color='red'
)])
fig.update_layout(title=f"{company} Stock Price (Candlestick)", xaxis_title="Date", yaxis_title="Price (USD)")
st.plotly_chart(fig)

st.subheader("Comparing Stock Price Trends for All Companies")
all_data = {}
for c in companies:
    df = load_data(c)
    all_data[c] = df.set_index('Date')['Close']

comparison_df = pd.DataFrame(all_data)
st.line_chart(comparison_df)

