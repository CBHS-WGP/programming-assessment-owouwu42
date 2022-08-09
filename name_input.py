#importing math
import math

#printing initial name request
print("please enter your name:")

#defining name error
nameerror=("please enter your name:")

#showing input
name=input()
while name.isnumeric() or name=="":
   print(nameerror)
   name=input()
   
#final name confirmation
print("hello ", name)