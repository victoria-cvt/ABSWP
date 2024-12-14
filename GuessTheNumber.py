import random
secret_number = random.randint(1, 20)
print("im thinking of a number between 1 and 20.")

for guessesTaken in range(1,7):
    print("take a guess: ")
    guess = int(input())
    if guess < secret_number:
        print("too low")
    elif guess > secret_number:
        print('too high')
    else:
        break
if guess == secret_number:
    print("good job! you guesses in: " + str(guessesTaken)+'guesses')
else:
    print('nope, the number i was thinking was'+str(secret_number))
