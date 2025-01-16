employees_file = open("employees.txt", "r")

# for employee in employees_file.readlines():
#   print(employee)

print("info in file -> " + employees_file.read())

employees_file.close()