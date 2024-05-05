import yfinance as yf

def fetchData(node, ticker_symbol="amc", days=100):
    stock_data = yf.download(ticker_symbol, period=f"{days}d")
    adj_close_prices = stock_data['Adj Close']
    return adj_close_prices