import numpy as np
import statsmodels.tsa.stattools as sm


def adf_test(series: np.NDArray) -> bool:
    """
    Requires: Nothing
    Modifies: Nothing
    Returns: True if series is stationary, False otherwise
    """
    result = sm.adfuller(series)
    print(f"Raw ADF: {result[0]:.4f}, p-value: {result[1]:.4f}")
    if result[1] < 0.05:
        return True
    else:
        return False
 

def OLS_regression(ind_stock: np.NDArray, dep_stock: np.NDArray) -> tuple[float, float]:
    """
    Requires: Nothing
    Modifies: Nothing
    Returns: Alpha and Beta values for the two variables
    """
    x = sm.add_constant(ind_stock)
    y = dep_stock
    regression = sm.OLS(x, y).fit()
    alpha = regression.params[0]
    beta = regression.params[1]
    return alpha, beta


def z_score(series: np.ndarray) -> np.NDArray[np.float64]:
    """
    Requires; Nothing
    Modifies: Nothing
    Returns: z-score for each entry in the series
    """
    return (series - np.mean(series)) / np.std(series)
