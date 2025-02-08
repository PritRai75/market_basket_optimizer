import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class MarketBasketAnalyzer:
    def __init__(self):
        self.stock_data = {}
        self.correlation_matrix = None
    
    def fetch_stock_data(
        self,
        tickers: List[str],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        period: str = "1y"
    ) -> Dict[str, pd.DataFrame]:
        try:
            if start_date and end_date:
                for ticker in tickers:
                    stock = yf.Ticker(ticker)
                    self.stock_data[ticker] = stock.history(
                        start=start_date,
                        end=end_date
                    )
            else:
                for ticker in tickers:
                    stock = yf.Ticker(ticker)
                    self.stock_data[ticker] = stock.history(period=period)
            return self.stock_data
        except Exception as e:
            print(f"Error fetching stock data: {str(e)}")
            return {}

    def calculate_correlations(self) -> pd.DataFrame:
        try:
            closing_prices = pd.DataFrame()
            for ticker, data in self.stock_data.items():
                closing_prices[ticker] = data['Close']
            self.correlation_matrix = closing_prices.corr()
            return self.correlation_matrix
        except Exception as e:
            print(f"Error calculating correlations: {str(e)}")
            return pd.DataFrame()