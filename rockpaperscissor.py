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
list=((rock), (paper), (scissors))
choose=int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. "))
print(list[choose])
import random
integer=int(random.randint(0,2))
print(f"Computer Choose: {list[integer]}")
if choose==0 and integer==0:
  print("This is a tie. Play again.")
if choose==1 and integer==1:
  print("This is a tie. Play again.")
if choose==2 and integer==2:
  print("This is a tie. Play again.")
if choose==0 and integer==1:
  print("You lose.Play again.")
if choose==0 and integer==2:
  print("Yay! You Win. ")
if choose==1 and integer==0:
  print("You lose.Play again.")
if choose==1 and integer==2:
  print("You lose.Play again.")
if choose==2 and integer==0:
  print("You lose.Play again.")
if choose==2 and integer==1:
  print("You lose.Play again.")