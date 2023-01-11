# first we make a skeleton structure with just the names of modules
# that we fill in later

# ------------------
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print("------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D)").upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    
    display_score(correct_guesses, guesses)
    
# ------------------
def check_answer(answer, guess):
    
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG!")
        return 0
    
# ------------------
def display_score(correct_guesses, guesses):
    print("------------------")
    print("RESULTS")
    print("------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
# ------------------
def play_again():
    
    response = input("Do you want to play again? (yes or no): ").upper()
    
    if response == "YES":
        return True
    else:
        return False
    
# ------------------

# for the questsions and answers we can use a dictionary
# first the questsions
questions = {
    "Who created Python: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the earth round?: ": "A"
}

# and the options, we use a 2D list
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1997", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. It's donut shaped"]]

new_game()

while play_again():
    new_game()
print("BYE DUDE")