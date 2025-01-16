phrase = "Elephants are "
print(phrase + "very large")

phrase = "string with a modest amount of length"
print("previous phrasee has " + str(len(phrase)) + " characters")

phrase = "as;jjdfa;ljasdfl;kasfdfl"
print("Fourth character of the previous string is " + phrase[3])

phrase = "a;lsdasfd;ljasl;kaslkasdf;lkjasdf;ljhbdfkbjfl"
print("First instance of 'd' is at index " + str(phrase.index("d")))

phrase = "jddhshdhshdsdhsjdhsjdhsdjh"
print(phrase.replace("d", "elephant"))