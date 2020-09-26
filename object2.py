class partyAnimal :
    x=0
    name=""
    def party(self,z) :
        self.name = z
        print(self.name,'is in')

    def party2(self) :
        self.x = self.x + 1
        print('is there',self.x)    

an = partyAnimal()              
an.party2()                     #output will be in order u write this  
an.party2() 

an.party('me')
an.party("u")   
