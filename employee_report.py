#employee Report - need to get the efficiency of each employee and group by ages

import csv

def main():
    empdata = open('employee_data.csv','r')
    #Using csv module, csv file object, important that we do it in two steps
    csv_file = csv.reader(empdata)
    next(csv_file)  

    def efficiency():

        #efficiency = productivity / hours worked, (list 5 / list 4)
        high_effic_indv = []
        low_effic_indv = []

        for rec in csv_file:
            if float(rec[5]) / float(rec[4]) > 2:
                high_effic_indv.append(rec[1])
            elif float(rec[5]) / float(rec[4]) <1:
                low_effic_indv.append(rec[1])
        
        print("Highly Efficient Individuals")
        for name in high_effic_indv:
            print(name)

        print(f"\nLow Efficiency individuals")
        for name in low_effic_indv:
            print(name)

    efficiency()
    
    def ages():
        #Create three list for the 20s, 30s, and 40s on age
        age20 = []
        age30 = []
        age40 = []

        for rec in csv_file:
            if float(rec[2]) >= 20 and float(rec[2]) < 30:
                age20.append(float(rec[2]))
            elif float(rec[2]) >= 30 and float(rec[2]) < 40:
                age30.append(float(rec[2]))
            else: 
                age40.append(float(rec[2]))
    
        print(age20)
    ages()


main()