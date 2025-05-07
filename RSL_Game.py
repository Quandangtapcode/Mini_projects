import random 
import time 

print("Welcome to the RSL Game !")
time.sleep(2)
name = input("Enter your name: ")
print(f"Hello {name}, now starting the game !") 

player_guess = 0
computer_guess = 0

player_win_count = 0
computer_win_count = 0
draw_count = 0

number_of_times_player_win = 0
number_of_times_computer_win = 0
number_of_times_in_harmony = 0

while player_guess != 'exit':
    player_guess = input("Select scissor -s, rock -r, leaf -l, exit \n")
    time.sleep(2)
    
    if player_guess not in ['s','r','l','exit']:
        print("Invalid select. Please select 's', 'r', 'l' or 'exit'")
        continue
    computer_guess = random.randint(1,3)
    if player_guess == 'exit':
        print("See you again!")
        break
    if computer_guess == 1:
        computer_guess = 's'
    elif computer_guess == 2:
        computer_guess = 'r'
    else:
        computer_guess = 'l'
                    
    if player_guess == computer_guess:
        print("Draw !!")
        draw_count += 1
    if player_guess == 's' and computer_guess == 'r':
        print(f"Player lose! Computer guess : {computer_guess}")
        computer_win_count += 1
    if player_guess == 's' and computer_guess == 'l':
        print(f"Player win! Computer guess : {computer_guess}") 
        player_win_count += 1
    if player_guess == 'r' and computer_guess == 's':
        print(f"Player win! Computer guess : {computer_guess}")
        player_win_count += 1
    if player_guess == 'r' and computer_guess == 'l':
        print(f"Player lose! Computer guess : {computer_guess}")
        computer_win_count += 1
    if player_guess == 'l' and computer_guess == 's':
        print(f"Player lose! Computer guess : {computer_guess}")
        computer_win_count += 1
    if player_guess == 'l' and computer_guess == 'r':
        print(f"Player win! Computer guess : {computer_guess}")      
        player_win_count += 1
                      
                

count = {
    "number_of_times_player_win" : player_win_count,
    "number_of_times_computer_win" : computer_win_count,
    "number_of_times_in_harmony" : draw_count
}       

print(f"\n{name}, Result: ")
print(count)