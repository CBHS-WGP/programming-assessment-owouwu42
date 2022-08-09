qa=0
qu=("ERROR")

def questions(): 
    if questionnum==1:
        qu=("which option contains the letter a?")
        qa=q1

#question answers defined
q1=3
q2=1
q3=4
q4=4
q5=2

questionnum=1
points=0
answer_list=[1,2,3,4]

#answer error message defined
anserror=print("please enter 1, 2, 3, or 4")
win=print("~~~~CORRECT~~~~         Points: ", (points))
loss=print("~~~~Wrong~~~~ Better luck next time!   The correct answer was: ", (qa), "   Points: ", (points))
while questionnum<6:
    exec(questions)
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