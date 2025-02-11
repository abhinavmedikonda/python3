class employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class salary_employee(employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary
    
    def calculate_paycheck(self):
        return self.salary/52

class horuly_employee(employee):
    def __init__(self, fname, lname, hours, rate):
        super().__init__(fname, lname)
        self.hours = hours
        self.rate = rate
    
    def calculate_paycheck(self):
        return self.hours*self.rate


class commission_employee(salary_employee):
    def __init__(self, fname, lname, salary, sales, rate):
        super().__init__(fname, lname, salary)
        self.sales = sales
        self.rate = rate
    
    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_commision = self.sales * self.rate
        return regular_salary + total_commision