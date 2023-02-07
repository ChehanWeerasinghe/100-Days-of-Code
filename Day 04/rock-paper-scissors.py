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

# Write your code below this line 👇
import random

choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
))

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("Invalid choice")

print("Computer chose:")

computer_choice = random.randint(0, 3)

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if (choice == computer_choice):
    print("Draw")
elif (choice == 0 and computer_choice == 1):
    print("You lose")
elif (choice == 0 and computer_choice == 2):
    print("You win")
elif (choice == 1 and computer_choice == 0):
    print("You win")
elif (choice == 1 and computer_choice == 2):
    print("You Lose")
elif (choice == 2 and computer_choice == 0):
    print("You Lose")
elif (choice == 2 and computer_choice == 1):
    print("You win")
