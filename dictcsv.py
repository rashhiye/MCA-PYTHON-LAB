#write a python dictionary to a csv file,read the csv file and print its content
import csv
mydict = [{'Name': 'John', 'Age': 28, 'Country': 'New York'},
            {'Name': 'Anna', 'Age': 22, 'Country': 'London'},
            {'Name': 'Mike', 'Age': 32, 'Country': 'San Francisco'}]
with open('sample.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'City'])
    writer.writeheader()
    for data in mydict:
        writer.writerow(data)
with open('output.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
