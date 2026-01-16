class Employee:
    no_of_instances = 0 # class variable
    compensation_rate = 1.04 # class variable

    def __init__(self, first, last, pay):
        Employee.no_of_instances += 1
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_compensation(self):
        self.pay = int(self.pay * self.compensation_rate)

a = Employee('abhi', 'nav', 150000)
b = Employee('test', 'user', 99999)

a.compensation_rate = 1.05 # instance variable
print(a.compensation_rate)
print(b.compensation_rate)
print(Employee.compensation_rate)
print(Employee.no_of_instances)

print(a.__dict__)
print(Employee.__dict__)
