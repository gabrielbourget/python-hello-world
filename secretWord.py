secret_word = "leaf"
user_guess = ""

while (user_guess != secret_word):
  user_guess = input("Guess the secret word: ")
  if (user_guess == secret_word):
    print("You win!")
  else:
    print("Try again")