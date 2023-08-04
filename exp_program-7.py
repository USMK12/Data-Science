import pandas as pd

# Sample data for demonstration
data = {
    'customer_id': [101, 102, 103, 101, 104, 105, 103],
    'product_id': [1, 2, 1, 3, 2, 1, 3],
    'order_date': ['2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04', '2023-07-05', '2023-07-06', '2023-07-07'],
    'order_quantity': [5, 10, 7, 3, 8, 6, 4]
}

# Creating the DataFrame from the sample data
order_data = pd.DataFrame(data)

def main():
    # 1. Total number of orders made by each customer
    customer_order_count = order_data.groupby('customer_id')['order_date'].count()
    print("Total Number of Orders by Each Customer:")
    print(customer_order_count)
    print()

    # 2. Average order quantity for each product
    product_avg_quantity = order_data.groupby('product_id')['order_quantity'].mean()
    print("Average Order Quantity for Each Product:")
    print(product_avg_quantity)
    print()

    # 3. Earliest and Latest order dates in the dataset
    earliest_order_date = order_data['order_date'].min()
    latest_order_date = order_data['order_date'].max()
    print("Earliest Order Date:", earliest_order_date)
    print("Latest Order Date:", latest_order_date)

if __name__ == "__main__":
    main()
