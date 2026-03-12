import pandas as pd
import statsmodels.tsa.stattools as sm


def OLS_regression(ind_stock: pd.Series, dep_stock: pd.Series) -> tuple[float, float]:
    """
    Requires: Nothing
    Modifies: Nothing
    Effects: Alpha and Beta values for the two variables
    """
    x = sm.add_constant(ind_stock)
    y = dep_stock
    regression = sm.OLS(y, x).fit()
    alpha = regression.params.iloc[0]
    beta = regression.params.iloc[1]
    return alpha, beta


def adf_test(stock_1: pd.Series, stock_2: pd.Series) -> bool:
    """
    Requires: Nothing
    Modifies: Nothing
    Effects: True if series is stationary, False otherwise
    """
    alpha, beta = OLS_regression(stock_1, stock_2)
    spread = stock_1 - (alpha + beta * stock_2)
    result = sm.adfuller(spread)
    print(f"Raw ADF: {result[0]:.4f}, p-value: {result[1]:.4f}")
    if result[1] < 0.1:
        return True
    else:
        return False


def rolling_OLS(stock_1: pd.Series, stock_2: pd.Series, window) -> pd.Series:
    """
    Requires: Both series contain rolling stock data
    Modifies: Nothing
    Effects: Calculates a rolling beta
    """
    
    return rolling_beta


def rolling_z_score(series: pd.Series, window: int) -> pd.Series:
    """
    Requires: Nothing
    Modifies: Nothing
    Effects: Rolling z-score for each entry
    """
    rolling_mean = series.rolling(window).mean()
    rolling_std = series.rolling(window).std()
    return (series - rolling_mean) / rolling_std
