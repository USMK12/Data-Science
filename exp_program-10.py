import pandas as pd
import matplotlib.pyplot as plt

# Sample monthly sales data
data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'sales': [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2300, 2100, 1900, 1800, 1600]
}

# Creating the DataFrame from the sample data
monthly_sales_data = pd.DataFrame(data)

def plot_line_chart():
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_sales_data['month'], monthly_sales_data['sales'], marker='o', linestyle='-', color='b')
    plt.title('Monthly Sales Data')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_line_chart()

#bar graph
import pandas as pd
import matplotlib.pyplot as plt

# Sample monthly sales data
data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'sales': [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2300, 2100, 1900, 1800, 1600]
}

# Creating the DataFrame from the sample data
monthly_sales_data = pd.DataFrame(data)

def plot_bar_chart():
    
    plt.figure(figsize=(10, 6))
    plt.bar(monthly_sales_data['month'], monthly_sales_data['sales'], color='b')
    plt.title('Monthly Sales Data')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid(axis='y')
    plt.show()

if __name__ == "__main__":
    
