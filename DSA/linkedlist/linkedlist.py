class sll:
    def __init__(self, data=None):
        self.data = data
        self.next: "sll" = None

class dll:
    def __init__(self, data=None):
        self.data = data
        self.prev: "dll" = None
        self.next: "dll" = None
    