class employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"
    def fullname(self):
        return f"{self.first} {self.last}"

a = employee('abhi', 'nav', 150000)
b = employee('test', 'user', 99999)

print(a)
print(a.email)
print(employee.fullname(a))
print(b.email)
print(b.fullname())