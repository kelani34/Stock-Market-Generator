import streamlit as st
import yfinance as yf
st.write(
"""
# A simple stock price app

### Below are shown **closing stock price** and the **volume** of **google**

"""
)

ticker_symbol = "AAPL"

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1d", start="2010-5-31", end="2020-5-31")
st.write("""
## Closing price
""")
st.line_chart(ticker_df.Close)
st.write("""
## Volume price
""")
st.line_chart(ticker_df.Volume)
