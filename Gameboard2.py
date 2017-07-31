import random
list1 = []
list2 = []
list3 = []
finallist = []
for i in range(3):
    list1.append(random.randrange(0,3))
    list2.append(random.randrange(0,3))
    list3.append(random.randrange(0,3))
finallist = [list1,list2,list3]
print(finallist)
def game(finallist):
    #check columns
    for i in range(3):
        col = set([finallist[0][i],finallist[1][i],finallist[2][i]])
        if len(col) == 1 and finallist[0][i] != 0:
            return print("winner is player:",finallist[0][i])
    #check rows
    for i in range(3):
        rows = set([finallist[i][0],finallist[i][1],finallist[i][2]])
        if len(rows) == 1 and finallist[i][0]!=0:
            return print("winner is player: ",finallist[i][0])
    #check diagnols
        diag1 = set([finallist[0][0],finallist[1][1],finallist[2][2]])
        diag2 = set([finallist[0][2],finallist[1][1],finallist[2][0]])
        if (len(diag1) == 1 or len(diag2) == 1) and finallist[1][1] !=0:
            return(print("winner is player: ",finallist[1][1]))
        return (print("No winner"))

game(finallist)
