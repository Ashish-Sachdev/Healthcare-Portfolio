# import pandas as pd

# xlsx = pd.ExcelFile('2009-2025_annual_surgical_wait_times.xlsx')

# # Print all sheet names first so you know what's available
# print(xlsx.sheet_names)

# # Then convert just the one you want
# df = xlsx.parse('SheetNameHere')
# df.to_csv('output.csv', index=False)

# print("Done!")



import pandas as pd
import os

xlsx_file = '2009-2025_annual_surgical_wait_times.xlsx'
folder_name = xlsx_file.replace('.xlsx', '')  # folder named after your file

os.makedirs(folder_name, exist_ok=True)  # creates the folder if it doesn't exist

xlsx = pd.ExcelFile(xlsx_file)

for sheet in xlsx.sheet_names:
    df = xlsx.parse(sheet)
    df.to_csv(f'{folder_name}/{sheet}.csv', index=False)

print(f"Done! All sheets saved to folder: {folder_name}")