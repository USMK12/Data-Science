#program 11

import matplotlib.pyplot as plt 
#sample data for monthly sales
months=['jan','feb','mar','apr','may']
sales=[10000,12000,8000,15000,11000]

#creating a line plot
plt.plot(months,sales,marker='o')
plt.xlabel('months')
plt.ylabel('sales')
plt.title('monthly sales prediction')
plt.grid(True)
plt.show()
print()
#scatter plot
plt.scatter(months,sales)
plt.xlabel('months')
plt.ylabel('sales')
plt.title('monthly sales prediction')
plt.grid(True)
plt.show()
#bar plot
plt.bar(months,sales)
plt.xlabel('months')
plt.ylabel('sales')
plt.title('monthly sales prediction')
plt.grid(True)
plt.show()
