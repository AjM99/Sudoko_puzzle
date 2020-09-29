sudoku = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,4,0,0,0,6,0],
    [6,0,0,0,6,0,0,9,3],
    [4,0,0,8,0,3,0,7,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9] 
]
def sudoku_board(b):
    for i in range (len(b)):            #this is for spacing between rows
        if i % 3 ==0 and i != 0:
            print('-----------------------------')            
        for j in range (len(b[0])):
            if j % 3==0 and j !=0:
                print(' | ', end ='')   #end is very important  
            if j==8:                    #8 as in column, i = rows , j = column
                print(b[i][j])
            else:
                print(str(b[i][j]), end = '  ') #this end is for spacing between numbers 

#sudoku_board(sudoku)




def f_empty_spaces(b):                 # this function is to find empty spaces(0) so that we can fill them in next function
    for i  in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] ==0:
                return(i,j)
    return None



def valid(b,n,pos):
    for i in  range(len(b)):            # for columns
        if b[i][pos[1]] == n and pos[0] !=i:
            return False      

    for i in  range(len(b[0])):            # for columns
        if b[pos[0]][i] == n and pos[1] !=i:
            return False

    box_x = pos[1]// 3
    box_y = pos[0]// 3
    
    for i in range(box_y * 3, box_y * 3 + 3):       #for boxes
        for j in range(box_x * 3, box_x *3 + 3): 
            if b[i][j] == n  and (i,j) != pos:
                return False     
   
    return True



 #main logic for solving
def solve(b):
    f = f_empty_spaces(b)
    if not f:
        return True
    else:
        row, col = f
    for i in range(1,10):
        if valid(b, i, (row, col)):
            b[row][col] = i 

            if solve(b):
                return True
                
            b[row][col] = 0         #in case we dont get the answer we putback value as 0          

    return False


sudoku_board(sudoku)
solve(sudoku)
print("__________________________________________")
sudoku_board(sudoku)



