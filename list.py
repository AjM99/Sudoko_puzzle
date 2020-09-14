a=['anuj',20,6.2]
print(a)
b=['anuj',[2,3],123]
print(b)
#looking inside list
print(a[1])
#strings are not mutable but list are
a[2]=12241
print(a)
#checking length
print(len(a))
#print(range(len(a)))

#slcing
print(a[0:2])

# building list
c = list()
c.append('lol')
c.append('lol2')
print(c)
#checking for things in list
'lol' in c

#sorting alphbetically, sorting elements must be all strings 
d = ['anuj','tom','anne','niclole']
d.sort()
print(d)

#math function in list
e =[1,2,3,48,7,9]
print(sum(e))
print(len(e))
print(max(e))
print(min(e))
print(sum(e)/len(e))

#making a list out of string  split
aa = "thressss words are"
bb = aa.split()
print(bb)
cc = aa[0]
dd = cc.split("e")          #splits at 'e'
print(dd)