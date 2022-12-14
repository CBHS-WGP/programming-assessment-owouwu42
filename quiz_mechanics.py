import math
#question answers defined
q1="3"
q2="1"
q3="4"
q4="4"
q5="2"
#answer error message defined
anserror=("please enter 1, 2, 3, or 4")
#win message
win=('~~~~CORRECT~~~~         ')
#loss message
loss=("~~~~Wrong~~~~ Better luck next time!   ")
#setting code to start with first question
questionnum=1
#setting the starting number of points to 0
points=0

#defining the questions and answers for each question
def questions_and_answers(): 
    #setting the vriables defined within the function to be global so that python shell still accepts them as defined variables.
    #setting initial value for the question which would start as question 1
    global question
    question=("which option contains the letter a?")
    #setting the answer to the answer for question 1
    global qa
    qa=q1
    #defining the question 1 answer options
    global opt
    opt=("1.c    "
         "2.c    "
         "3.a    "
         "4.c    ")        
    #checking which question the player is on and changing the question, answer, and answer options appropriately 
    if questionnum==2:
        question=("which option is option 1?")
        qa=q2
        opt=("1. "
             "2. "
             "3. "
             "4. ")
    #checking which question the player is on and changing the question, answer, and answer options appropriately
    elif questionnum==3:
        question=("the answer is 4")
        qa=q3
        opt=("1. "
             "2. "
             "3. "
             "4. ")
    #checking which question the player is on and changing the question, answer, and answer options appropriately
    elif questionnum==4:
        question=("it's still 4")
        qa=q4
        opt=("1. "
             "2. "
             "3. "
             "4. ")
    #checking which question the player is on and changing the question, answer, and answer options appropriately 
    elif questionnum==5:
        question=("it's two now")
        qa=q5
        opt=("1. "
             "2. "
             "3. "
             "4. ")

#checking the question number
while questionnum<6:
    #running function for defined answers and questions
    questions_and_answers()
    #printing the question and options
    print(question)
    print(opt)
    #user input
    ans=input()
    #making sure that the user has chosen one of the options
    if ans=="1" or ans=="2" or ans=="3" or ans=="4":
        #checking if the user was correct
        if ans==qa:
            #awarding the user a point
            points=points+1
            #displaying user's points
            print(win, 'Points: {}' .format(points))
            #changing the question number
            questionnum=questionnum+1
        else:
            print(loss, 'Points: {}' .format(points))
            questionnum=questionnum+1
    else:
        #prompting the user to try a valid input
        print(anserror)
        
#end message
print("end")