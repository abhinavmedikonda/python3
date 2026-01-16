class Employee:
    compensation_rate = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    @classmethod # overloading constructor
    def from_string(cls, str):
        first, last, pay = str.split('-')
        return cls(first, last, int(pay))

    def apply_compensation(self):
        self.pay = int(self.pay * self.compensation_rate)
    
    @classmethod
    def set_compensation_rate(cls, rate):
        cls.compensation_rate = rate

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

a = Employee.from_string('abhi-nav-150000')
b = Employee.from_string('test-user-99999')
print(a.email)
print(b.email)

Employee.set_compensation_rate(1.05)
print(a.compensation_rate)
print(Employee.compensation_rate)

import datetime
date = datetime.date(2023, 10, 8)
print(Employee.is_workday(date))
