import random
strikes = 0
while strikes < 3:
    coin = random.choice(["heads", "tails"])
    while True:
        guess = input("What is your guess? (Heads or Tails)\n")
        guess = guess.lower()
        if guess == "heads" or guess == "tails":
            break
        else:
            print("Bad input")
    if guess == coin:
        print("Correct")
        strikes = 0
    else:
        print("Incorrect")
        strikes = strikes + 1
    print("The coin was", coin)
    print("Incorrect guesses in a row", strikes)

print("Game over, 3 wrong answers in a row")