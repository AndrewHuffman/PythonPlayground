#!/usr/bin/env python3
import csv

def csvToArray(csvFileName):
    with open(csvFileName) as csvfile:
        fromReader = csv.reader(csvfile, delimiter=',')
        rows = []
        for row in fromReader:
            rows.append(row)
        return rows
table = csvToArray('2019_accountability_media_file_9.17.19.csv')
column_names = table[0]
row_dicts = []
for row in table:
    dict = {}
    for idx in range(0, len(row)):
        column_name = column_names[idx]
        dict[column_name] = row[idx]
    row_dicts.append(dict)

for row in row_dicts:
    grade = row['Grade']
    if (len(grade) > 1):
        continue
    if (grade not in ['A', 'B', 'C', 'D']):
        print(row['District Name'])

# for name in column_names:
#     csvDict[name] = []