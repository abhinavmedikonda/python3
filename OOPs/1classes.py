class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"
    def fullname(self):
        return f"{self.first} {self.last}"

a = Employee('abhi', 'nav', 150000)
b = Employee('test', 'user', 99999)

print(a)
print(a.email)
print(Employee.fullname(a))
print(b.email)
print(b.fullname())