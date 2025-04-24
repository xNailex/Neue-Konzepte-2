solution = 25
tries = 0
while tries <= 4:
    guess = (input("Please enter your guess: "))

    if guess.isdigit():
        guess = int(guess)
    else:
        print("Invalid input. Please enter a number.")
        continue

    if guess < solution:
        print("Too low! Try again.")
        tries += 1
    elif guess > solution:
        print("Too high! Try again.")
        tries += 1
    else:
        print("Congratulations! You guessed the correct number.")
        break