#%% EXERCISE1 : AMSTRONG NUMBERS VERY WORKING SOLUTION
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
        

#%%
print('Hello')



             
 

           
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

#%%  EXERCISE 4
import math as m
the_list = [1,2,3,4,5,67]
the_list.sort()
search = 1
list1 = []
list2 = []
for i in the_list:
    middle_index = m.floor( (0 + len(the_list)) / 2)
    if the_list[middle_index] == search:
        print('The number you are searching for is: ',the_list[middle_index])
        
    elif the_list[middle_index] < search:
        middle_index = m.floor( (0 + (middle_index-1)) / 2)
        for a in range(0,middle_index+1):
           
            list1.append(a)
        if list1[middle_index] == search:
                print('The number you are searching for is: ',list1[middle_index])
            
    elif the_list[middle_index] > search:
        middle_index = m.floor((middle_index+1) + len(the_list) / 2)
        for b in range(middle_index,len(the_list)):
           
            list1.append(b)
        
        if list2[middle_index] == search:
                print('The number you are searching for is: ',list2[middle_index])
            
            
#%%  EXERCISE 4
import math as m
the_list = [1,2,3,4,5,67]
the_list.sort()
search = 1
list1 = []
list2 = []

middle_index = m.floor( (0 + len(the_list)) / 2)
if the_list[middle_index] == search:
            print('The number you are searching for is: ',the_list[middle_index])
            
elif the_list[middle_index] < search:
            middle_index = m.floor( (0 + (middle_index-1)) / 2)
            for a in range(0,middle_index+1):
               
                list1.append(a)
            if list1[middle_index] == search:
                    print('The number you are searching for is: ',list1[middle_index])
                
elif the_list[middle_index] > search:
            middle_index = m.floor((middle_index+1) + len(the_list) / 2)
            for b in range(middle_index,len(the_list)):
               
                list1.append(b)
            
            if list2[middle_index] == search:
                    print('The number you are searching for is: ',list2[middle_index])
                
                
#%%  EXERCISE 4
import math as m
the_list = [1,2,3,4,5,67]
the_list.sort()
x = len(the_list)
search = 1
list1 = []
list2 = []
newlist = []

middle_index = m.floor( (0 + x) / 2)
if the_list[middle_index] == search:
                print('The number you are searching for is: ',the_list[middle_index])
                
elif the_list[middle_index] > search:
                for a in range(0,middle_index):
                   
                    list1.append(the_list[a])
                newlist = list1.copy()
                middle_index = m.floor( (0 + (middle_index-1)) / 2)
                
                if newlist[middle_index] == search:
                        print('The number you are searching for is: ',list1[middle_index])
                    
elif the_list[middle_index] < search:
                for b in range(middle_index+1,x):
                   
                    list2.append(the_list[b])
                newlist = list2.copy()
                middle_index = m.floor(((middle_index+1) + x) / 2)
                
                if newlist[middle_index] == search:
                        print('The number you are searching for is: ',list2[middle_index])
                
            
#%%  EXERCISE 4
import math as m
the_list = [1,2,3,4,5,67]
the_list.sort()
x = len(the_list)
search = 1
list1 = []
list2 = []
newlist = []


middle_index = m.floor( (0 + x) / 2)
if the_list[middle_index] == search:
                print('The number you are searching for is: ',the_list[middle_index])        

elif the_list[middle_index] > search:
                for a in range(0,middle_index):
                   
                    list1.append(the_list[a])
                newlist = list1.copy()
                middle_index = m.floor( (0 + (middle_index-1)) / 2)
                
                if newlist[middle_index] == search:
                        print('The number you are searching for is: ',list1[middle_index])
                
#%%  EXERCISE 4
import math as m
the_list = [1,2,3,4,5,67]
the_list.sort()
x = len(the_list)
search = 1
list1 = []
list2 = []
newlist = []

def middle(the_list,search):
    if the_list[middle_index] == search:
                  return  print('The number you are searching for is: ',the_list[middle_index])
                      
        
def leftside(the_list,search):
    if the_list[middle_index] > search:
                    for a in range(0,middle_index):
                       
                        list1.append(the_list[a])
                    newlist = list1.copy()
                    middle_index = m.floor( (0 + (middle_index-1)) / 2)
                    
                    if newlist[middle_index] == search:
                            print('The number you are searching for is: ',list1[middle_index])
                        
    
 Maybe I sould be returning the index instead 
                        
                           

