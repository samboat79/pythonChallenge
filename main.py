import os 
import csv
import pathlib

filePath= os.path.join("budget_data_1.csv")
firstMonth = True

#Initialized all variable that are to be used
totalSales = 0.0
totalMonths = 0
saleChanges = []
lastMonthSales = 0.0
salesGreatestIncrease = 0.0
monthGreatestIncrease = ""
salesGreatestDecrease = 0.0
monthGreatestDecrease = ""



#open and read csv
with open(filePath) as csvfile:
    reader = csv.reader(csvfile)
#Pass over the header and set your pointer on the second row
    next(reader)

#Looping through First and second column 

    for row in reader:
        date = row[0]
        currentMonthlySales = float(row[1])

#Change in the monthly sales should begin calculating from the second row
        if firstMonth == True:
            lastMonthSales = currentMonthlySales
            changeInSales = 0
            firstMonth = False
    
        else:
            changeInSales = currentMonthlySales - lastMonthSales
            saleChanges.append(changeInSales)
            lastMonthSales = currentMonthlySales
    
# Tracking how many months of data we have
            totalMonths += 1
# Keep track of total sales
            totalSales = totalSales + currentMonthlySales

        if changeInSales > salesGreatestIncrease :
            salesGreatestIncrease = changeInSales
            monthGreatestIncrease = date
    
        if changeInSales < salesGreatestDecrease:
            salesGreatestDecrease = changeInSales
            monthGreatestDecrease = date

#finding the average and printing out results
#Greatest revenue and Decrease in Revenue
#Total Revenue
#Total months

line = ('.' * 40)

financialAnalysis = (
        f' Financial Analysis\n \
        {line}\n \
        Total Months: {totalMonths}\n \
        Total Revenue: ${totalSales}\n \
        Average Revenue change: $a{sum(saleChanges) / len(saleChanges)}\n \
        Greatest Decrease in Revenue:{monthGreatestDecrease} (${salesGreatestDecrease})\n \
        Greatest Increase in Revenue: {monthGreatestIncrease} (${salesGreatestIncrease})\n' )

#print your financial Analysis
print(financialAnalysis)

#print to file
with open("budget_data_1.txt", 'w') as outputFile:
    outputFile.write(financialAnalysis)






