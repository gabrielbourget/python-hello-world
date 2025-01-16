def translate(phrase):
  translation = ""
  for letter in phrase:
    if letter in "AEIOUaeiou":
      translation = translation + "g"
    else:
      translation = translation + letter
  return translation

user_input = input("Enter phrase to translate: ")
print("Translation of Pidgeon is " + translate(user_input))