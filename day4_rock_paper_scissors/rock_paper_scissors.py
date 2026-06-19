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

random_number = random.randint(0, 2)
player_choice = int(input("What do you choose? Choose 0 for Rock, 1 for Paper, 2 for Scissors. "))

if player_choice == 0:
    print("You chose: \n" + rock)
    if random_number == 0:
        print("Computer chose: \n" + rock)
        print("Its a draw!")
    elif random_number == 1:
        print("Computer chose: \n" + paper)
        print("You lost!")
    elif random_number == 2:
        print("Computer chose: \n" + scissors)
        print("You won!")

elif player_choice == 1:
    print("You chose: \n" + paper)
    if random_number == 0:
        print("Computer chose: \n" + rock)
        print("You won!")
    elif random_number == 1:
        print("Computer chose: \n" + paper)
        print("Its a draw!")
    elif random_number == 2:
        print("Computer chose: \n" + scissors)
        print("You lost!")

elif player_choice == 2:
    print("You chose: \n" + scissors)
    if random_number == 0:
        print("Computer chose: \n" + rock)
        print("You lost!")
    elif random_number == 1:
        print("Computer chose: \n" + paper)
        print("You won!")
    elif random_number == 2:
        print("Computer chose: \n" + scissors)
        print("Its a draw!")
else:
    print("Invalid choice!")
