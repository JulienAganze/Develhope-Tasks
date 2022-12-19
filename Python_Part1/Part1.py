#%%Variables Exercise1
firstName='Mario'

#%%Variables Exercise2
age=25

#%%Variables Exercise3
sentence="Hello, I'm Mario!" 

#%%Variables Exercise4
amount=2.14

#%%Variables Exercise5
var_1=True
var_2=True
var_3=True


#%%Variables Exercise6
name='Mario'
variable=f'1my-first2_Name = {name}'
characters=['1','-','2']
for character in characters:
    variable = variable.replace(character, '')
#%%Variables Exercise7
"Hi,my name is John Doe"

"python"

#%%Variables Exercise8
a=2
b=3
c=4
print(a,b,c)
#%%Variables Exercise9
a = 12
b = 'Hello'
print(a, b)
c = a
a = b
b = c
print(a,b)

#%%Variables Exercise10
hello = 'Hello!'
name = 'Jhon Doe'
age = '40'
print(hello,'has lenght = ',len(hello))
print(name,'has lenght = ',len(name))
print(age,'has lenght  = ',len(age))
#%%Variables Exercise11 I should come back to this 
a = 'hello' #capitalize
a=a.capitalize()
b = 'tom' #uppercase
b=b.upper()
c = 'LAURA' #lowercase
c=c.lower()
question = 'How are you' #change o in e
question=question.replace('o','e')
age_question = 'How old are you?' #use the correct method to create a string for each word
age_question=age_question.split(' ')
print(a, b, c, question, age_question)

#%%Variables Exercise12
name='Julien'
age=12
hello = "Hello, {}. You are {}".format(name,age)
print(hello)
#%%Methods Exercise1 comme back to this too
print(type("Hello World"))
print(type(True))
print(type(False))
print(type(33))
print(type(24.5))
print(type(4+1j))
print(type(4j))
print(type(["lion", "monkey", "dog","fish"]))
print(type(("lion", "monkey", "dog","fish")))
print(type({"name" : "John", "surname" : "Doe", "age":22}))
print(type({"lion", "monkey", "dog","fish"}))

#%%Nethods Exercise2
num1 = 1.3
num2 = 2.3
num3 = 1j 
num4 = 1.4 
num5 = 1.5

num1=float(num1)
num2=int(num2)
num3=complex(num3)
num4=round(num4)
num5=round(num5)
print(num1,num2,num3,num4,num5)
print(type(num1),type(num2),type(num3),type(num4),type(num5))
#%%Methods Exercise3
num1 = 1122334455666

num1_str=str(num1)
len(num1_str)
num1_str[2]
num1_str[2:5]


