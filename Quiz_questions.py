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
    question=("Which game number is Skyrim in the Elder Scrolls series?")
    #setting the answer to the answer (qa) for question 1 by pulling it from the previously defined answer numbers (q1)
    global qa
    qa=q1
    #defining the question 1 answer options (opt)
    global opt
    opt=("1. Elder Scrolls III        2. Elder Scrolls IV        3. Elder Scrolls V        4. Elder Scrolls VI")        
    #checking which question the player is on and changing the question, answer, and answer options appropriately 
    if questionnum==2:
        question=("Who was the head developer, producer, writer, and designer of The Elder Scrolls V: Skyrim?")
        qa=q2
        opt=("1. Todd Howard        2. Jeremy Soule        3. Emil Pagliarulo        4. Kurt Kuhlmann")
    #checking which question the player is on and changing the question, answer, and answer options appropriately
    elif questionnum==3:
        question=("What year was Skyrim released?")
        qa=q3
        opt=("1. 2013        2. 2018        3. 2016        4. 2011")
    #checking which question the player is on and changing the question, answer, and answer options appropriately
    elif questionnum==4:
        question=("What illicit drug are the Khajiit of Skyrim well-known for selling")
        qa=q4
        opt=("1. Giant water        2. Wabbajack        3. Groundwater hit        4. Skooma")
    #checking which question the player is on and changing the question, answer, and answer options appropriately 
    elif questionnum==5:
        question=("Who killed the high king and is almost to be excecuted in the 'unbound' intro before being interrupted by Aluin?")
        qa=q5
        opt=("1. Legate Rikke        2. Ulfric Stormcloak        3. Galmar Stone-Fist        4. Lydia Delphine")

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
print("                                                    GOOD JOB!!!!! you completed the quiz!")
print("                                                         your score was:   ", points,"/5")