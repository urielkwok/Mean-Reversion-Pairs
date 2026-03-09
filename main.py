import src.data_loader as dl
import src.analysis as an
import src.visualizer as vz
import src.backtester as bt

START_DATE, END_DATE = dl.get_dates()
STOCK_1 = "GRAB"
STOCK_2 = "DASH"
ROLLING_WINDOW = 30

stock_df = dl.get_data(STOCK_1, STOCK_2, START_DATE, END_DATE)
alpha, beta = an.OLS_regression(stock_df[STOCK_1], stock_df[STOCK_2])
stock_df["spread"] = stock_df[STOCK_2] - (alpha + beta * stock_df[STOCK_1])
stationary = an.adf_test(stock_df["spread"])
if stationary is True:
    print("Spread is stationary")
    z_scores = an.rolling_z_score(stock_df["spread"], ROLLING_WINDOW)
    vz.plot_z_values(z_scores.dropna())
    stock_df["z-score"] = z_scores
    bt.get_positions(stock_df)
    stock_df["returns"] = bt.get_returns(stock_df["spread"], stock_df["position"])
    stock_df["spy_returns"] = bt.get_returns(stock_df["spy"], stock_df["spy_position"])
else:
    print("Spread is not stationary.")
