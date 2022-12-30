#%% EXERCISE1 :  AMSTRONG NUMBER
a ='153'

for i in a:
    print('i is equal to:',i,'and type b is ',type(i))
    b = int(i)
    print('b is equal to: ',b,'and type b is ',type(b))
print(i)
#%% EXERCISE1 :  AMSTRONG NUMBER
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
#%% EXERCISE1 :  AMSTRONG NUMBER
x = input('Enter a number :')
c = 0
d = 0
b = len(x)
for i in x:
    c = int(i) ** b
    #print(c)
    d = c + d
print(d)
if d == int(x):
    print(x,' is an amstrong number')
else:
    print(x,' is not an amstrong number')
        
    
    
    
    