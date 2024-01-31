import csv

def main():
    customers = open('customers.csv','r')
    #Using csv module, csv file object, important that we do it in two steps
    csv_file = csv.reader(customers)

    #Print customer details and skip header
    next(csv_file)
    num =0

    #Create the New CSV
    outfile = open('customer_country.csv','w')
    outfile.write(F"Full Name, Country \n")

    #Go through each customer and just slect Full name and country to the new csv
    for rec in csv_file:
        num +=1
        print(f"{rec[1]}  {rec[2]}, {rec[4]}")
        outfile.write(f'{rec[1]} {rec[2]},{rec[4]} \n')

    print(f"Total Employees: {num}")
    #always close any file you write to
    outfile.close()

main()