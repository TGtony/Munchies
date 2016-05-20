import csv
import json

csvfile = open('database.csv', 'r')
jsonfile = open('database.json', 'w')

#csvfile = open('deelte.csv', 'r')
#jsonfile = open('delete.json', 'w')

#fieldnames = ("1")
fieldnames = ("asin","description","title","url")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
