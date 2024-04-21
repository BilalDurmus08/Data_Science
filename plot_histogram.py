import matplotlib.pyplot as plt
import pandas as pd

# Bring data from Sale Price inside of Ames.csv for the histogram
ames = pd.read_csv('Ames.csv')
data = ames['SalePrice']
 
# Plotting a basic histogram
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
 
# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Sale Prices of Houses Histogram')
 
# Display the plot
plt.show()