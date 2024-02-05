import csv

emppay = open('employee_data.csv','r')
#Using csv module, csv file object, important that we do it in two steps
csv_file = csv.reader(emppay)

#Print customer details and skip header
next(csv_file)

for rec in csv_file:
    print(f"Name: {rec[1]}")
    pay = float(rec[3])* (1+float(rec[7]))
    bonus = float(rec[3])* float(rec[7])
    print(f"Salary: $ {rec[3]}\nBonus: $ {bonus}\nTotal Pay: $ {pay}")
    input()