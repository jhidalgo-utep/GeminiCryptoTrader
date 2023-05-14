# -*- coding: utf-8 -*-
"""
Created on Sun May 14 09:50:38 2023

@author: joaqu
"""

import requests
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, date2num
from datetime import datetime

# Set the API endpoint for Gemini exchange
url = 'https://api.gemini.com/v2/candles/btcusd/1hr'

# Make a request to the API and get the response as a JSON object
response = requests.get(url).json()

# Extract the data we need from the JSON response
candles = response[:-1]  # ignore the last incomplete candle
dates = [datetime.fromtimestamp(candle[0] / 1000) for candle in candles]
open_prices = [candle[1] for candle in candles]
high_prices = [candle[2] for candle in candles]
low_prices = [candle[3] for candle in candles]
close_prices = [candle[4] for candle in candles]

# Convert the dates to Matplotlib's internal format
dates = date2num(dates)

# Set up the figure and the axis
fig, ax = plt.subplots(figsize=(13, 5))

# fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M:%S'))

# Create the candlestick chart
candlestick_data = [tuple([dates[i], open_prices[i], high_prices[i], low_prices[i], close_prices[i]]) for i in range(len(dates))]
ax.plot([], [], ' ', label='Candlestick Chart')
ax.legend()
ax.set_title('BTC/USD Candlestick Chart')
ax.set_xlabel('Date')
ax.set_ylabel('Price (USD)')
candle_colors = {'up': 'green', 'down': 'red'}
for i in range(len(candlestick_data)):
    candle = candlestick_data[i]
    date = candle[0]
    open_price = candle[1]
    high_price = candle[2]
    low_price = candle[3]
    close_price = candle[4]
    candle_color = candle_colors['up'] if close_price >= open_price else candle_colors['down']
    ax.plot([date, date], [low_price, high_price], color=candle_color, linewidth=1)
    ax.plot([date, date], [open_price, close_price], color=candle_color, linewidth=4)

# Display the chart
plt.show()
