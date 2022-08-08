import math
print("please enter your name:")
nameerror=("please enter your name:")

name=input()
while name.isnumeric() or name=="":
   print(nameerror)
   name=input()

print("hello ", name)