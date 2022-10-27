from art import logo
from art import vs
from game_data import data
from replit import clear
import random

current_score = 0
first_person = random.choice(data)
second_person = random.choice(data)
a = ""
b = ""

def new_comparison():
  global first_person
  global second_person
  global a
  global b
  
  first_person = second_person
  a = f"{first_person['name']}, {first_person['description']}, {first_person['country']}"

  second_person = random.choice(data)
  b = f"{second_person['name']}, {second_person['description']}, {second_person['country']}"


def compare(A, B):
  a_folower = A['follower_count']
  b_folower = B['follower_count']
  if a_folower > b_folower:
    return "a"
  else:
    return "b"

def evaluate():
  global current_score
  global end_of_game
  
  if who == compare(first_person, second_person):
    current_score += 1
  else:
    end_of_game = True

end_of_game = False
while not end_of_game:
  clear()
  print(logo)
  new_comparison()
  
  if current_score > 0:
    print(f"You're right! Current score: {current_score}")

  print(f"Compare A: {a}")
  print(vs)
  print(f"Compare B: {b}")
  who = input("Who has more followers? Type 'A' or 'B': ").lower()
  evaluate()

clear()
print("Sorry, thats's wrong :(")
print(f"Final score: {current_score}")