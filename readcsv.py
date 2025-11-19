#read each row frim a given csv file and print it a s a list of strings
import csv
with open('sample.csv',mode ='r')as file:
    csvFile=csv.reader(file)
    for lines in csvFile:
        print(lines)
