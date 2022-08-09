#defining logo
def logo():
    print('''                                         :                 :
                                        ::     :           ::
                                       ::       :  :        ::
                                      ::::     ::.:::        ::
                                     ::::    ::::  :::       :::
                                    ::::          :::      ::::::
                                   :::::::       :::          ::::
                                  ::::          :::            ::::
                                 ::::::::    :  ::::           :::::
                                :::::::      :: ::::: ::  :::::::::::
                                ::::::::::    ::::::::::   ::::::::::
                                 ::::::::::: :::::::::::: ::::::::::
                                  :::::::::::::::::::::::::::::::::
                                   ::::::::::::::::::::::::::::::
                                    ::::::::  :  :::::  :: :::::
                                     ::::         :::   :   :::
                                      ::         :::        ::
                                       :::      :::        ::
                                        ::      ::        ::
                                         ::     ::       ::
                                          :      ::      :
                                                ::  .    
                                                 :: ::
                                                  :::
                                                   :
                            
''')
    
#define beginning error message
starterror=("Press ENTER to begin")
#importing math
import math
#printing initial name request
print("please enter your name:")
nameerror=("please enter your name")
    
#spacing
loop=0
while loop < 15:
    print("")
    print("")
    loop=loop+1

#title screen content
print("*****-------------------------------------------------------------------------------------------*****")
logo_print=logo()
print("                                                Skyrim:")
print("                                               The Quiz")
print("*****-------------------------------------------------------------------------------------------*****")
print("                                          Press Enter to begin.")

#more spacing
loop=0
while loop < 8:
    print("")
    print("")
    loop=loop+1
    
#initial chance to begin
start=input()

#error message trigger upon failure to start
while not start=="":
    print(starterror)
    start=input()   
    
#showing input
name=input()
while name.isnumeric() or name=="":
    print(nameerror)
    name=input()
    
#final name confirmation
print("hello ", name)