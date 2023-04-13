import random

from Words import word_list
word = random.choice(word_list)
chosen_word = word.lower()
print(chosen_word)

from Stages import logo
print(logo)

list = []
for letter in range(len(chosen_word)):
  list += "_"

lives = 6 
end_game = False

while not end_game:
  guess = input("Guess a letter: ").lower()

  if guess in list:
    print(f"You have already guessed {guess}.")
   
  for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
      list[position]=guess
    
  if guess not in chosen_word:
    print(f"You have guessed {guess}, that is not in the word. You lose a life.")

    lives -= 1
    if lives==0:
      end_game = True
      print("You Lose.")

  print(f"{' '.join(list)}")  
      
  if "_" not in list:
    end_game = True
    print("You Win!")

  from Stages import stages
  print(stages[lives]) 
  
