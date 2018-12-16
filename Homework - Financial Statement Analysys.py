#Data 
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]


#Solution
#Calculate profit as the difference between revenue and expenses
profit = []
for i in range (0, len(revenue)):
    profit.append(revenue[i] - expenses[i])
profit    


#Calculate TAX as 30% of profit and round to 2 decimal points
tax = [round(i * 0.3,2) for i in profit]
tax


# Calculate profit remaining after TAX is deducted
profitAfterTax = []
for i in range(0, len(profit)):
    profitAfterTax.append(profit[i] - tax[i])
profitAfterTax    


#Calculate the profit margin as profit after TAX over revenue
#Round to 2 decimal points, then multiply by 100 to get %
profitMargin = []
for i in range (0, len(profitAfterTax)):
    profitMargin.append(profitAfterTax[i] / revenue[i])
profitMargin
profitMargin = [round((i * 100),2) for i in profitMargin]
profitMargin


#Calculate the mean profit after TAX for the 12 months
meanPat = sum(profitAfterTax) / len(profitAfterTax)
meanPat


#Find the months with above-mean profit after TAX
goodMonths = []
for i in range(0, len(profitAfterTax)):
    goodMonths.append(profitAfterTax[i] > meanPat)
goodMonths    


#Bad months are the opposite of good months
badMonths = []
for i in range(0, len(profitAfterTax)):
    badMonths.append(profitAfterTax[i] < meanPat)
badMonths    


#The best month is where profit after TAX was equal to the maximum
bestMonth = []
for i in range(0, len(profitAfterTax)):
    bestMonth.append(profitAfterTax[i] == max(profitAfterTax))
bestMonth    


#The worst month is where profit after TAX was equal to the minimum
worstMonth = []
for i in range(0, len(profitAfterTax)):
    worstMonth.append(profitAfterTax[i] == min(profitAfterTax))
worstMonth    


#Convert all calculations to units of one thousand Dollars
revenue_1000 = [round(i/1000,2) for i in revenue]
expenses_1000 = [round(i/1000,2) for i in expenses]
profit_1000 = [round(i/1000,2) for i in profit]
profitAfterTax_1000 = [round(i/1000,2) for i in profitAfterTax]


revenue_1000 = [int(i) for i in revenue_1000]
expenses_1000 = [int(i) for i in expenses_1000]
profit_1000 = [int(i) for i in profit_1000]
profitAfterTax_1000 = [int(i) for i in profitAfterTax_1000]


#Print results
print ("Revenue :") 
print (revenue_1000)
print ("Expenses :") 
print (expenses_1000)
print ("Profit :")
print(profit_1000)
print ("Profit after tax :")
print (profitAfterTax_1000)
print ("Profit margin :")
print (profitMargin)
print ("Good months :")
print (goodMonths)
print ("Bad months :")
print (badMonths)
print ("Best month :")
print (bestMonth)
print ("Worst month :")
print (worstMonth)
