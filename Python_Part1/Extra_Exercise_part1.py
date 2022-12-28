#%% Exercise1
names = ('Numa' , 'Tullio' , 'Anco')
surnames = ('Pomplio' , 'Ostilio' , 'Marzio')
list1 = [{'first name' : names[0], 'last name' : surnames[0]} ,
         {'first name' : names[1], 'last name' : surnames[1]} ,
         {'first name' : names[2], 'last name' : surnames[2]}]
result = zip(names, surnames)
print(list1)
#%% Exercise1
names = ('Numa' , 'Tullio' , 'Anco')
surnames = ('Pomplio' , 'Ostilio' , 'Marzio')
list1 = []
for name, surname in zip(names,surnames):
    list1.append({'name':name , 'surname': surname})
print(list1)
#%% Solution 2: list comprehension
names = ('Numa' , 'Tullio' , 'Anco')
surnames = ('Pomplio' , 'Ostilio' , 'Marzio')
l = []
l = [{'name': name, 'surname': surname} for name, surname in zip (names, surnames)]
print(l)

#%% EXERCISE1
x = input('Enter your name:')
y = input('Enter your surname:')
z = {
     'name' : x,
     'surname' : y
     }
print(z)