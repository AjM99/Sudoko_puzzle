bag = dict()
bag['chips' ] = 1
bag['soda' ] = 2
bag['mountain dew' ] = 3
bag['drugs' ] = 4
print(bag)

print(bag['chips'])

#dictionay is mutable can change values 
bag['chips'] = bag['chips'] +2
print(bag)

#simple way of writing dictionaty
data = {'age' : 20,'height' : 6.2  }
print(data)
# to get  only worsd and not keys
print(list(data))
#printing values 
print(data.values())
#printing keys
print(data.keys())

#searching 
'soda' in bag