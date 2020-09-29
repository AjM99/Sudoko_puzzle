#combintion of list in dictionary    very imp
Dictonary = dict()
L = ['asd','asdd','assdf','asd','asd']
for i in L :
    Dictonary[i] = Dictonary.get(i,0) + 1
print(Dictonary)    

#how to use this , find how many times a word is repeated in  a line
a = dict()
b = input('enter a line')
word = b.split()
for  i in  word :
    a [i] = a.get(i,0) +1
print(a)    