# opening of file, pattern =>  handele = open('filename.txt','mode')  if mode not mentoned consider it to be read
x = open('first.py') 
print(x)

#this will display the code of file in  terminal
y=  open("second.py")
#for i in  y :
#   print(i)
 #z = y.read()   
#print(len((z))

#searching
#for h in y :  
 #   h=h.rstrip()                  #when running this comment others
  #  if h.startswith("if") :
   #     print(h)
   
# for counting  lines 
count = 0
for ii in y :
   count = count + 1
print("no of line:",count)     

   