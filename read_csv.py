import csv

customers = open('customers.csv','r')
#Using csv module, csv file object, important that we do it in two steps
csv_file = csv.reader(customers)

#Print customer details and skip header
next(csv_file)

for rec in csv_file:
    print(f"first Name: {rec[1]} Last name: {rec[2]}")
    input()