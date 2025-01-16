is_male = True
is_tall = True

if is_male and is_tall:
    print("Male and tall")
elif is_male and not is_tall:
    print("Male but short")
elif not is_male and is_tall:
    print("not male but tall")
else:
    print("Neither male or tall")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else: return num3

print(str(max_num(4,7,8)))