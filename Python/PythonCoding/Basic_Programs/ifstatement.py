"""
Date: 22-04-2026
Des: working on various is statement
"""


#Big2

'''num1=int (input('Enter a number'))
num2=int (input('enter another number'))

if num1==num2:
    print('both are equal')

elif num1>num2:
    print(num1,'is big')
else:
    print(num2,'is big')'''

#Big3

'''num1=int (input('Enter a number'))
num2=int (input('enter another number'))
num3=int (input('Enter 3rd number'))

if num1==num2 and num2==num3:
    print('All values are equal')
elif num1>num2 and num1>num3:
    print(num1,'num1 is biggest')
elif num2>num1 and num2>num3:
    print(num2,'num2 is biggest')
else:
    print(num3,'num3 is biggest')'''

#Weekdays

ch=int(input('Enter a number bet 1to7'))

match(ch):
    case 1:
        print('Monday')
    case 2:
        print('Tue')
    case 3:
        print('Wed')
    case 4:
        print('thrusday')
    case 5:
        print('fri')
    case 6:
        print('sat')
    case 7:
        print('sun')
    case _:
        print('invalid value')

