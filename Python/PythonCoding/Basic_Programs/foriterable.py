'''numbers=[11,22,98,54,63,45,20,45]

for number in numbers:
    print(number%10,end='\t')

    numbers=(11,22,98,54,63,45,20,45)

    for number in numbers:
        print(number%10,end='\t')'''


'''numbers={11,22,98,54,63,45,20,5}
for number in numbers:
    print(number%10,end='\t')'''

'''stud={'rno':101,'name':'AAA','city':'MMM'}

for stu in stud:
    print (stu)'''

stud={'rno':101,'name':'AAA','city':'MMM'}

for k,v in stud.items():
    print(k,'__',v)