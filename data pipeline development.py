import pandas as pd
import numpy as np

def generate_dummy_data(num_rows=100):
    """
    Generates dummy data for pipeline development.

    Args:
        num_rows (int): The number of rows to generate.

    Returns:
        pd.DataFrame: A Pandas DataFrame containing the dummy data.
    """

    data = {
        'transaction_id': np.arange(1, num_rows + 1),
        'customer_id': np.random.randint(1000, 2000, num_rows),
        'transaction_date': pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 365, num_rows), unit='D'),
        'amount': np.random.uniform(10, 1000, num_rows),
        'product_category': np.random.choice(['Electronics', 'Clothing', 'Home Goods', 'Books'], num_rows),
        'location': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston'], num_rows)
    }
    df = pd.DataFrame(data)
    return df

def data_cleaning(df):
    """
    Performs basic data cleaning operations.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    # Example cleaning steps (replace with your actual cleaning logic)
    df = df.dropna() # Drop rows with missing values
    df = df[df['amount'] > 0] # Filter out negative or zero amounts
    return df

def data_transformation(df):
    """
    Performs data transformation.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The transformed DataFrame.
    """

    #Example transformation
    df['transaction_year'] = df['transaction_date'].dt.year
    return df

def data_aggregation(df):
    """
    Performs data aggregation.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The aggregated DataFrame.
    """
    #Example aggregation
    agg_df = df.groupby('product_category')['amount'].sum().reset_index()
    return agg_df


if __name__ == '__main__':
    # Generate dummy data
    dummy_data = generate_dummy_data(num_rows=100)
    print("Generated Dummy Data:")
    print(dummy_data.head())

    # Clean the data
    cleaned_data = data_cleaning(dummy_data)
    print("\nCleaned Data:")
    print(cleaned_data.head())

    # Transform the data
    transformed_data = data_transformation(cleaned_data)
    print("\nTransformed Data:")
    print(transformed_data.head())

    # Aggregate the data
    aggregated_data = data_aggregation(transformed_data)
    print("\nAggregated Data:")
    print(aggregated_data.head())
