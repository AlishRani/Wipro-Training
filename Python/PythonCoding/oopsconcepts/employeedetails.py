class  EmployeeDetails:
    def __init__(self):
        self.empno = 0
        self.ename = ' '
        self.basic_pay = 0.0
        self.da = 20.0
        self.hra = 10.0
        self.pf = 5.5


    def calculate_allowence(self):
        allowence=(self.basic_pay * self.da /100) +(self.basic_pay *self.hra/100)
        return allowence

    def calculate_deduction(self):
        deduction=(self.basic_pay *self.pf /100)
        return deduction

    def calculate_netsel(self):
        netsel=self.basic_pay + self.calculate_allowence() -self.calculate_deduction()
        return netsel