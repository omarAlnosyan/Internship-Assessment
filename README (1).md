# Sales Transactions ETL Script

This Python script loads, cleans, and aggregates sales transaction data from a CSV file and prints the total revenue per product.

## Requirements

- Python 3.x
- Pandas library

You can install Pandas using pip if it is not already installed:

```bash
pip install pandas

How to Run
1. Make sure sales_transactions.csv is in the same folder as the script.
2. Open a terminal or command prompt.
3. Run the script using Python: python etl_script.py
4. The script will print a revenue summary per product.



Assumptions
1.The CSV file exists in the same directory as the script.
2.Only positive values for quantity are valid.
3.Duplicate rows in the dataset should be removed.
4.transaction_date can be converted to datetime; invalid dates will be set to NaT.
5.Revenue is calculated as unit_price * quantity.
6.Aggregation is based on product_name rather than product_id.

Notes
1.All warnings are suppressed in the script using the Python warnings library.
2.The script will raise a clear error if the CSV file is missing.


