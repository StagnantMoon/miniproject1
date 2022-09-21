# INF601 - Advanced Programming in Python
# Alex (Daniele) Basden
# Mini Project 1

import yfinance as yf
import numpy as np
# import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("QtAgg")

# get stock info
# MSFT = Microsoft
# NVDA = Nvidia Corporation
# AMD = Advanced Micro Devices
# INTC = Intel Corporation
# TSM = Taiwan Semiconductor Manufacturing Company
# AAPL = Apple

msft = yf.Ticker("MSFT")
amd = yf.Ticker("AMD")
intc = yf.Ticker("INTC")
nvda = yf.Ticker("NVDA")
tsm = yf.Ticker("TSM")
aapl = yf.Ticker("AAPL")

# get historical market data
msftData = yf.download("MSFT", start="2022-09-01", end="2022-09-19")
amdData = yf.download("AMD", start="2022-09-01", end="2022-09-19")
intcData = yf.download("INTC", start="2022-09-01", end="2022-09-19")
nvdaData = yf.download("NVDA", start="2022-09-01", end="2022-09-19")
tsmData = yf.download("TSM", start="2022-09-01", end="2022-09-19")
aaplData = yf.download("AAPL", start="2022-09-01", end="2022-09-19")

#Arrays to hold the yahoo finance data
msftPrices = []
amdPrices = []
intcPrices = []
nvdaPrices = []
tsmPrices = []
aaplPrices =[]

for price in msftData['Adj Close']:
    msftPrices.append(price)

for price in amdData['Adj Close']:
    amdPrices.append(price)

for price in intcData['Adj Close']:
    intcPrices.append(price)

for price in nvdaData['Adj Close']:
    nvdaPrices.append(price)

for price in tsmData['Adj Close']:
    tsmPrices.append(price)

for price in aaplData['Adj Close']:
    aaplPrices.append(price)

# Create a NumPy Array and print stock price at end of day
msftArray = list(np.around(np.array(msftPrices), 2))
print(msftArray)
amdArray = list(np.around(np.array(amdPrices), 2))
print(amdArray)
intcArray = list(np.around(np.array(intcPrices), 2))
print(intcArray)
nvdaArray = list(np.around(np.array(nvdaPrices), 2))
print(nvdaArray)
tsmArray = list(np.around(np.array(tsmPrices), 2))
print(tsmArray)
aaplArray = list(np.around(np.array(aaplPrices), 2))
print(aaplArray)

# Create matplotlib graph
from matplotlib import pyplot as plt
plt.style.use('dark_background')

plt.plot(msftArray, color='c', label='MSFT')
plt.plot(amdArray, color='r', label='AMD')
plt.plot(intcArray, color='b', label="Intel")
plt.plot(nvdaArray, color='g', label="Nvidia")
plt.plot(tsmArray, color='m', label="TSM")
plt.plot(aaplArray, color='w', label="AAPL")

plt.xlabel("Days Stock Market Open")
plt.ylabel("Share Price")
plt.title("Share Price from 01.09.2022 to 19.09.2022")
plt.xlim(1, 10)
plt.ylim(bottom=0, top=300)

plt.legend()


# show the graph

plt.savefig('charts/SharePriceForTechStocks.png')
# show the graph
plt.show()

