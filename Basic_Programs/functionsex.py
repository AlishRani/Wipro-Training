#functions
'''def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
     return n1*n2

def div(n1,n2):
    pass


#driver

num1=int(input('enter a number'))
num2=int(input('enter a another number'))

res=add(num1,num2)
print('Add :',res)
res=sub(num1,num2)
print('sub :',res)
res=mul(num1,num2)
print('mul :',res)'''


#Arbitary

'''def fun(*a,**b):
    print(a)
    print(b)
fun(1,2,3, name="Alish")'''

#optional

'''def greet(name="guest"):
    print("Hello",name)
greet("Alish")
greet()'''

#Lambda

'''add=lambda a, b: a + b
print(add(2,3))'''

numbers=[1,2,3,4,5,6,7,8,9,10]
sq=lambda nums : [num * num for num in nums if num%2==0]
print(sq(numbers))





