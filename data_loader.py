import yfinance as yf
import pandas as pd


def get_data(stock_1: str, stock_2: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Requires: Valid tickers, dates formatted as 'YYYY-MM-DD'.
    Modifies: Nothing
    Effects: Returns a DataFrame containing price data.
    """
    stock_df = yf.download([stock_1, stock_2, "SPY"], start_date, end_date)

    return stock_df
