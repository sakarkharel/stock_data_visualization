# Stock Market Data Visualization

## Description:
This project fetches weekly stock market data for major IT companies and visualizes key metrics such as **stock price trends**, **trading volume**, and **comparative analysis** across multiple companies. The goal is to provide insightful visualizations that help analyze stock performance over time using various chart types, including line charts, bar charts, and candlestick charts.

## Project Features:
- **Data Fetching**: Uses the AlphaVantage API to fetch weekly stock data for 10 major IT companies (e.g., IBM, AAPL, MSFT, etc.).
- **Data Preprocessing**: Organizes and cleans stock data into a structured format for easy analysis.
- **Data Visualization**: Includes:
  - **Line charts** for stock price trends.
  - **Bar charts** for weekly trading volume.
  - **Candlestick charts** for detailed price movement.
  - **Comparative stock price trends** across all companies.
- **Interactive Visuals**: Provides insights into the relationship between **stock price**, **volume**, and **other metrics**.

## Libraries Used:
- `requests` for fetching data from the AlphaVantage API.
- `pandas` for data manipulation and processing.
- `matplotlib` and `seaborn` for static visualizations.
- `plotly` for interactive charts, including candlestick and comparative stock trend visualizations.

## Use Cases:
- **Stock Performance Analysis**: Track the weekly price trends and trading volumes for major IT companies.
- **Comparative Stock Analysis**: Compare the performance of different stocks over time.
- **Investor Insights**: Gain insights into how stocks fluctuate week-to-week and identify patterns in price movements.

## Getting Started:
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    ```
2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up your **AlphaVantage API key** and place it in a `.env` file.
4. Run the script or open the Jupyter notebook to view the visualizations.

