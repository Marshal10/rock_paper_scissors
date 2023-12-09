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
import random
game=[rock,paper,scissors]
user_choice=int(input("What do you choose?Type 0 for Rock,1 for Paper and 2 for Scissors\n"))

if 0 <= user_choice <= 2:
    user_valid_choice = game[user_choice]
else:
    print("Please type a number between 0 and 2")
    exit()

computer_choice=game[random.randint(0,2)]

print(f"You chose: \n{user_valid_choice}")
print(f"Computer chose: \n{computer_choice}")

if computer_choice==user_valid_choice:
    print("It's a draw!")
elif (
    (user_valid_choice == rock and computer_choice == scissors) or
    (user_valid_choice == paper and computer_choice == rock) or
    (user_valid_choice == scissors and computer_choice == paper)
):
    print("You win!")
else:
    print("You lose!")
