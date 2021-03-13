# Winter Hardcastle, 03/12/2021
# This script pulls data from a robinhood portfolio, and returns whether each stock in the portfolio is up/down for the day.


import robin_stocks.robinhood as rs  # pip3 install robin_stocks
import yfinance as yf  # pip3 install yfinance
from datetime import datetime
import pandas as ps

# robin_stocks login, will throw MFA request if relevant.
# use your robinhood username/password here
login = rs.login("username", "password")

# Price at market open today for each ticker
open_price_dict = {}

# Current Price of each ticker, pulled off of robin_stocks
rs_price_dict = {}

# Creates stock list. RUN THIS FIRST
def tickers():

    my_tickers_list = []
    my_stocks = rs.build_holdings()
    for key, value in my_stocks.items():
        my_tickers_list.append(key)
    print(my_tickers_list, "\n")

    return my_tickers_list
    # List of stocks in portfolio


# Creates market open dictionary
def open_price(tick):
    stock = yf.Ticker(tick)
    stock_history = stock.history(period="1d", interval="1d")
    for x in stock_history.Open:
        price_at_open = x
    open_price_dict.update({tick: float(price_at_open)})
    print(price_at_open, "\n")
    return


# Creates current prices dictionary.
def rs_current_price(tick):

    my_stocks = rs.build_holdings()
    value = my_stocks[tick]
    rs_price_dict.update({tick: float(value["price"])})
    print(value["price"], "\n")

    return


# For each stock, outputs either "up" or "down"
def red_or_green(tick):
    rs_current_price(tick)
    open_price(tick)
    open_price_val = open_price_dict[tick]
    open_price_dict.update({tick: float(open_price_val)})

    if float(open_price_dict[tick]) <= float(rs_price_dict[tick]):
        return "up"
    if float(open_price_dict[tick]) > float(rs_price_dict[tick]):
        return "down"
