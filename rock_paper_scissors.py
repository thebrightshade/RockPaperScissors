import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = {"R": rock, "P": paper, "S": scissors}

def compare(user_choice, computer_choice):
    if user_choice == computer_choice:
        result = "tie"
        print("It's a tie!")
        return result
    elif user_choice == "R" and computer_choice == "S":
        result = "win"
        # print("You win!")
    elif user_choice == "P" and computer_choice == "R":
        result = "win"
        # print("You win!")
    elif user_choice == "S" and computer_choice == "P":
        result = "win"
        # print("You win!")
    else:
        result = "lose"
        # print("You lose!")
    print(f"You {result}!")
    return result

def game_loop():
    user_choice = (input("What do you choose? Type R for Rock, P for Paper or S for Scissors:  ").upper())
    if user_choice not in ['R', 'P', 'S']: 
        print("You typed an invalid option, you lose!")
        return "lose"
    else:
        print("You chose: " + game_images[user_choice])
        # print(game_images[user_choice])
        computer_choice = random.randint(0, 2)
        if computer_choice == 0:
            computer_choice = "R"
        elif computer_choice == 1:
            computer_choice = "P"
        else:
            computer_choice = "S"
        print("Computer chose: " + game_images[computer_choice])
        # print(game_images[computer_choice])
        result = compare(user_choice, computer_choice)
        return result

def main():
    game_end = False
    wins = 0
    losses = 0
    ties = 0
    while game_end == False:
        result = game_loop()
        if result == "win":
            wins += 1
        elif result == "lose":
            losses += 1
        else:
            ties += 1
        print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")
        play_again = input("Do you want to play again? (Y/N) ").upper()
        if play_again == "Y":
            game_end = False
        else:
            print("Thanks for playing!")
            game_end = True


if __name__ == "__main__":
    main()

