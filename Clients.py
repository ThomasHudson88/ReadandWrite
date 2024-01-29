#Excerise
#Print each Client name and a number for each one
def main():
    #Open the file
    infile = open('clients.txt','r')

    #Iterate through the list
    cnum = 1
    for line in infile:
        print(cnum, line.rstrip('\n'))
        cnum += 1

main()