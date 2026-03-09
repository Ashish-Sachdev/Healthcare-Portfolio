import pandas as pd

df = pd.read_excel(r"D:\Healthcare Analytics Portfolio\Level-2\Data\BC Surgical Wait Times\2009_2025-annual-surgical_wait_times.xlsx")

df.to_csv(r"D:\Healthcare Analytics Portfolio\Level-2\Data\BC Surgical Wait Times\surgical_wait_times.csv", index=False)

print("File converted successfully!")