class PartyAnimal :             #name of the object
    x=0                         #value of the object
    def party(self) :            #code or constructor of thr object
        self.x = self.x + 1
        print('so far',self.x  )    

    def trash(self):
        print('i am destructed',self.x)   #destructor

an = PartyAnimal()          #closing the object , u can give value of self in this dependnig upon code
an.party()                  # this is output display  statement ,without this no output
an.party()
an.trash()
an = 63
print('slo',an)
