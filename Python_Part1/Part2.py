#%% Iterators While loop
i = 0
while i < 3:
    print('*', end = '')
    i += 1 
#%% Iterators For loop EXERCISE 1
for i in range(0,6):
    if i % 2 != 0:
        print('*'*i)
#%% Iterators For loop EXERCISE 2
todo = ["exercise1", "exercise2", "exercise3","coffee break" ,"exercise4","exercise5","exercise6"]
for x in todo:
    if x .upper() == "COFFEE BREAK":
        print(x)
        break
#%% Iterators For loop EXERCISE 3
list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}
# Iterating through list
for i in list1:
    print(i)
    
# Iterating through turple
for i in tuple1:
    print(i)
    
# Iterating through set   
for i in set1:
    print(i)
    
# Iterating through dict    
for x,y in dict1.items():
    if y == 'land':
        print(f'{x} lives in {y}')
#%%  DATA STRUCTURES
list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}
            # 1.PRINTING THE LENGTHS OF ALL ELEMENTS
#length of list
print(len(list1))
#length of tuple
print(len(tuple1))
#length of set
print(len(set1))
#length of dict
print(len(dict1))
             # 2.PRINTING THE FIRST ELEMENT OF list1 and tuple1

print(list1[0])
print(tuple1[0])
            # 3.PRINTING THE VALUE OF lion key of dict1
print(dict1['lion'])
            # 4.CHANGING THE SECOND POSITION OF list1 TO 'rabbit'
list1[1] = 'rabbit'
print(list1)
            # 5.TRYING TO CHANGE THE 2nd position element of the tuple to 'rabbit'
tuple1[1] = 'rabbit'
#Trying to run thie above command i get an error because tuples are unchangeable or immmutable

            # 6.ADING 'momkey' to list
list1.append('monkey')
print(list1)
            # 7.REMOVUNG 'rabbit form the list
list1.remove('rabbit')
print(list1)
            # 8. Fixing the wrong value of the number of feets for the fish
dict1['fish'] = 0
print(dict1)

#%% EXERCISE 1 FUNCTIONS
def goodbye():
    print('good bye')
goodbye()

#%% EXERCISE 2 FUNCTIONS
def goodbye(name):
    print(f'Good bye {name}')
goodbye('Julien')

#%% EXERCISE 3 FUNCTIONS
import os
user = os.getlogin()
print(user)


#%% EXERCISE 4 FUNCTIONS
def greeting():
    family = ['John Doe','Tristram Mcbride','Baldwin Preston', 'Wally Collins']
    for person in family:
        print(f'Hello {person}!')
greeting()
#%% EXERCISE 4 FUNCTIONS  --version without classes
def greeting(newcomer,default = 'John Doe'):
    family = []
    family.append(default)
    family.append(newcomer)
    for person in family:
        print(f'Hello {person}!')
greeting('Julien Chambali')
#%% EXERCISE 4 FUNCTIONS -- version with classes
class greeting:
    def __init__(self,newcomer,default ='John Doe'):
        self.newcomer = newcomer
        self.default = default
    def sayhello(self):
        family = []
        family.append(self.default)
        family.append(self.newcomer)
        for person in family:
            print(f'Hello {person}!')      
newperson = greeting('Julien Chambali')
newperson.sayhello()     


#%% EXERCISE 5 FUNCTIONS
import random
def random_list_summer():
    list1 = []
    for i in range(15):
        x = random.randint(-100, 100)
        list1.append(x)
    y =sum(list1) 
    print(list1)
    print(y)
random_list_summer()    

#%% EXERCISE 6 FUNCTIONS
def Fibonacci():
    a = 0
    b = 1
    for i in range(5):
        print(a)
        c = a + b
        a = b
        b = c
    
Fibonacci()
#%% EXERCISE 7 FUNCTIONS
my_list= [*range(5)] 
for x in my_list:
    if x % 2 == 0:
        y = lambda x: x**2
        print(y(x))
   # else:
    #    print('you entered an odd number')


#%% EXERCISE 1 CLASSES AND OBJECTS
class Animal():
    def __init__(self, legs):
        self.legs = legs
        print("Animal object was created")
    
    def runs(self):
        print('Runnig started')

x = Animal(4)
x.count_legs()
print(x.return_legs())
print("The number of legs is:",x._Animal__legs)
x.runs()


#%% EXERCISE 2 CLASSES AND OBJECTS
class Animal():
    def __init__(self, legs):
        self.__legs = legs
        #print("Animal object was created")
    
    def runs(self):
        print('Runnig started')
        
    def count_legs(self):
        print("The number of legs is:", self.__legs)
        
    def return_legs(self):
        return self.__legs
    
x = Animal(4)
print("The number of legs is:",x._Animal__legs)
x.runs()    
        


#%% EXERCISE 3 CLASSES AND OBJECTS
class Animal():
    def __init__(self, legs):
        self.__legs = legs
        #print("Animal object was created")
    
    def runs(self):
        print('Runnig started')
        
    def count_legs(self):
        print("The number of legs is:", self.__legs)
        
    def return_legs(self):
        return self.__legs

            
    
x = Animal(4)
print("The number of legs is:",x._Animal__legs)
x.runs()    


#%% EXERCISE 4 CLASSES AND OBJECTS
class Animal():
    def __init__(self, legs):
        self.__legs = legs
        #print("Animal object was created")
    
    def runs(self):
        print('Runnig started')
        
    def count_legs(self):
        print("The number of legs is:", self.__legs)
        
    def return_legs(self):
        return self.__legs
    
class Dog(Animal):
    def __init__(self, legs,name):
        super().__init__(legs)
        #Animal.__init__(legs,name)
        
        self.__name = name
    
    def bark(self):
        print('woof woof')
            
    
x = Dog(4,'Sam')
print("The number of legs is:",x._Dog__name)
print("The number of legs is:",x._Animal__legs)
x.bark()
#x.runs()    
