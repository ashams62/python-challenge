import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

row_counter = 0
total = 0
date=[]
p_l=[]
change=[]
b = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        date.append(row[0])
        p_l.append(row[1])
        row_counter += 1
        total += int(row[1])
        a=int(row[1])
        change.append(a-b)
        b=int(row[1])

    change.pop(0)

    print('Financial Analysis')
    print('--------------------------')

    print("Total Months: " + str(row_counter))
    print("Total: $" + str(total))
    ave_chg = round(sum(change)/len(change),2)
    print('Average Change: '+ '$' + str(ave_chg))

    #print(date)
    #print(p_l)
    #print(change)
    
    max_chg = max(change)
    min_chg = min(change)
    
    max_date = date [change.index(max_chg)+1]
    min_date = date [change.index(min_chg)+1]

    print('Greatest Increase in Profits: ' + str(max_date) + ' ($' + str(max_chg)+ ')')
    print('Greatest Decrease in Profits: ' + str(min_date) + ' ($' + str(min_chg)+ ')')

    txtpath = os.path.join('Analysis', 'pybank_export.txt')

    with open(txtpath, 'w') as f:
        print('Financial Analysis',file=f)
        print('--------------------------',file=f)

        print("Total Months: " + str(row_counter), file=f)
        print("Total: $" + str(total),file=f)
    
        print('Average Change: '+ '$' + str(ave_chg),file=f)

        print('Greatest Increase in Profits: ' + str(max_date) + ' ($' + str(max_chg)+ ')',file=f)
        print('Greatest Decrease in Profits: ' + str(min_date) + ' ($' + str(min_chg)+ ')',file=f)

