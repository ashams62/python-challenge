import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

row_counter = 0
#total = 0
ballot_ID=[]
county=[]
candidate=[]
count_cand=[]
percentage=[]

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    # Read each row of data after the header
    for row in csvreader:
        ballot_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        row_counter += 1

    print('Election Results')
    print('--------------------------')

    print("Total Votes: " + str(row_counter))

    print('--------------------------')

    candidate_uni_list = unique(candidate)
    #print(candidate_uni_list) 

    size= len(candidate_uni_list)
    #print(size)

    for i in range (size):
        count_cand.append(candidate.count(candidate_uni_list[i]))
        p = 100 * (count_cand[i]/row_counter)
        p = round(p,3)
        percentage.append(p)
        #print(count_cand)
        #print(percentage)
        print(candidate_uni_list[i] + ': ' + str(percentage[i])+ '% ' + '(' + str(count_cand[i]) + ')')
   
    max_vote = max(count_cand)
    
    winner = candidate_uni_list [count_cand.index(max_vote)]
    
    print('--------------------------')
    print('Winner: '+ winner) 
    print('--------------------------')

    txtpath = os.path.join('Analysis', 'pypoll_export.txt')

    with open(txtpath, 'w') as f:
        print('Election Results', file=f)
        print('--------------------------', file=f)

        print("Total Votes: " + str(row_counter), file=f)

        print('--------------------------', file=f)

        for i in range (size):
            count_cand.append(candidate.count(candidate_uni_list[i]))
            p = 100 * (count_cand[i]/row_counter)
            p = round(p,3)
            percentage.append(p)
            print(candidate_uni_list[i] + ': ' + str(percentage[i])+ '% ' + '(' + str(count_cand[i]) + ')', file=f)
   
    
        print('--------------------------', file=f)
        print('Winner: '+ winner, file=f) 
        print('--------------------------', file=f)