
import random


sccisors = '''

---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

rock = '''

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
my_list = [rock, paper, sccisors]
computer_choice = random.randint(0,2)
choice = int(input("What do you choose? Type 0 for Scissors, 1 for rock or 2 for paper \n"))
if choice == 0:
    print(f"You chose: {sccisors}")
    print(f"Computer chose {computer_choice}")
    if choice == computer_choice:
        print("It's a draw")
    elif choice > computer_choice:
        print("You win")
    else: 
        print("You lose!")
elif choice == 1:
    print(f"You chose: {rock}")
    print(f"Computer chose {computer_choice}")
    if choice == computer_choice:
        print("It's a draw")
    elif choice > computer_choice:
        print("You win")
    else: 
        print("You lose!")
else:
    print(f"You chose: {paper}")
    print(f"Computer chose {computer_choice}")
    if choice == computer_choice:
        print("It's a draw")
    elif choice > computer_choice:
        print("You win")
    else: 
        print("You lose!")

