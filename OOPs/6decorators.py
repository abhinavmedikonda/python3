class employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(sef, name):
        first, last = name.split(' ')
        sef.first = first
        sef.last = last

    @fullname.deleter
    def fullname(self):
        print('delete name!')
        self.first = None
        self.last = None

a = employee('abhi', 'nav', 150000)
print(a.fullname)
print(a.email)

a.fullname = 'test user'
print(a.first)
print(a.email)

del a.fullname
print(a.first)