import data_loader as dl

stock_df = dl.get_data("KO", "PEP", "2024-01-01", "2026-01-01")
print(stock_df)