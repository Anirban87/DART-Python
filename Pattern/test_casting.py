import csv

with open('EGFD_WO_1_TimeLog.csv', 'r') as csvfile:
    arr = csv.reader(csvfile, delimiter= ',')
    for row in arr:
            print (row)
