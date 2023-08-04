import pandas as pd

# Sample sales data in the format of a dictionary with product names as keys and quantities sold as values
sales_data = {
    "Product A": 100,
    "Product B": 80,
    "Product C": 120,
    "Product D": 150,
    "Product E": 90,
    "Product F": 60,
    # Add more products and their sales data here
}

# Create a DataFrame from the sales_data dictionary
df = pd.DataFrame(list(sales_data.items()), columns=["Product", "Quantity Sold"])

# Sort the DataFrame by Quantity Sold in descending order
df_sorted = df.sort_values(by="Quantity Sold", ascending=False)

# Retrieve the top 5 products
top_5_products = df_sorted.head(5)

print("Top 5 products sold the most in the past month:")
print(top_5_products)
