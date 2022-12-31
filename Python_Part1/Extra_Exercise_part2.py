#%% EXERCISE1 :  AMSTRONG NUMBER
a ='153'
for i in a:
    print('i is equal to:',i,'and type b is ',type(i))
    b = int(i)
    print('b is equal to: ',b,'and type b is ',type(b))
print(i)
#%% EXERCISE1 :  
x = input('Enter a number :')
c = 0
d = 0
b = len(x)
for i in x:
    c = int(i) ** b
    print(c)
    d = c + d
print(d)
if d == int(x):
    print(x,' is an amstrong number')
else:
    print(x,' is not an amstrong number')
#%% EXERCISE1 :  VERY WORKING SOLUTION
x = input('Enter a number :')
c = 0
d = 0
b = len(x)
for i in x:
    c = int(i) ** b
    #print(c)
    d = c + d
#print(d)
if d == int(x):
    print(x,' is an amstrong number')
else:
    print(x,' is not an amstrong number')
        




#%% EXERCISE2 :  DETERMINE WEITHER A SENTENCE IS A PANGRAM OR NOT
#x = input('Enter your sentence:')
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
alphabet = alphabet.lower()
alpha2 = list(alphabet)
x = input('Enter your sentence: ')
x = x.lower()
x = x.replace(" ","")
#for a in x:
for a in range(len(x)):
    for i in range(len(alphabet)):
        i = 0
        first = alphabet[i]
        if first == x[a]:
            #print('This is a pagram sentence')
            
            i = i + 1
            first = alphabet[i]
            if i == len(alphabet):
                break
       
                print('this is a pagnam')
            else:
                print('This is not')
             
 
#%% EXERCISE2 :
#x = input('Enter your sentence:')
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
alpha2 = list(alphabet)
x = input('Enter your sentence: ')
#for a in x:
for a in x:
    for i in range(len(alphabet)):
        first = alphabet[i]
        if first != a:
            print('This is not')
           
#%% EXERCISE2 :  VERY WORKING WELL SOLUTION
#x = input('Enter your sentence:')
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
alphabet = alphabet.lower()
alpha2 = list(alphabet)
x = input('Enter your sentence: ')
x = x.lower()
x = x.replace(" ","")
list1 = []
#for a in x:
for a in alphabet:
    for i in range(len(x)):
        
        if a == x[i]:
            if a not in list1:
                list1.append(a)
            
if len(list1) == 26:
    print('this is a pagnant sentence')
else:
    print('this is not a pagnant sentence')
    



#%% EXERCISE3 : TAKE A NESTED LIST AND RETURN A SINGLE FLATTENED LIST WITH ALL VALUES EXCEPT NULL
x = [1,[2,3,None,4],[None],5]
list1 = []
list2 = []
for i in x:
    a = str(i)
    if len(a) == 1:
        list1.append(a)
    if len(a) > 1:
        for b in a:
            list1.append(b)
for c in list1:
    if type(c) == int:
        list2.append(c)
print(list2)     
        
#%% EXERCISE3 :
x = 3
if type(x) == int:
    print(x,'is an integer')
#%% EXERCISE3 :
x = [1,[2,3,None,4],[None],5]
list1 = []
list2 = []
for i in x:
    a = str(i)
    if len(a) == 1:
        list1.append(a)
    if len(a) > 1:
        for b in a:
            list1.append(b)
for c in list1:
    print(type(c))
#%% EXERCISE3 :
x = [1,[2,3,None,4],[None],5,6]
list1 = []
for i in x:
    #a = str(i)
    if type(i) == int:
        list1.append(i)
    if type(i) == list:
        for b in i:
            if type(b) == int:
                list1.append(b)
#for c in list1:
print(list1)
#%% EXERCISE3 : IT IS REALLY WORKING VERY VERY WELL
x = [1,[2,3,None,4],[None],5,6,'y',[1,2,'as',None]]
def myfunction(sentence):
    list1 = []
    for i in x:
        #a = str(i)
        if type(i) != list and i != None:
            list1.append(i)
        if type(i) == list:
            for b in i:
                if type(b) != list and b != None:
                    list1.append(b)
    return list1
print(myfunction(x))






                      
        
    
    
    
                        
                           
                            