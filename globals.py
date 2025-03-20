import sys

x = """
awesome
"""
print(sys.version)

def funcA():
  # using new local variable
  x = "excellent"
  print("funcA")

def funcB():
  # using global variable without extra decleration
  print("funcB")
  print(x)

def funcC():
  # using global scope variable
  global x
  x = "fentastic"
  print("funcC")
  

def myFunc():
  print("python is", x)

myFunc()
funcA()
myFunc()
funcB()
myFunc()
funcC()
myFunc()