#%%
mylist = ["apple","banane","cherry",'apple']
print(mylist)
print(mylist[1:])
list1 = list((1,2,3,4,5))
print(list1)
if 10 in list1:
    print('Yes 10 is the the selected list')
else:
    print('10 deoes not extist in nthe list')
    
#%% REPLACING 2 ITEMS BY ONE VALUE
mylist[1:3] = ["watermelon"]
print(mylist)
#%% list looping using while loop
thislist = ["apple", "banana", "cherry"]
a = 0
while a in range(len(thislist)):
    print(mylist[a])
    a = a+1
#%% list looping using while loop
thislist = ["apple", "banana", "cherry"]
[print(a) for a in thislist]
    
#%% LIST COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for a in fruits:
    if 'a' in a:
        newlist.append(a)
print(newlist)

#%% LIST COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [a if a !='mango' else  'banana' for a in fruits ]
print(newlist)
#%% SORTING LIST
fruits = ["apple", "banana", "cherry", "kiwi", "mango", 'Aga']
fruits.sort(reverse = True)
list1 = [45,21,9,1]
list1.sort(reverse = True)
print(list1)
print(fruits)
#%% SORTING LIST
def myfunction(n):
    return abs(n-50)
list1 = [45,21,9,1,48]
list1.sort(key = myfunction)
print(list1)
#%% SORTING LIST
fruits = ["apple", "Banana", "cherry", "kiwi", "mango", 'aga']
fruits.sort(key = str.lower)
print(fruits)
#%% SORTING LIST
fruits = ["apple", "Banana", "cherry", "kiwi", "mango", 'aga']
fruits.reverse()
print(fruits)
#%% COPY LIST
list1 = ["apple", "Banana", "cherry", "kiwi", "mango", 'Agaa']
list2 = list(list1)
print(list1)
print(list2)
#%% JOINING LIST
list1 = ["apple", "Banana", "cherry", "kiwi", "mango", 'Agaa']
list2 = [1,2,3,4]
for a in list1:
    list2.append(a)
print(list2)
print(list1)
#%% JOINING LIST
list1 = ["apple", "Banana", "cherry", "kiwi", "mango", 'Agaa']
list2 = [1,2,3,4]
list1.extend(list2)
print(list1)


#%% TUPLES
tuple1 = ("apple", "Banana", "cherry", "kiwi", "mango", 'apple')
print(tuple1)
print(len(tuple1))
#%%
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#%% TUPLES
tupl1 =("apple", "Banana", "cherry", "kiwi", "mango", 'apple')
x = list(tupl1)
x[0] = 'mango'
tupl1 = tuple(x)
print(tupl1)
#%% TUPLES
tupl1 =("apple", "Banana", "cherry", "kiwi", "mango", 'apple')
x = ('aga',)
tupl1 += x
print(tupl1)
#%% TUPLES
tupl1 =("apple", "Banana", "cherry", "kiwi", "mango", 'apple')
x = list(tupl1)
x.remove('apple')
tupl1 = tuple(x)
print(tupl1)
#%% TUPLES
tupl1 =("apple", "Banana", "cherry", "kiwi", "mango", 'apple')
(*x,y,z) = tupl1
print(x)
print(y)
print(z)
#%% LOOP TUPLES
tupl1 =("apple", "Banana", "cherry", "kiwi", "mango", 'apple')
a = 0
while a <len(tupl1):
    print(tupl1[a])
    a = a + 1
#%% LOOP TUPLES
tupl1 =("apple", "Banana", "cherry", "kiwi", "mango", 'apple')
a = tupl1 * 2
print(a)
#%% LOOP TUPLES
tupl1 =("apple", "Banana", "cherry", "kiwi", "mango", 'apple')
tupl1.index('apple')
print(tupl1.index('apple'))


#%% SETS
set1 ={"apple", "Banana", "cherry", "kiwi", "mango", 'apple'}
print(set1)
#%% SETS
set1 ={"apple", "Banana", "cherry", "kiwi", "mango", 'apple'}
for a in set1:
    print(a)
#%% SETS
set1 ={"apple", "Banana", "cherry", "kiwi", "mango", 'apple'}
print('Banana' in set1)
#%% SETS
set1 ={"apple", "Banana", "cherry", "kiwi", "mango", 'apple'}
set1.add('Aga')
print(set1)
#%% SETS
set1 ={"apple", "Banana", "cherry", "kiwi", "mango", 'apple'}
set1.remove('apple')
print(set1)
#%% SETS
thisset = {"apple", "banana", "cherry"}
tropical = ("pineapple", "mango", "papaya")
thisset.update(tropical)
print(thisset)
#%% SETS
set1 ={"apple", "Banana", "cherry", "kiwi", "mango", 'apple'}
set1.discard('Apple')
print(set1)
#%% SETS
set1 ={"apple", "Banana", "cherry", "kiwi", "mango"}
x = set1.pop()
print(x)
print(set1)
#%% SETS
set1 ={"apple", "Banana", "cherry", "kiwi", "mango"}
set1.clear()
print(set1)
#%% SETS
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1 = set1.union(set2)
print(set1)
#%% SETS
set1 = {"apple", "Banana", "watermelon", "kiwi", "mango"}
set2 = {"apple", "lemon", "cherry", "Aga", "mango"}
set1.intersection_update(set2)
print(set1)
#%% SETS
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
#%% SETS
set1 = {"apple", "Banana", "watermelon", "kiwi", "mango"}
set2 = {"apple", "lemon", "cherry", "Aga", "mango"}
set3 = set1.intersection(set2)
print(set3)
#%% SETS
set1 = {"apple", "Banana", "watermelon", "kiwi", "mango"}
set2 = {"apple", "lemon", "cherry", "Aga", "mango"}
set1.symmetric_difference_update(set2)
print(set1)
#%% SETS
set1 = {"apple", "Banana", "watermelon", "kiwi", "mango"}
set2 = {"apple", "lemon", "cherry", "Aga", "mango"}
set3 = set1.symmetric_difference(set2)
print(set3)
#%% SETS
set1 = {"apple", "Banana", "watermelon", "kiwi", "mango"}
set2 = {"apple", "lemon", "cherry", "Aga", "mango"}
print(set1.issuperset(set2))


#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict1['year'])
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
print(len(dict1))
#%% DICTIONARIES
dict1 = dict(name = 'Julien' , age = 23 , country = 'Congo')
print(dict1)
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict1.get('year'))
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
a = dict1.keys()
b = dict1.values()
print(a)
print(b)
dict1['color'] ='red'
dict1['year'] = 2022
print(a)
print(b)
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = dict1.items()
print(x)
dict1['year'] = 2022
print(x)
dict1['color'] ='red'
print(x)
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
'Ford' in dict1.values()
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict1.update({'year' : 2022})
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict1)
dict1['color'] = 'red'
print(dict1)
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict1)
dict1.update({'color' : 'red'})
print(dict1)
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict1)
dict1.pop('brand')
print(dict1)
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict1)
dict1.popitem()
print(dict1)
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict1)
del dict1['model']
print(dict1)
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict1)
dict1.clear()
print(dict1)
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for a in dict1:
    print(a)
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for a in dict1:
    print(a , dict1[a])
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for a in dict1.keys():
    print(a)
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for a , b in dict1.items():
    print(a,b)
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict1)
dict2 = dict1.copy()
print(dict2)
#%% DICTIONARIES
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict1)
dict2 = dict(dict1)
print(dict2)
#%% DICTIONARIES
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
#%% DICTIONARIES
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)