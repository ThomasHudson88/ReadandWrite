#Excerise
#Print each Client name and a number for each one
def main():
    #Open the file
    infile = open('clients.txt','r')

    #Iterate through the list
    cnum = 0
    for line in infile:
        cnum += 1
        print(cnum, line.rstrip('\n'))

    print(f"Total Nuber of Clients: {cnum}")
main()