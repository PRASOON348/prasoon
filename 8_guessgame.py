secret_number = 8
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess_count += 1
    guess = int(input("GUESS:"))
    if guess == secret_number:
        print("you win!")
print("you lose!")
