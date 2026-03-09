# import pandas as pd

# xlsx = pd.ExcelFile(r'D:\Healthcare Analytics Portfolio\Level-2\Data\CIHI Wait Times Priority Procedures\CIHI_wait_times.xlsx')

# # Print all sheet names first so you know what's available
# print(xlsx.sheet_names)

# # Then convert just the one you want
# df = xlsx.parse('Table 1')
# df.to_csv('output.csv', index=False)

# print("Done!")



import pandas as pd
import os

xlsx_file = r'D:\Healthcare Analytics Portfolio\Level-2\Data\CIHI Wait Times Priority Procedures\CIHI_wait_times.xlsx'
folder_name = xlsx_file.replace('.xlsx', '')

os.makedirs(folder_name, exist_ok=True)

xlsx = pd.ExcelFile(xlsx_file)

# Print all available sheets
print("Available sheets:")
for sheet in xlsx.sheet_names:
    print(f"  - {sheet}")

# Ask user to type which sheet they want
sheet = input("\nType the sheet name exactly as shown above: ")

df = xlsx.parse(sheet)
df.to_csv(f'{folder_name}/{sheet}.csv', index=False)

print(f"Done! '{sheet}.csv' saved to folder: {folder_name}")