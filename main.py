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

msft = yf.Ticker("MSFT")
amd = yf.Ticker("AMD")
intc = yf.Ticker("INTC")
nvda = yf.Ticker("NVDA")
tsm = yf.Ticker("TSM")

# get historical market data
msftData = yf.download("MSFT", start="2022-09-02", end="2022-09-19")
amdData = yf.download("AMD", start="2022-09-02", end="2022-09-19")
intcData = yf.download("INTC", start="2022-09-02", end="2022-09-19")
nvdaData = yf.download("NVDA", start="2022-09-02", end="2022-09-19")
tsmData = yf.download("TSM", start="2022-09-02", end="2022-09-19")


msftPrices = []
amdPrices = []
intcPrices = []
nvdaPrices = []
tsmPrices = []

for price in msftData ['Adj Close']:
    msftPrices.append(price)

for price in amdData ['Adj Close']:
    amdPrices.append(price)

for price in intcData ['Adj Close']:
    intcPrices.append(price)

for price in nvdaData ['Adj Close']:
    nvdaPrices.append(price)

for price in tsmData ['Adj Close']:
    tsmPrices.append(price)

print(msftPrices)
print(amdPrices)
print(intcPrices)
print(nvdaPrices)
print(tsmPrices)

# Create a NumPy Array
msftArray = np.array(msftPrices)
amdArray = np.array(amdPrices)
intcArray = np.array(intcPrices)
nvdaArray = np.array(nvdaPrices)
tsmArray = np.array(tsmPrices)

# Create matplotlib graph
from matplotlib import pyplot as plt

plt.plot(msftArray, color='c', label='MSFT')
plt.plot(amdArray, color='r', label='AMD')
plt.plot(intcArray, color='b', label="Intel")
plt.plot(nvdaArray, color='g', label="Nvidia")
plt.plot(tsmArray, color='m', label="TSM")

plt.xlabel("Days")
plt.ylabel("Share Price")
plt.title("Share Price from 02.09.2022 to 19.09.2022")

plt.legend()

#plt.plot(msftArray)
#plt.plot(amdArray)
# show the graph

#plt.savefig('charts/msft.png')

plt.show()

