import pandas as pd
import matplotlib.pyplot as plt

Ames = pd.read_csv('Ames.csv')

plt.figure(figsize=(18, 6))
feature = 'SalePrice'

plt.boxplot(Ames[feature], vert=True, widths=0.7,medianprops=dict(color="red"))
plt.title('Sale Price box-plot', fontsize=16)
plt.ylabel('Sale Price', fontsize=14)
plt.xlabel('')  # Removing the x-axis label as it's not needed



plt.show()