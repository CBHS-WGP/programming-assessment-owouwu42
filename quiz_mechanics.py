import math
#question answers defined
q1="3"
q2="1"
q3="4"
q4="4"
q5="2"



questionnum=1
points=0
answer_list=[1,2,3,4]

def questions(): 
    global qu
    qu=("which option contains the letter a?")
    global qa
    qa=q1
    global opt
    opt=("1.c    "
         "2.c    "
         "3.a    "
         "4.c    ")        
    if questionnum==2:
        qu=("which option is option 1?")
        qa=q2
        opt=("1. "
             "2. "
             "3. "
             "4. ")
    elif questionnum==3:
        qu=("the answer is 4")
        qa=q3
        opt=("1. "
             "2. "
             "3. "
             "4. ")
    elif questionnum==4:
        qu=("it's still 4")
        qa=q4
        opt=("1. "
             "2. "
             "3. "
             "4. ")
    elif questionnum==5:
        qu=("it's two now")
        qa=q5
        opt=("1. "
             "2. "
             "3. "
             "4. ")





questions()

#answer error message defined
anserror=("please enter 1, 2, 3, or 4")
win=('~~~~CORRECT~~~~         ')
loss=("~~~~Wrong~~~~ Better luck next time!   ")

while questionnum<6:
    questions()
    print(qu)
    print(opt)
    ans=input()
    if ans=="1" or ans=="2" or ans=="3" or ans=="4":
        if ans==qa:
            points=points+1
            print(win, 'Points: {}' .format(points))
            questionnum=questionnum+1
        else:
            print(loss, 'Points: {}' .format(points))
            questionnum=questionnum+1
    else:
        print(anserror)
        
print("end")