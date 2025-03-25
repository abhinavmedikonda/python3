class employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullname(self):
        return f"{self.first} {self.last}"

class developer(employee):
    compensation_rate = 1.1

    def __init__(self, first, last, pay, programming_language='Python'):
        super().__init__(first, last, pay)
        self.programming_language = programming_language

class manager(employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        print(f'employees under manager {self.fullname()}:')
        for emp in self.employees:
            print(f'--> {emp.fullname()}')

# print(help(developer))

a = developer('abhi', 'nav', 150000)
b = employee('test', 'user', 99999)
c = manager('the', 'boss', 90000, [a])
c.add_employee(b)
c.print_employees()
print(a.email)
print(b.email)
print()
print(isinstance(a, employee))
print(isinstance(a, manager))
print(isinstance(a, developer))
print()
print(issubclass(employee, manager))
print(issubclass(manager, employee))
print(issubclass(developer, manager))