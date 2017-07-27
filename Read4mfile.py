""" Given a .txt file that has a list of a bunch of names, count how many of each name there are 
in the file, and print out the results to the screen. I have a .txt file for you, if you want to 
use it! """
"""
Extra:
Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt 
file, and count how many of each “category” of each image there are. This text file is actually a list
of files corresponding to the SUN database scene recognition database, and lists the file directory 
hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear 
which part represents the scene category. To do this, you’re going to have to remember a bit about 
string parsing in Python 3. I talked a little bit about it in this post. """

f=open('nameslist.txt','r')
line = f.readlines()
dict1 = {}
for i in line:
    i=i.strip('\n')
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)


""" Extra """
f = open("Training_01.txt",'r')
line = f.readlines()
dict2 = {}
for i in line:
    i = i.split('/')
    i = i[2]
    if i in dict2:
        dict2[i] += 1
    else:
        dict2[i] = 1
print(dict2)
