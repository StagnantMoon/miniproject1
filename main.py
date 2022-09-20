# INF601 - Advanced Programming in Python
# Alex (Daniele) Basden
# Mini Project 1

import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info


# get historical market data
data = yf.download("MSFT", start="2022-09-02", end="2022-09-19")

msftPrices = []

for price in data ['Adj Close']:
    msftPrices.append(price)

print(msftPrices)



