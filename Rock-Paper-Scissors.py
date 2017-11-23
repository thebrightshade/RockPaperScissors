import random
player1 = (input("Please select one: Rock(R), Paper(P) or Scissors(S): ")).upper()

player2 = random.sample({"R", "P", "S"}, 1)


def compare(p1, p2):
    if p1 == "S" or p1 == "SCISSORS":
        if p2[0] == "R":
            print("You lose! Rock beats scissors.")
            replay = input("Do you want to play again (Y/N)? ").upper()
            if replay == "Y":
                p1 = (input("Please select one: Rock(R), Paper(P) or Scissors(S): ")).upper()
                p2 = random.sample({"R", "P", "S"}, 1)
                compare(p1,p2)
            
        elif p2[0] == "P":
            print("You win! Scissors beats paper.")
            replay = input("Do you want to play again (Y/N)? ").upper()
            if replay == "Y":
                p1 = (input("Please select one: Rock(R), Paper(P) or Scissors(S): ")).upper()
                p2 = random.sample({"R", "P", "S"}, 1)
                compare(p1,p2)
                
        elif p2[0] == "S":
            print("Let's try again, you and I, both have scissors")
            p1 = (input("Please select one: Rock(R), Paper(P) or Scissors(S): ")).upper()
            p2 = random.sample({"R", "P", "S"}, 1)
            compare(p1,p2)

    elif p1 == "R" or p1 == "ROCK":
        if p2[0] == "P":
            print("You lose! Paper beats rock.")
            replay = input("Do you want to play again (Y/N)? ").upper()
            if replay == "Y":
                p1 = (input("Please select one: Rock(R), Paper(P) or Scissors(S): ")).upper()
                p2 = random.sample({"R", "P", "S"}, 1)
                compare(p1,p2)
            
        elif p2[0] == "S":
            print("You win! Rock beats scissors.")
            replay = input("Do you want to play again (Y/N)? ").upper()
            if replay == "Y":
                p1 = (input("Please select one: Rock(R), Paper(P) or Scissors(S): ")).upper()
                p2 = random.sample({"R", "P", "S"}, 1)
                compare(p1,p2)
            
        elif p2[0] == "R":
            print("Let's try again, you and I, both have rock")
            p1 = (input("Please select one: Rock(R), Paper(P) or Scissors(S): ")).upper()
            p2 = random.sample({"R", "P", "S"}, 1)
            compare(p1, p2)

    elif p1 == "P" or p1 == "PAPER":
        if p2[0] == "S":
            print("You lose! Scissors beats paper.")
            replay = input("Do you want to play again (Y/N)? ").upper()
            if replay == "Y":
                p1 = (input("Please select one: Rock(R), Paper(P) or Scissors(S): ")).upper()
                p2 = random.sample({"R", "P", "S"}, 1)
                compare(p1,p2)
            
        elif p2[0] == "R":
            print("You win! Paper beats rock.")
            replay = input("Do you want to play again (Y/N)? ").upper()
            if replay == "Y":
                p1 = (input("Please select one: Rock(R), Paper(P) or Scissors(S): ")).upper()
                p2 = random.sample({"R", "P", "S"}, 1)
                compare(p1,p2)
            
        elif p2[0] == "P":
            print("Let's try again, you and I, both have paper")
            p1 = (input("Please select one: Rock(R), Paper(P) or Scissors(S): ")).upper()
            p2 = random.sample({"R", "P", "S"}, 1)
            compare(p1, p2)
    else:
        print('You did not type a correct response!')
        player1 = (input("Please select one: Rock(R), Paper(P) or Scissors(S): ")).upper()
        compare(player1, player2)

compare(player1, player2)