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

#Write your code below this line 👇
choices = [rock,paper,scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice > 3 or choice < 0:
    print("Invalid number, You lose")        
else:
    print(choices[choice])
        
    print("Computer chose:")

    computer = random.randint(0,2)

    print(choices[computer])


    if choice == 0 and computer == 2 or choice == 1 and computer == 0 or choice == 2 and computer == 1:
        print("You win")
    elif choice == computer:
        print("Its a drow")
    else:
        print("You lose")
