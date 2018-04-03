#!/usr/bin/env python
#

# <bitbar.title>Realtime Stock Tracker</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Bogdan Mosincat</bitbar.author>
# <bitbar.author.github>bogdan1304</bitbar.author.github>
# <bitbar.desc>Shows realtime stock price and daily percentage change for each stock in the list.</bitbar.desc>
# <bitbar.image>https://i.imgur.com/hQoCXFL.png</bitbar.image>
# <bitbar.dependencies>python</bitbar.dependencies>

import json, urllib2

def get_stock_prices(stocks):
	response = urllib2.urlopen('https://api.iextrading.com/1.0/stock/market/batch?symbols=' + stocks +
		'&types=quote&displayPercent=true&filter=latestPrice,changePercent')
	return json.loads(response.read())

def create_output_string(stock):
	output = stock
	changePercent = response[stock]["quote"]["changePercent"]
 	output += " - $"
 	output += "{:0.2f}".format(response[stock]["quote"]["latestPrice"])
 	output += " (" + "{:0.2f}".format(changePercent) + "%)"

 	color = "red" if changePercent < 0 else "green"
 	output += " | color=" + color

	return output

stocks = ["SPY", "ATHM", "AMZN", "BZUN", "NOW", "CRM", "PAYC", "NFLX", "AAPL", "TSLA", "FB", "QTM", "GOOGL", "JCP"]
response = get_stock_prices( ",".join(stocks) )
print create_output_string(stocks[0]) # first item displays in the menubar
print '---'
for stock in stocks:
	print create_output_string(stock)
