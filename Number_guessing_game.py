import random 

def number_guessing_game():
    secret_number = random.randint(1,100)
    test = 0
    max_of_tests = 10
    
    
    print("Welcome to the Number Guessing Game !")
    print(f"I'm thinking a number between 1 and 100. You have {max_of_tests} times to guess.")


    while test < max_of_tests:
        try:
            guess = int(input("Enter you guess: "))
        except:
            print("Please enter a valid number.")
            continue
    
        test += 1
    
    
        if guess < secret_number:
            print("Too low !")
        elif guess > secret_number:
            print("Too high !")
        else:
            print(f"Congratulations! You guessed number {secret_number} in {test} times. ")
            break
    
        remaining = max_of_tests - test
        if remaining > 0:
            print(f"You have {remaining} time left.")
            
        if test == max_of_tests and guess != secret_number:
            print("Game over ! You lose ! Good luck next time.") 
        
        
    play_again = input("Are you want to play again ? (yes/no): ")
    if play_again.lower() == 'yes' or play_again.lower == 'y':
        number_guessing_game()
    else:
        print("Thanks for playing! Goodbye.")
                        
            
if __name__=='__main__':
    number_guessing_game()    
            
    