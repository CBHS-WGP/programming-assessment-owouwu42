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
                                 ::::::::::: :::::::::::::::::::::::
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
    
#set loading screen to false
    
loading=False
    
#define error message
error=("Press ENTER to begin")
    
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
    print(error)
    start=input()   
    
#loading trigger
while start=="":
    print("loading...")
    loop=0
    print("loading..")
    loop=0
    print("loading.")
    loop=0

