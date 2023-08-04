#program 12
import matplotlib.pyplot as plt
months=['Jan','Feb','Mar','Apr','May','June','Jul','Aug','Sep','Oct','Nov','Dec']
temp=[22,23,21,19,15,18,25,24,22,89,75,72]
plt.plot(months,temp,marker='o')
plt.xlabel('Months')
plt.ylabel('Data in (mm)')
plt.title('Monthly Rainfall Data')
plt.grid(True)
plt.show()
print()
plt.scatter(months,temp)
plt.xlabel('Months')
plt.ylabel('Data in (mm)')
plt.title('Monthly Rainfall Data')
plt.grid(True)
plt.show()
