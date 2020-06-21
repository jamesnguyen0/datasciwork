#libraries
import os
import csv

#variables
months = 0
netChange = 0
avgChange = 0
totalAbsoluteChanges = 0
maxIncrease = ["", 0]
maxDecrease = ["", 0]

#read files
pybank_csv = os.path.join("Resources","budget_data.csv")
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skip header   
    next(csvreader)
    
    #loop through each row
    for row in csvreader:
        #calculations
        months += 1
        netChange += int(row[1])
        totalAbsoluteChanges += abs(int(row[1]))

        if int(row[1]) > int(maxIncrease[1]):
            maxIncrease[0] = row[0]
            maxIncrease[1] = row[1]
        if int(row[1]) < int(maxDecrease[1]):
            maxDecrease[0] = row[0]
            maxDecrease[1] = row[1]
    
    avgChange = round(totalAbsoluteChanges/months, 2)

    #output to console
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${netChange}")
    print(f"Average Change: ${avgChange}")
    print(f"Greatest Increase in Profits: {maxIncrease[0]} (${maxIncrease[1]})")
    print(f"Greatest Decrease in Profits: {maxDecrease[0]} (${maxDecrease[1]})")

    #prep text for output to .txt
    text = []
    
    text.append("Financial Analysis")
    text.append("----------------------------")
    text.append("Total Months: " + str(months))
    text.append("Total: $" + str(netChange))
    text.append("Average Change: $" + str(avgChange))
    text.append("Greatest Increase in Profits: " + maxIncrease[0] + " $" + str(maxIncrease[1]))
    text.append("Greatest Decrease in Profits: " + maxDecrease[0] + " $" + str(maxDecrease[1]))
    
    outputtext = zip(text)

#write files
output_file = os.path.join("Analysis","PyBank_analysis.txt")    
with open(output_file, 'w') as datafile:
    writer = csv.writer(datafile)
    writer.writerows(outputtext)
