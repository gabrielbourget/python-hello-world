try:
  # bad_num = 10 / 0
  number = int(input("Enter a number: "))
  print("You entered " + str(number))
except ZeroDivisionError as err:
  print("You cannot divide by zero " + str(err))
except ValueError:
  print("Invalid input")