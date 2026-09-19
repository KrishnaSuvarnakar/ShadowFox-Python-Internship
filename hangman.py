words = {
    "python": "A popular programming language",
    "computer": "An electronic machine",
    "developer": "A person who creates software",
    "database": "A place where data is stored",
    "keyboard": "Used to type on a computer"
}

score = 0
total_attempts = 3

print("===== WORD GUESSING GAME =====")

for word, hint in words.items():

    attempts_left = total_attempts
    guessed = False

    print("\n-----------------------------")
    print("Question:")
    print("Hint:", hint)
    print("Word Size:", len(word), "letters")
    print("Total Attempts:", total_attempts)
    print("Attempts Left:", attempts_left)

    while attempts_left > 0:

        answer = input("\nEnter your answer: ").lower().strip()

        if answer == word:
            print("Correct! ✅")
            score += 1
            guessed = True
            break

        attempts_left -= 1

        if attempts_left > 0:
            print("Wrong answer! ❌")
            print("Attempts Left:", attempts_left)
        else:
            print("Wrong answer! ❌")
            print("No attempts left!")
            print("Correct answer:", word)

    if guessed:
        print("Moving to next question...")

print("\n=============================")
print("GAME OVER")
print("Your Score:", score, "/", len(words))
print("=============================")