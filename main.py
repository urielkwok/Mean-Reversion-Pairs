import data_loader as dl

START_DATE, END_DATE = dl.get_dates()
STOCK_1 = "KO"
STOCK_2 = "PEP"

stock_df = dl.get_data(STOCK_1, STOCK_2, START_DATE, END_DATE)
print(stock_df)
