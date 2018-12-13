


#Data 
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]


#Solution
#Calculate Profit as the Difference between Revenue and Expenses
profit = []
for i in range (0, len(revenue)):
    profit.append(revenue[i] - expenses[i])
profit    




#Calculate tax as 30% of profit and round to 2 decimal points
tax = [round(i * 0.3,2) for i in profit]
tax




# Calculate profit remaining after tax is deducted
profitAfterTax = []
for i in range(0, len(profit)):
    profitAfterTax.append(profit[i] - tax[i])
profitAfterTax    




#Calculate The Profit Margin As Profit After Tax Over Revenue
#Round To 2 Decimal Points, Then Multiply By 100 To Get %
profitMargin = []
for i in range (0, len(profitAfterTax)):
    profitMargin.append(profitAfterTax[i] / revenue[i])
profitMargin
profitMargin = [round((i * 100),2) for i in profitMargin]
profitMargin




#Calculate The Mean Profit After Tax For The 12 Months
meanPat = sum(profitAfterTax) / len(profitAfterTax)
meanPat




#Find The Months With Above-Mean Profit After Tax
goodMonths = []
for i in range(0, len(profitAfterTax)):
    goodMonths.append(profitAfterTax[i] > meanPat)
goodMonths    




#Bad Months Are The Opposite Of Good Months!
badMonths = []
for i in range(0, len(profitAfterTax)):
    badMonths.append(profitAfterTax[i] < meanPat)
badMonths    




#The Best Month Is Where Profit After Tax Was Equal To The Maximum
bestMonth = []
for i in range(0, len(profitAfterTax)):
    bestMonth.append(profitAfterTax[i] == max(profitAfterTax))
bestMonth    





#The Worst Month Is Where Profit After Tax Was Equal To The Minimum
worstMonth = []
for i in range(0, len(profitAfterTax)):
    worstMonth.append(profitAfterTax[i] == min(profitAfterTax))
worstMonth    




#Convert All Calculations To Units Of One Thousand Dollars
revenue_1000 = [round(i,0) for i in revenue]
expenses_1000 = [round(i,0) for i in expenses]
profit_1000 = [round(i,0) for i in profit]
profitAfterTax_1000 = [round(i,0) for i in profitAfterTax]



revenue_1000 = [int(i) for i in revenue]
expenses_1000 = [int(i) for i in expenses]
profit_1000 = [int(i) for i in profit]
profitAfterTax_1000 = [int(i) for i in profitAfterTax]




#Print Results
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






