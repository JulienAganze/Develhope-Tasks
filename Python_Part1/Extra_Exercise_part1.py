#%% VARIABLES AND DATA TYPE
#%% Exercise1 MINE
names = ('Numa' , 'Tullio' , 'Anco')
surnames = ('Pomplio' , 'Ostilio' , 'Marzio')
list1 = [{'first name' : names[0], 'last name' : surnames[0]} ,
         {'first name' : names[1], 'last name' : surnames[1]} ,
         {'first name' : names[2], 'last name' : surnames[2]}]
result = zip(names, surnames)
print(list1)
#%% Exercise1 proposed
names = ('Numa' , 'Tullio' , 'Anco')
surnames = ('Pomplio' , 'Ostilio' , 'Marzio')
list1 = []
for name, surname in zip(names,surnames):
    list1.append({'name':name , 'surname': surname})
print(list1)
#%% Solution 2: list comprehension proposed
names = ('Numa' , 'Tullio' , 'Anco')
surnames = ('Pomplio' , 'Ostilio' , 'Marzio')
l = []
l = [{'name': name, 'surname': surname} for name, surname in zip (names, surnames)]
print(l)

#%% EXERCISE2 Mine
x = input('Enter your name:')
y = input('Enter your surname:')
a = input('Enter serial number:')
b = input('Enter grade for exam:')
z = {
     'name' : x,
     'surname' : y,
     'serial number' : int(a),
     'exam grade' : float(b)
     }
print(z)
#%% EXERCISE2 proposed
d = {'name': 'Pinco', 'surname': 'Pallino'} # defining the dictionary
d ['Serial number'] = 258115 # adding a key-value pair
d ['exams'] = [{' name ':' Bioinformatics', 'grade': 30}, {'name': 'Analysis',' grade ': 18}]
print(d)
# Solution 2: dict(assignment:mark)
d ['exams'] = {'Bioinformatics': 30, 'Analysis': 18}
print(d)



#%% CONDITIONALS
#%% Exercise1 MINE
a = 'A'
c = 'C' 
g = 'G' 
t = 'T'
x = input('Enter the nucleotide: ')
if x == a.lower() or x == a.upper():
    print('the complimentaryh nucleotide is',t)
elif x == t.lower() or x == t.upper():
    print('the complimentaryh nucleotide is',a)
elif x == c.lower() or x == c.upper():
    print('the complimentaryh nucleotide is',g)
elif x == g.lower() or x == g.upper():
    print('the complimentaryh nucleotide is',c)
else:
    print('Please enter A, C, G or T')
#%% Exercise1 PROPOSED
nucleotide = input ('Enter a nucleotide (A, C, G, T): ')
# Add check for correct input: no numeric, only a-c-g-t are accepted,
if nucleotide == 'A' or nucleotide == 'a':
    print ('T')
elif nucleotide == 'C' or nucleotide == 'c':
    print ('G')
elif nucleotide == 'G' or nucleotide == 'g':
    print ('C')
elif nucleotide == 'T' or nucleotide == 't':
    print ('A')
# solution to avoid the capitalization problem:
nucleotide = nucleotide.capitalize () # /upper() o check in lowercase only (lower())
#%% Exercise2 MINE
year = int(input('Enter the year: '))
leap = False
if (year % 4) == 0 and (year % 100) != 0:
    leap = True
    print(leap)
elif (year % 400) == 0:
    leap = True
    print(leap)
else:
    print(leap)
#%% Exercise2 PROPOSED
def is_leap(year):
    leap = False
    if year%4==0 and year%100!=0 :
        leap = True
    elif year%400 == 0:
        leap = True
    else:
        leap=False
    return leap
year = int(input())
print(is_leap(year))
    
#%% ITERATIONS 
#%% Exercise1 MINE
c = 0
for a in range(500):   
    c += a
print(c)
#%% Exercise1 MINE
list1=[]
for x in range(0,500):
    list1.append(x)
print(list1)
c = 0
for a in range(len(list1)):
    c = c + list1[a] 
    print(c)
#%% Exercise1 MINE
c = 0
while x in range(0,500):
    c = c + x
c
print(c)
#%% Exercise1 PROPOSED
# Solution 1
n=0
for i in range(0,500): # O(n)
    n += i
print(n)
#%% Exercise1 PROPOSED
# Solution 2
n = sum(range(0,500)) 
print(n)
#%% Exercise2 MINE
while True:
    x = str(input('Enter the string: ' ))
    print(x)
    print('The length of the string is', len(x))
    if x == 'exit':
        break

#%% Exercise2 PROPOSED
while True:
    line = input ('Enter a string: ').lower()
    if line == 'exit': # avoid issue with the capitalization
        break
    print(len(line))
