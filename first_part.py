import pandas as pd

ames = pd.read_csv('Ames.csv')

#salePriceSmall = ames[(ames['SalePrice'] < 100000)] # With that we can eliminate what we want.
#print(len(salePriceSmall)) #with that we can see how many are there
#print(ames.dtypes) #Gives dataTypes
#print(ames.shape) #how many column and row are there

mean = ames['SalePrice'].mean()
median = ames['SalePrice'].median()
mode = ames['SalePrice'].mode()[0] #with that i took only the mode value
standardDeviation= ames['SalePrice'].std()

print('Mean: ' + str(mean) + 
    '\nMedian: ' + str(median) +
    '\nMode: ' + str(mode) +
    '\nStandard Deviation: ' + str(standardDeviation))