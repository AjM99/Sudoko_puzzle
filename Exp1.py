#calculating avg
#count = 0
#total = 0

#while True :
#    a = input("enter a number, print done when u done :")
#    if a =='done' :
#        break
#    value = float(a)
#    count = count + 1
#    total = total + value
#    avg =total/count
#print("avg is  : ",avg)    


#doing same thing with list
c= list()
while True :
    inp=input("enter a value : ")
    if inp =='done':break
    value = float(inp)        
    c.append(value)
avg=sum(c)/len(c)
print(avg)
