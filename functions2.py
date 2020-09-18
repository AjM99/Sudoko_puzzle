# ARGUMENTS ,they are the input variable of fuctions, in this "a" is argument
 
def LOL(a) :
    if int(a) > 0 :                         #dont froget that u have to mention int ofr numbers
        print('its a number')
    elif a == 'qwe':                        # for string use ==  i.e euqals to
        print('word')
    else :
        print('shit')    



a = input('give input : ')
LOL (a)                                     # calling function and its Argument


#we ca n pass more thsn 1 arguments
#dont run this,if u want to just remove earlier part,traceback error will come i f u dont
def add(x,y) :
    z= x + y

r = add(2,3)
print(z)
