qa=0
#question answers defined
q1=3
q2=1
q3=4
q4=4
q5=2

qu=("")

questionnum=1
points=0
answer_list=[1,2,3,4]

def questions(): 
    if questionnum==1:
        qu=("which option contains the letter a?")
        qa=q1
        opt=("1. "
             "2. "
             "3. "
             "4. ")
    elif questionnum==2:
        qu=("")
        qa=q2
        opt=("1. "
             "2. "
             "3. "
             "4. ")
    elif questionnum==3:
        qu=("")
        qa=q3
        opt=("1. "
             "2. "
             "3. "
             "4. ")
    elif questionnum==4:
        qu=("")
        qa=q4
        opt=("1. "
             "2. "
             "3. "
             "4. ")
    elif questionnum==5:
        qu=("")
        qa=q4
        opt=("1. "
             "2. "
             "3. "
             "4. ")


#answer error message defined
anserror=("please enter 1, 2, 3, or 4")
win=("~~~~CORRECT~~~~         Points: ", (points))
loss=('~~~~Wrong~~~~ Better luck next time!   The correct answer was: ', (qa), '   Points: ', (points))

questions()
while questionnum<=6:
    questions()
    print(qu)
    ans=input()
    if ans==1 or 2 or 3 or 4:
        if ans==qa:
            print(win)
            points=pounts+1
            questionnum=questionnum+1
        else:
            print(loss)
            questionnum=questionnum+1
    else:
        print(anserror)
        
