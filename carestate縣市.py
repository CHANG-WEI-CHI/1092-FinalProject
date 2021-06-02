import csv
with open('109年6月行政區社區照顧關懷據點統計_縣市.csv',newline = '') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for old in csvreader:
        print(old['COUNTY'])