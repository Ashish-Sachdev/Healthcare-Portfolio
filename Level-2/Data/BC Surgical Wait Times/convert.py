# import pandas as pd

# xlsx = pd.ExcelFile(r'D:\Healthcare Analytics Portfolio\Level-2\Data\CIHI Wait Times Priority Procedures\CIHI_wait_times.xlsx')

# # Print all sheet names first so you know what's available
# print(xlsx.sheet_names)

# # Then convert just the one you want
# df = xlsx.parse('Table 1')
# df.to_csv('output.csv', index=False)

# print("Done!")


# from xlsx to csv import converter:

# import pandas as pd
# import os

# xlsx_file = r'D:\Healthcare Analytics Portfolio\Level-2\Data\CIHI Wait Times Priority Procedures\CIHI_wait_times.xlsx'
# folder_name = xlsx_file.replace('.xlsx', '')

# os.makedirs(folder_name, exist_ok=True)

# xlsx = pd.ExcelFile(xlsx_file)

# # Print all available sheets
# print("Available sheets:")
# for sheet in xlsx.sheet_names:
#     print(f"  - {sheet}")

# # Ask user to type which sheet they want
# sheet = input("\nType the sheet name exactly as shown above: ")

# # Skip the title row, use row 2 as headers
# df = xlsx.parse(sheet, skiprows=1)
# df = df.loc[:, ~df.columns.str.contains('^Unnamed|^Column', na=False)]
# # Show columns so you can verify it worked
# print("\nColumns found:")
# for col in df.columns.tolist():
#     print(f"  - {col}")

# df.to_csv(f'{folder_name}/{sheet}.csv', index=False)

# print(f"Done! '{sheet}.csv' saved to folder: {folder_name}")




# from docx to pdf import converter: 

# from docx2pdf import convert
# import os

# docx_file = r'C:\Word Documents\Job Description.docx'

# convert(docx_file)

# pdf_name = os.path.splitext(os.path.basename(docx_file))[0] + '.pdf'
# print(f"Done! '{pdf_name}' saved.")

#Create a database:
# import sqlite3

# conn = sqlite3.connect(r"D:\Healthcare Analytics Portfolio\Level-2\Data\healthcare_waittimes.db")

# print("Database created successfully!")
# conn.close()


import sqlite3
import pandas as pd

# Connect to your database
conn = sqlite3.connect(r"D:\Healthcare Analytics Portfolio\Level-2\Data\healthcare_waittimes.db")

# Read your sheets
df1 = pd.read_excel(r"D:\Healthcare Analytics Portfolio\Level-2\Data\CIHI Wait Times Priority Procedures\CIHI_wait_times.xlsx", sheet_name="Table 1", skiprows=1)
df2 = pd.read_excel(r"D:\Healthcare Analytics Portfolio\Level-2\Data\BC Surgical Wait Times\2009-2025_annual_surgical_wait_times.xlsx", sheet_name="Sheet1")

# Write them into the database as tables
df1.to_sql("cihi_table1", conn, if_exists="replace", index=False)
df2.to_sql("bc_table2", conn, if_exists="replace", index=False)

print("Done! Both sheets loaded into the database.")
conn.close()