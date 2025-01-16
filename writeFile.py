employees_file = open("employees.txt", "a")

print("Appending to text file")

employees_file.write("\nGunther")

employees_file.close()

###

# employees_file = open("employees.txt", "w")

# print("Writing to text file")

# employees_file.write("Sandra\n")

# employees_file.close()

###

employees_file = open("employees.txt", "r")

print("updated employees file -> " + employees_file.read())

employees_file.close()