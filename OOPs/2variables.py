class employee:
    no_of_instances = 0 # class variable
    compensation_rate = 1.04 # class variable

    def __init__(self, first, last, pay):
        employee.no_of_instances += 1
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_compensation(self):
        self.pay = int(self.pay * self.compensation_rate)

a = employee('abhi', 'nav', 150000)
b = employee('test', 'user', 99999)

a.compensation_rate = 1.05 # instance variable
print(a.compensation_rate)
print(b.compensation_rate)
print(employee.compensation_rate)
print(employee.no_of_instances)

print(a.__dict__)
print(employee.__dict__)
