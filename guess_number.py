import random

lower_bound = 0
upper_bound = 10
max_attempts = 5

secret_number = random.randint(lower_bound,upper_bound)

name = input("Hi bro! \nWhat is your name? ")

def get_guess():
    while True:
        try:
            guess = int(input(f"Please enter a number between {lower_bound} and {upper_bound} : "))
            
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print("Invalid input. please enter a number within the specifid range.")
        except ValueError:
            print("Invalid input.please enter a valid number.")

def check_guess(guess,secret_number):
     if guess == secret_number:
         return "Correct"
     elif guess > secret_number:
         return "Too high"
     else:
         return "Too low"
     
def play_game():
    attempts = 0
    won = False
    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess,secret_number)

        if result == "Correct":
            print(f"Conguratulation {name.title()}! You guessed secret number {secret_number} in {attempts} attempts. ")
            won = True
            break
        else:
            print(f"{result}. try again.")
    if not won:
        print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")        

if __name__ == "__main__":
    print(f"Wellcom {name.title()} to the guessing number game.")


    play_game()

   
    
    


                

        

