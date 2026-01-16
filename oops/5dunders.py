class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def __repr__(self):
        return f"employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        return NotImplemented # to avoid throwing error, it can be checked in other class for implementation

    def __len__(self):
        return len(self.fullname())

a = Employee('abhi', 'nav', 150000)
b = Employee('test', 'user', 99999)

print(a)
print(a.__repr__())
print(a.__str__())
print()
print(repr(a))
print(str(a))
print()
print(a + b)
print(a.__add__(b))
print()
print(len(a))
print(a.__len__())