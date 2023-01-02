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






                      
        
    
    
    
                        
                           
                            