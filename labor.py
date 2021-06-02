import csv
with open('移工總數.csv',newline = '',encoding="utf-8") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for labor in csvreader:
        print(labor['　家庭看護工'])
        