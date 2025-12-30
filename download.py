import requests
import pandas as pd
from dotenv import load_dotenv
import os
import time

load_dotenv()

api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
base_url = "https://www.alphavantage.co/query"

companies = ["IBM", "AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "NVDA", "CSCO", "INTC"]

for company in companies:
    url = f'{base_url}?function=TIME_SERIES_WEEKLY&symbol={company}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()

    if 'Weekly Time Series' not in data:
        print(f"Error fetching data for {company}: {data.get('Error Message', 'Unknown error')}")
        print(f"Full response: {data}")  
        continue  

    dates = []
    open_prices = []
    high_prices = []
    low_prices = []
    close_prices = []
    volumes = []

    for date, values in data['Weekly Time Series'].items():
        dates.append(date)
        open_prices.append(float(values['1. open']))
        high_prices.append(float(values['2. high']))
        low_prices.append(float(values['3. low']))
        close_prices.append(float(values['4. close']))
        volumes.append(int(values['5. volume']))

    df = pd.DataFrame({
        'Date': dates,
        'Open': open_prices,
        'High': high_prices,
        'Low': low_prices,
        'Close': close_prices,
        'Volume': volumes
    })

    df.to_csv(f'{company}_weekly_data.csv', index=False)

    time.sleep(12) 