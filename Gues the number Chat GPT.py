#This code is created by Chat GPT
while(1):  #for infinite fun
    import random # for selecting number randomly

    def guess_the_number(): # creating a user defined function
        secret_number = random.randint(1, 100) #limits
        attempts = 0

        print("Welcome to the Number Guessing Game!")
        print("I've selected a number between 1 and 100. Try to guess it.")

        while True:
            user_guess = int(input("Your guess: "))
            attempts += 1

            if user_guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif user_guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

    if __name__== "__main__":
        guess_the_number() #function call
