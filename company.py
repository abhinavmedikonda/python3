from employee import employee, horuly_employee, salary_employee, commission_employee

class company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        print('Current Employees:')
        for item in self.employees:
            print(item.fname, item.lname)
        print('------------------------')

    def pay_employees(self):
        print('Employee Payments:')
        for item in self.employees:
            print('Paycheck for:', item.fname, item.lname)
            print(f'Amount: ${item.calculate_paycheck():,.2f}')
            print('------------------------')

def main():
    my_company = company()

    emp1 = salary_employee('fname', 'lname', 50000)
    my_company.add_employee(emp1)
    emp2 = horuly_employee('sdfg', 'yhtyh', 40, 50)
    my_company.add_employee(emp2)
    emp3 = commission_employee('frds', 'hgtb', 30000, 5, 200)
    my_company.add_employee(emp3)

    my_company.show_employees()
    my_company.pay_employees()

main()