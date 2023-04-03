def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("......................")
        print(key)

        for i in options[question_num-1]:
            print(i)

        guess = input("Enter (A, B, or C): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += Check_answer(questions.get(key), guess)

        question_num += 1

    display_score(correct_guesses, guesses)


def Check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def display_score(correct_guesses, guesses):
    print("....................................")
    print("Results")
    print("....................................")
    print("Answers: ", end="")

    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is:   "+str(score)+"%")

def play_again():
    response = input("Play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

questions = {
    "What is the color of water?: " : "A",
    "Capital of USA?: " : "B",
    "Capital of Nigeria?: " : "C",
}

options =[
    ["A. colorless", "B. Purple", "C. Yellow"],
    ["A. NY", "B. DC", "C. TX"],
    ["A. NY", "B. DC", "C. Abj"]
]

new_game()

while play_again():
    new_game()

print("Goodbye!")