""" Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of 
happy numbers up to 1000."""

def openfiles(filename):
    list1=[]
    f = open(filename,"r")
    line = f.readlines()
    for i in line:
        i = i.strip("\n")
        list1.append(int(i))
    return list1
primes = openfiles("primenumbers.txt")
happynumbers = openfiles("happynumbers.txt")
print(primes)
print("\n")
print(happynumbers)

finallist = [ ]
for i in primes:
    if i in happynumbers:
        finallist.append(i)
print("\n")
print(finallist)
