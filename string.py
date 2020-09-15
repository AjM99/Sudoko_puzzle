a = "anuj" 
b = a[1]                #indexing
print(b)

for i in a :           #to print entire string completely, vertically
    print(i)

#slicing
c = "Nicole Kidman"
print(c[0:4])          # to give range of word in a long stringss its is from 0 TO 3 NOT 4
print(c[6:])

#concatination
d = a   + c
print(d)

 

#string library
e = c.lower()
print(e)
#there are may more thins u can od like all capital some capital,suffix etc, google it 

#replace (part of library)
f = c.replace("Nicole" , "LOL")
print(f)

g = c.strip()   # removes extra spaces
print(g)

#find (string method)
n = c.find("N") 
print(n)