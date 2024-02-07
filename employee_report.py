#employee Report - need to get the efficiency of each employee and group by ages

import csv

def main():
      

    def efficiency():
        empdata = open('employee_data.csv','r')
        #Using csv module, csv file object, important that we do it in two steps
        csv_file = csv.reader(empdata)
        next(csv_file)
        #efficiency = productivity / hours worked, (list 5 / list 4)
        high_effic_indv = []
        low_effic_indv = []

        for rec in csv_file:
            if float(rec[5]) / float(rec[4]) > 2:
                high_effic_indv.append(rec[1])
            elif float(rec[5]) / float(rec[4]) <1:
                low_effic_indv.append(rec[1])
        
        print(f"Highly Efficient Individuals")
        for name in high_effic_indv:
            print(name)

        print(f"\nLow Efficiency individuals")
        for name in low_effic_indv:
            print(name)

    efficiency()
    
    def ages():
        empdata = open('employee_data.csv','r')
        #Using csv module, csv file object, important that we do it in two steps
        csv_file = csv.reader(empdata)
        next(csv_file)
       
        #Create three list for the 20s, 30s, and 40s on age
        age20 = []
        age30 = []
        age40 = []

        for name in csv_file:
            if 20 <= float(name[2]) < 30:
                age20.append(name[1])
            elif  30 <= float(name[2]) < 40:
                age30.append(name[1])
            elif 40 <= float(name[2]) < 50:
                age40.append(name[1])
        
        num = 0
    
        print(f'\nEmployees in their 20s')
        for name in age20:
            num +=1
            print(name)
        print(f'\n Total number of employees in 20s: {num}')
        
        num = 0
        print(f'\nEmployees in their 30s')
        for name in age30:
            num +=1
            print(name)
        
        print(f'\n Total number of employees in 30s: {num}')
        
        num = 0
        print(f'\nEmployees in their 40s')
        for name in age40:
            num +=1
            print(name)
        print(f'\n Total number of employees in 40s: {num}')

    ages()


main()