from employeedetails import EmployeeDetails

#driver
eno = int(input('Emp no :'))
name = input('Emp name : ')
bp = float(input('basic pay : '))

employee = EmployeeDetails()
employee.empno = eno
employee.ename = name
employee.basic_pay = bp
print(' Emp no : ',employee.empno)
print('Emp name : ',employee.ename)
print('Basic Pay : ',employee.basic_pay)
print('Salary : ',employee.calculate_netsel())