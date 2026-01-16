from abc import ABC, abstractmethod

# ABC must be inherited to create interface
class IEmployee(ABC): # interface
    @abstractmethod
    def email(self):
        pass

    @abstractmethod
    def fullname(self):
        pass

# ABC must be inherited to create abstract class, thats done in iemployee
class Employee(IEmployee): # abstract class
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    @abstractmethod
    def fullname(self):
        pass

class developer(Employee):
    def __init__(self, first, last, prog_lang='python'):
        super().__init__(first, last)
        self.prog_lang = prog_lang

    def fullname(self):
        return f"{self.first} {self.last}"

a = developer('abhi', 'nav', 150000)
print(a.fullname())