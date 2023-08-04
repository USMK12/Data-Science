import numpy as np
#sample sales data stored in a numpy array(replace this with your actual sales data)
sales_data=np.array([1000,1500,800,1200,2500,1800,3000,2100,900,1400])

#basic sales analysis
tot_sales=np.sum(sales_data)
avg_sales=np.mean(sales_data)
max_sales=np.max(sales_data)
min_sales=np.min(sales_data)

#find the index of the best-selling product
best_selling_index=np.argmax(sales_data)
best_selling_product_sales=sales_data[best_selling_index]
#output values
print("sales analysis:")
print("--------------")
print(f"total sales:${tot_sales}")
print(f"average sales:${avg_sales:.2f}")
print(f"best-selling_product_sales:${best_selling_product_sales}(product{best_selling_index+1})")
print(f"maximum sales:${max_sales}")
print(f"minimum sales:${min_sales}")
