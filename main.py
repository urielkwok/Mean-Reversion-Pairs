import src.data_loader as dl
import src.analysis as an
import src.visualizer as vz
import src.backtester as bt

START_DATE, END_DATE = dl.get_dates()
STOCK_1 = "DASH"
STOCK_2 = "GRAB"
WINDOW = 30

df = dl.get_data(STOCK_1, STOCK_2, START_DATE, END_DATE)
rolling_beta = an.rolling_beta(df, STOCK_1, STOCK_2, WINDOW)
df["spread"] = df[STOCK_2] - (rolling_beta * df[STOCK_1])
stationary = an.adf_test(df[STOCK_1], df[STOCK_2])
if stationary is True:
    print("Spread is stationary")
    z_scores = an.rolling_z_score(df["spread"], WINDOW)
    df["z-score"] = z_scores
    bt.get_positions(df)
    investment_price = df[STOCK_2] + (rolling_beta * df[STOCK_1])
    df["cum_returns"] = bt.cum_returns(df["spread"], df["position"], investment_price, WINDOW)
    df["cum_SPY"] = bt.cum_returns(df["SPY"], df["spy_position"], df["SPY"], WINDOW)
    vz.plot_values(df)
    bt.get_measurements(df["cum_returns"], WINDOW)
else:
    print("Spread is not stationary.")
