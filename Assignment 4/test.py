"""Personal Project 2020: Cara Lee 1081476"""

print("Welcome to Cara's Game!")
user = input("Please enter your name: ")                                        # Asks user for name
print("\nHi "+str(user)+" enter the number next to your selection")             # Menu: To view instructions or play
print("1. Read Instructions")
print("2. Play")
menu = int(input("Enter your election: "))                                      # Asks user to choose one
if menu == 1:                                                                   # Print instruction if they chose so
    print("\nInstructions: The user must collect all 4 essential "
          "items from various rooms to escape the house. The user does so by correctly answering questions")

questions = ["What are chips made of", 2, 3, 4, 5, 6, 7, 8, 9, 10]              # list of questions, choices & answers
choices = [["potato", "tomato", "cheese", "sausage"], "2", "3", "4", "5", "6", "7", "8", "9", "10"]
answers = ["potato", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

correct = 0                                                                     # variable to track players score
i = 0                                                                           # variable to iterate through questions

print("\nPart 1: Multiple-Choice-Questions")

while correct < 6 and i < 10:                                                   # keep giving questions till they get 6 right, or run out of questions
    print("\nQuestion "+str(i+1)+": "+str(questions[i]))                        # prints question
    print("Here are your choices: ")
    for k in range(len(choices[i])):                                            # prints choices
        print(str(k+1)+": "+choices[i][k])
    x = input("Please enter your answer: ")                                     # asks user to input answer
    if x == answers[i]:                                                         # checks if answer matches
        print("Your answer was correct")
        correct += 1                                                            # iterate score +1
    else:
        print("Your answer was incorrect")                                      # else answer is incorrect
    i += 1                                                                      # iterate question variable

if correct < 6:                                                                 # check if user lost (<6 correct answers)
    print("\n Soz mate you lose")
    exit()                                                                      # quit game

questions_2 = ["Dogs have 4 legs", "Cats have 10 eyes", 3, 4, 5, 6, 7, 8, 9, 10] # list of questions, answers (as binary)
answers_2 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

correct_2 = 0                                                                   # variable to track players score
j = 0                                                                           # variable to iterate through questions

print("\nPart 2: True or False")

while correct_2 < 6 and j < 10:                                                 # keep giving questions till they get 6 right, or run out of questions
    print("\nQuestion "+str(j+1)+": "+str(questions_2[j]))                      # print question
    x = input("Please enter True or False: ")                                   # ask user for answer
    if answers_2[j] == 0 and x == "false" or answers_2[j] == 0 and x == "False":# if correct answer is 0, check for false
        print("Your answer was correct")
        correct_2 += 1                                                          # iterate score +1
    elif answers_2[j] == 1 and x == "true" or answers_2[j] == 1 and x == "True":# if correct answer is 1, check for true
        print("Your answer was correct")
        correct_2 += 1                                                          # iterate score +1
    else:
        print("Your answer was incorrect")                                      # else answer is incorrect
    j += 1                                                                      # question iterator variable +1

if correct_2 < 6:                                                               # check if user lost (<6 correct answers)
    print("\n Soz mate you lose")
    exit()                                                                      # quit game

else:                                                                           # else user wins
    print("\n Congrats, you win!")
    exit()                                                                      # quit game