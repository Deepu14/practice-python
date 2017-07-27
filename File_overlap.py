""" Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of 
happy numbers up to 1000."""

"""f1 = open("primenumbers.txt","r")
line1 = f1.readlines()
f2 = open("happynumbers.txt","r")
line2 = f2.readlines()
list1=[]
list2=[]
list3=[]
for i in line1:
    i = i.strip("\n")
    list1.append(int(i))
print(list1)

for i in line2:
    i = i.strip("\n")
    list2.append(int(i))
print(list2)

for i in list1:
    if i in list2:
        list3.append(i)
print(list3)"""

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
