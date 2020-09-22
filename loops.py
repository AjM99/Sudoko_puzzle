#while
n = 2
while n > 0 :
    print("LOL")
    n = n - 1
print("done") 

#break  and continue are used with 'if',  break if condition is satisfied we move  outta loop, in continue even if condition is statisfied we stay inidse loop   

#for loop , its a definate lopp
a = ['anuj','qwe','qwe']
for i in a :
    print('good luck ', i )   #its 'i' not 'a' in print statement

#largest number 
q = [1,3,5,2,6]
largest = -1
for ii in q :
    if ii > largest:
        largest = ii     # this means largest <- ii ,dont write other way round
print(ii)        
    