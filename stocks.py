import yfinance as yf

class Stock:    
    def __init__(self, symbol):
        self.symbol = symbol

    def fetch_stockdata(self, start_date, end_date):
        self.stock_data = yf.download(self.symbol, start=start_date, end=end_date)
        self.stock_data["Open"] = self.stock_data["Open"].round(2)  
        self.stock_data["Low"] = self.stock_data["Low"].round(2) 
        self.stock_data["Adj Close"] = self.stock_data["Adj Close"].round(2)  
        return self.stock_data
