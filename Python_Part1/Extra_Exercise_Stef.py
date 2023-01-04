#%% EXERCISE1 RETHINK ABOUT A SHORTER SOLUTION
time_first = int(input('Enter time one: '))
time_second = int(input('Enter time two: '))
time_third = int(input('Enter time three: '))
def myfunction(a,b,c):
    total = a + b + c
    minutes = round(total / 60)
    seconds = total % 60
    if seconds < 10:
        x = print(f'The time taken in format MINUTE:SECOND is {minutes}:0{seconds}')   
    else:
        x = print(f'The time taken in format MINUTE:SECOND is {minutes}:{seconds}') 
    return x
myfunction(time_first,time_second,time_third)

#%% EXERCISE2 RETHINK ABOUT A SHORTER SOLUTION ---------------I HAVE TO COME BACK TO THIS
a = int(input('Enter the number x: '))
if a % 2 == 0:
    bonus1 = 1
elif a % 5 == 0:
    bonus1 = 2
else:
    bonus1 =0
def myfunction(x,bonus1):            
            if x <= 100:
                bonus2 = 5
                total_bonus = bonus1 + bonus2
                total_point = x+bonus1+bonus2
            elif (x > 100) and (x <= 1000):
                bonus2 = x*0.2
                total_bonus = bonus1 + bonus2
                total_point = x+bonus1+bonus2
            elif x > 1000:
                bonus2 = x*0.1
                total_bonus = bonus1 + bonus2
                total_point = x+bonus1+bonus2
            return print('the total bonus is: ',total_bonus,'and the total points are: ',total_point)
myfunction(a,bonus1)

   
#%% EXERCISE3 SOLUTION 2 SHORT VERSION WORKIN WELL
a = str(input('Enter the season: ').lower())
b = int(input('Tnter the number of people: '))
dict1 = {'spring' : 3000,'summer': 4200,'autumn': 4200 ,'winter': 2600}
#list2 = [3000,4200,4200,2600]
def seasons(season,people):
    for x in dict1.keys():
        if season == x and season != 'autumn':
            price1 = dict1[x]
            if people % 2 == 0:
                discount2 = 0.05
                if people <= 6:
                    discount = 0.1
                    final_price = price1 - (price1 * discount) - (price1 * discount2)
                elif people in range(7,12):
                    discount = 0.15
                    final_price = price1 - (price1 * discount) - (price1 * discount2)
                elif people > 11:
                    discount = 0.25
                    final_price = price1 - (price1 * discount) - (price1 * discount2)
            else:
                if people <= 6:
                    discount = 0.1
                    final_price = price1 - (price1 * discount)
                elif people in range(7,12):
                    discount = 0.15
                    final_price = price1 - (price1 * discount)
                elif people > 11:
                    discount = 0.25
                    final_price = price1 - (price1 * discount)
                    
        elif season == 'autumn':
            price1 = 4200
            if people <= 6:
                discount = 0.1
                final_price = price1 - (price1 * discount)
            elif people in range(7,12):
                discount = 0.15
                final_price = price1 - (price1 * discount)
            elif people > 11:
                discount = 0.25
                final_price = price1 - (price1 * discount)
            
          #else:
           # print('enter the correct season')
 

    return print('The final price is: ',final_price,'$')
seasons(a,b)          


#%% EXERCISE4  WORKING WELL SOMEHOW
#b = 0
list1 = []
while True:
    c = 0
    x = input('enter the steps: ').capitalize()
    if str(x) == 'Going home':
        print(x)
        print('Today you did not reach your goal')
        break
    list1.append(int(x))
    print(list1)
    for a in range(len(list1)):
        b = list1[a]
        c += b
    print(c)
    if c >= 10000:
        print('Good job Ana you reached 10 000 steps')
        break





#%% EXERCISE5  WORKING VERY VERY WELL
e = int(input('Enter the first number: '))
f = int(input('Enter the second number: '))
def fibonacci(x,y):
    a = 0
    b = 1
    list1 = []
    for d in range(0,y):
            
                c = a + b
                a = b
                #b = c
                
                if a in range (x+1,y):
                    #print(c)
                        list1.append(a)
                b = c
    return print(list1)    
fibonacci(e, f)


#%% EXERCISE 6 WORKING WELL SOLUTION VERY VERY WELL
username = input('Enter your username: ')
password = input('Enter your password: ')
special = '!@#$%^'
if len(password) < 8:
    print('Password INVALID')
else:
    if username.lower() in password.lower():
        print('Password INVALID')
    else:
        a = 0
        b = 0
        c = 0
        for i in password:
            
            if i.isupper():
                a = a + 1
            
                
            if i.isnumeric():
                b = b + 1
            
            
            if i in special:
                c = c + 1
           
        
        if (a != 0) and (b != 0) and (c != 0):
            print('Password OK')
        else:
            print('Password INVALID')
            



     


#%%
list1 = [ 5,3,10 ]
list1.sort()
x = len(list1)
list2 = []
for i in range(list1[0],list1[x-1]):
     if i not in list1:
         #print(a)
         list2.append(i)
print(list2)  
  
    