#%% Exercise3 MINE
list1=[]
for x in range(20):
    list1.append(x)
    print(list1)
#%% Exercise3 MINE
import random
list1=[]
for x in range(20):
    list1.append(random.randint(0,100))
print(list1)
a = 0
b =0
for  i in range(0,len(list1)):
        if list1[i] % 2 == 0:
            a = a + 1
        if list1[i] > 70:
            b = b + 1
print('the number of even elements is',a)
print('the number of even elements is',b)
#%% Exercise3 PROPOSED
# Solution
import random
list_of_num = [random.randint(1,100) for _ in range (0,20)] # creating the list
# or
# list_of_num = []
# for _ in range(20):
# list_of_num.append(random.ranint(0,100))
even_num = []
count=0
for i in list_of_num:
    if i%2==0: # the number is even
        even_num.append(i)
    if i > 70:
        count +=1
print(f"Even numbers: {even_num}")
print(f"Count of numbers greater than 70: {count}")
#%% Exercise3 MINE AND VERY VERY VERY VERY GOOD SOLUTION
import random
list1=[]
for x in range(20):
    list1.append(random.randint(0,100))
print(list1)
a = 0
b =0
even_number = []
list2 = []
for  i in list1:
        if i % 2 == 0:
            a = a + 1
            even_number.append(i)
        if i > 70:
            b = b + 1
            list2.append(i)
print(even_number)
print('the number of even elements is',a)
print(list2)
print('the number of elements greater than 70 is',b)
#%% Exercise3 MINE
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort()
print('The sorted list: ',guests)
guests.reverse()
print('The reverse sorted list: ',guests)
#%% Exercise3 MINE   SORTED
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
sorted_guest = []
while guests:
    first = guests[0]
    for i in guests:
        if i < first:
            first = i
    print(first)
    sorted_guest.append(first)
    print(sorted_guest)
    guests.remove(first)
    print(guests)
#%% Exercise3 MINE REVERSE SORTED
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
sorted_guest = []
while guests:
    first = guests[0]
    for i in guests:
        if i > first:
            first = i
    print(first)
    sorted_guest.append(first)
    print(sorted_guest)
    guests.remove(first)
    print(guests)
#%% Exercise3 PROPOSED   SORTED
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort()
guests.sort(reverse = True)
#guests.reverse()
print(guests)


#%% EXERCISE1 FUNCTIONS MINE
import random
guests = []
for x in range(20):
    guests.append(random.randint(0,100))
def mymax(list1):
    while list1:
        first = list1[0]
        for i in list1:
            if i > first:
                first = i
        
        return first
print(guests)
print(mymax(guests))
#%% EXERCISE 1 FUNCTIONS PROPOSED
import random
list_of_num = [random.randint(1,100) for _ in range (0,20)]
def find_highest(aList):
    highest=aList[0]
    for element in aList:
        if element > highest:
            highest = element
    return(highest)
print(find_highest(list_of_num))
#%% EXERCISE2 FUNCTIONS MINE VERY CORRECT ALTERNATIVE
import random
list1 = []
for x in range(20):
    list1.append(random.randint(0,100))
def even(list2):
    list3 = []
    for x in list2:
        if x%2 == 0:
            list3.append(x)
            
    return list3
print(list1)
print(even(list1))
#%% EXERCISE2 FUNCTIONS PROPOSED
import random
list_of_num = [random.randint(1,100) for _ in range (0,20)] # creating the list
# Solution
def even_position (aList):
    even_pos=[]
    for i in range(0,len(aList)):
        if i%2==0:
            even_pos.append(aList[i])
    return even_pos
# Check
if __name__ == "__main__":
    print(even_position(list_of_num))
#%% EXERCISE2 FUNCTIONS MINE VERY CORRECT SOLUTION
import random
list1 = []
for x in range(20):
    list1.append(random.randint(0,100))
def even(list2):
    list3 = []
    for x in range(len(list2)):
        if x%2 == 0:
            list3.append(list2[x])
            
    return list3
print(list1)
print(even(list1))
#%% EXERCISE3 FUNCTIONS MINE
import random
x = random.randint(0,10)
L = lambda x : x + 2
print(x)
print(L(x))
#%% EXERCISE3 FUNCTIONS MINE
import random
x = int(input('Enter the variable: '))
L = lambda x : x + 2
print(x)
print(L(x))
#%% EXERCISE3 FUNCTIONS MINE

x = int(input('Enter the variable: '))
def myfunction(x):
    return lambda x : x + 2
print(x)
adding_2 = myfunction(x)
print(adding_2(x))
#%% EXERCISE3 FUNCTIONS PROPOSED
i = 8
L = lambda x : x + 2
print(L(i))