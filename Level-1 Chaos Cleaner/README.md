Healthcare Facility Data Analysis – Canada
Overview
This project involved cleaning and analyzing healthcare facility data from Statistics Canada's Open Database of Healthcare Facilities (ODHF). Using Excel functions and pivot tables, I identified and resolved multiple data quality issues including duplicates, inconsistent naming conventions, missing values, and geographic organization problems. The result is a cleaned dataset suitable for accurate healthcare facility analysis and decision-making.
Data Source
Statistics Canada Open Database of Healthcare Facilities
Link: https://www150.statcan.gc.ca/n1/pub/13-26-0001/2020001/ODHF.zip
Data Quality Issues Identified
1. Duplicate Entries from Multiple Data Sources

Rows Affected: 1,420 (approximately 16% of the dataset)
Impact: Overcounting facilities leads to misallocation of government funds. Policy makers may believe an area has more facilities than it actually does, resulting in improper resource distribution.

2. Inconsistent Facility Type Naming

Rows Affected: 654
Examples: "long term care", "long-term care", "longterm care"
Impact: Undercounting of specific facility types leads to poor planning and funding decisions. Government officials may underestimate the true number of facilities of a given type.

3. Missing Facility Type Information

Rows Affected: 1,590 blank entries in source_facility_type
Impact: Researchers and analysts cannot obtain accurate counts of detailed facility types, limiting the depth of analysis possible.

4. Unorganized Geographic Data

Rows Affected: 9,039 (entire dataset)
Impact: Without proper geographic grouping, finding and analyzing facilities by region is time-consuming and inefficient.

Cleaning Methodology
1. Duplicate Removal

Used COUNTIFS function to identify duplicates based on street_no, odhf_facility_type, and postal_code
Created a helper column with IF/AND logic to flag rows for deletion
Retained entries from Public Health Agency of Canada when duplicates existed across multiple data providers

2. Standardizing Facility Type Names

Created a pivot table to identify all variations of facility type names
Applied IFS and PROPER functions to standardize naming conventions (e.g., all variations of "long term care" standardized to "Long-Term Care")

3. Geographic Organization

Used LEFT function to extract the first three characters of postal codes, creating Forward Sortation Area (FSA) identifiers
Built pivot tables to organize facilities by city and FSA, providing clear geographic distribution

Tools & Skills Used

Excel Functions: COUNTIFS, IFS, PROPER, LEFT, TRIM, IF, AND
Excel Features: Pivot Tables, Filtering, Find & Replace
Data Analysis: Data quality assessment, deduplication, standardization

Key Insights
This analysis revealed how duplicate and inconsistent data can significantly impact government resource allocation in healthcare. With approximately 16% of the dataset containing duplicate entries, relying on uncleaned data could lead to substantial misallocation of healthcare funding across Canadian provinces. Proper data cleaning is essential for evidence-based healthcare policy and planning.Healthcare Facility Data Analysis – Canada
Overview
This project involved cleaning and analyzing healthcare facility data from Statistics Canada's Open Database of Healthcare Facilities (ODHF). Using Excel functions and pivot tables, I identified and resolved multiple data quality issues including duplicates, inconsistent naming conventions, missing values, and geographic organization problems. The result is a cleaned dataset suitable for accurate healthcare facility analysis and decision-making.
Data Source
Statistics Canada Open Database of Healthcare Facilities
Link: https://www150.statcan.gc.ca/n1/pub/13-26-0001/2020001/ODHF.zip
Data Quality Issues Identified
1. Duplicate Entries from Multiple Data Sources

Rows Affected: 1,420 (approximately 16% of the dataset)
Impact: Overcounting facilities leads to misallocation of government funds. Policy makers may believe an area has more facilities than it actually does, resulting in improper resource distribution.

2. Inconsistent Facility Type Naming

Rows Affected: 654
Examples: "long term care", "long-term care", "longterm care"
Impact: Undercounting of specific facility types leads to poor planning and funding decisions. Government officials may underestimate the true number of facilities of a given type.

3. Missing Facility Type Information

Rows Affected: 1,590 blank entries in source_facility_type
Impact: Researchers and analysts cannot obtain accurate counts of detailed facility types, limiting the depth of analysis possible.

4. Unorganized Geographic Data

Rows Affected: 9,039 (entire dataset)
Impact: Without proper geographic grouping, finding and analyzing facilities by region is time-consuming and inefficient.

Cleaning Methodology
1. Duplicate Removal

Used COUNTIFS function to identify duplicates based on street_no, odhf_facility_type, and postal_code
Created a helper column with IF/AND logic to flag rows for deletion
Retained entries from Public Health Agency of Canada when duplicates existed across multiple data providers

2. Standardizing Facility Type Names

Created a pivot table to identify all variations of facility type names
Applied IFS and PROPER functions to standardize naming conventions (e.g., all variations of "long term care" standardized to "Long-Term Care")

3. Geographic Organization

Used LEFT function to extract the first three characters of postal codes, creating Forward Sortation Area (FSA) identifiers
Built pivot tables to organize facilities by city and FSA, providing clear geographic distribution

Tools & Skills Used

Excel Functions: COUNTIFS, IFS, PROPER, LEFT, TRIM, IF, AND
Excel Features: Pivot Tables, Filtering, Find & Replace
Data Analysis: Data quality assessment, deduplication, standardization

Key Insights
This analysis revealed how duplicate and inconsistent data can significantly impact government resource allocation in healthcare. With approximately 16% of the dataset containing duplicate entries, relying on uncleaned data could lead to substantial misallocation of healthcare funding across Canadian provinces. Proper data cleaning is essential for evidence-based healthcare policy and planning.