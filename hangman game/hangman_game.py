import os
import random 

def load_words(filename):
    with open(filename, 'r') as file:
        return [line.strip().lower() for line in file if line.strip()]
    
def load_scores():
    scores = {}
    if os.path.exists("scores.txt"):
        with open("scores.txt", 'r') as file:
            for line in file:
                if ":" in line:
                    name, score = line.strip().split(":")
                    scores[name.strip()] = int(score.strip())
    return scores

def save_scores(player_name, score):
    scores = load_scores()
    scores[player_name] = score
    with open("scores.txt", "w") as file:
        for name, sc in sorted(scores.items(), key=lambda x: x[1], reverse=True):
            file.write(f"{name}: {sc}\n")

def clear_scores():
    confirm = input("Are you sure you want to delete all points? (y/n): ").lower()
    if confirm == "y":
        open("scores.txt", "w").close()
        print("Deleted all scores.")
    else:
        print("Cancelled delete scores.")       
        
             
def show_leaderboard(top_n=10):
    scores = load_scores()
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print("\n LEADERBOARD: ")
    print("-" * 25)
    for idx, (name, score) in enumerate(sorted_scores[:top_n], start=1):
        print(f"{idx}. {name} - {score} points.")
    print("-" * 25)      
               
def play_game():
    won = False
    word_list = load_words("words.txt")
    word = random.choice(word_list)
    guessed_letters = []
    max_tries = 6        
    tries = 0
    score = 0
    
    scores = load_scores()
    
    while True:                    
        player_name = input("Enter your name: ").strip()    
        if player_name == "":
            print("The name is not left empty. Please enter your name.")
        elif player_name in scores:
            print("The name existed. Please choose another name.")
        else:
            break
    
    
    print(f"Welcome {player_name} to Hangman Game !")
    print("_" * len(word)) 
    
    
    while tries < max_tries:
        guess = input("Please enter 1 letter or 1 word: ").lower().strip()
        
        if not guess.isalpha():
            print("Please enter 1 letter or a valid word: ")
            continue
        
        if len(guess) > 1:
            if guess == word:
                score += 20
                print(f"Congratulation! You have correctly guessed : {word}")
                won = True
                break 
            else:
                tries +=1
                score -=5
                print(f"Wrong! You still have {max_tries-tries} times to guess.")
        else:
            if guess in guessed_letters:      
                print("You have guessed this word")
                continue
            
            guessed_letters.append(guess)
            
            
            if guess in word:
                score += 5
                print("Correct!")  
            else:
                tries += 1
                score -= 2
                print(f"Wrong! You still have {max_tries - tries} times to guess.")
        
        
        display_word = [letter if letter in guessed_letters else "_" for letter in word ]      
        print(" ".join(display_word))
        
        if "_" not in display_word:
            print(f"You have correctly guessed: {word}")
            score += 10
            won = True 
            break
        
    if not won:
        print(f"You lose! The word is true: {word}") 

        
                
    print(f"Your score: {score}")
    save_scores(player_name, score)
                
            



if __name__ == "__main__":
    while True:
        print("\n MENU:")
        print("1. Play game")
        print("2. Show leaderboard")
        print("3. Delete scores") 
        print("4. Exit")
        choice = input("Select: ")
        
        if choice == '1':
            play_game()
        elif choice == '2':
            show_leaderboard()
        elif choice == '3':
            clear_scores()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid select! Please choice again!")          
        
                