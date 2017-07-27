"""This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. 
The other exercises are: Part 2, Part 3, and Part 4.
Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes 
(8x8 for chess, 19x19 for Go, and many more)."""

def draw(size_row,size_col):
    #size_row = int(input("Please enter the number of rows: "))
    #size_col = int(input("Please enter the number of columns: "))
    rows = "--- "
    cols = "|   "
    for i in range(size_row):
        print(rows*(size_col))
        print(cols*(size_col+1))
    print(rows * size_col)

draw(3,3)
draw(8,8)
draw(19,19)
