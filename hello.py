import sys, random

x = """
awesome
"""
print(sys.version)

def funcA():
  print("funcA")
  funcB()

def funcB():
  global x
  x = "fentastic"
  print("funcB")
#   funcA()

def funcC():
  print("funcC")

def myFunc():
  print("python is", x)

myFunc()
funcA()
myFunc()