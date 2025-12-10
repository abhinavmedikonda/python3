class sll:
    def __init__(self, data):
        self.data = data
        self.next: "sll" = None

class dll:
    def __init__(self, data):
        self.data = data
        self.previous: "dll" = None
        self.next: "dll" = None
    