import random

def roll_the_dice(dices):
    result = []
    for _ in range(dices):
        result.append(random.randint(1,6))
    return result 

number_of_dice = 0 

while True:
    choice = input("Roll the dice ? (y/n): ").lower()
    if choice == 'y':
        dices = int(input('How many dice you want to roll ? '))
        try:
            if dices <= 0:
                print("Please enter the number greater than 0.")
            else:    
                result = roll_the_dice(dices)
                number_of_dice += 1
                print(f'The result roll {dices} dices: {result} ')
                print('Sum of dice: ', sum(result))
        except ValueError:
            print("Please enter a valid number.") 
    
    else:
        print(f'You roll {number_of_dice} times.')
        print("Thanks for playing !")
        break
                
