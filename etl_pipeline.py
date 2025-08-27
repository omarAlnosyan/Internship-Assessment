import pandas as pd
import warnings
warnings.filterwarnings("ignore")


def load_data():
    """Load sales transaction data from CSV file."""
    try:
        df = pd.read_csv("sales_transactions.csv")
    except FileNotFoundError:
        raise FileNotFoundError("The file 'sales_transactions.csv' was not found.")
    return df

def clean_data(df):
    """Clean and preprocess the sales data."""
    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Convert transaction_date column to datetime
    df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')


    # Keep only rows with positive quantity and price
    df = df[(df['quantity'] > 0)]

    # Calculate total revenue
    df['total_revenue'] = df['unit_price'] * df['quantity']

    return df

def aggregate_data(df):
    """Aggregate revenue by product name."""
    summary = df.groupby('product_name', as_index=False)['total_revenue'].sum()
    return summary

def main():
    df = load_data()
    df_clean = clean_data(df)
    summary = aggregate_data(df_clean)
    print("Revenue summary per product:")
    print(summary)

if __name__ == "__main__":
    main()
