import csv
with open('108年產業及社福外籍勞工人數_縣市.csv',newline = '') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for old in csvreader:
        print(old['COUNTY'])
    

