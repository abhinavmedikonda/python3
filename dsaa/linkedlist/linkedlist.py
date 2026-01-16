class Sll:
    def __init__(self, data=None):
        self.data = data
        self.next: "Sll" = None

class Dll:
    def __init__(self, data=None):
        self.data = data
        self.prev: "Dll" = None
        self.next: "Dll" = None
    