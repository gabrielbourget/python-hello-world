animals = ["monkey", "seal", "raptor", "elephant", "snake"]

print(animals)
print(animals[2])
print(animals[-2])
print(animals[1:5])

animals[4] = "eagle"

print(animals)

animals_2 = ["rhinoceros", "turkey"]

animals.extend(animals_2)
print(animals)

animals.append("dolphin")
print(animals)

animals.insert(3, "starfish")
print(animals)

animals.remove("monkey")
print(animals)

print("Index of eagle item -> " + str(animals.index("eagle")))

num_eagles = animals.count("eagle")
print("number of eagles in list -> " + str(num_eagles))

print("reverse order array is -> ", str(animals))

print("sorted array is -> ", sorted(animals))
animals.reverse()

animals_copy = animals.copy()

print("animals list copy -> ", animals_copy)

print("number of elements in animals list -> "+ str(len(animals)))
animals.clear()
print("number of elements in animals list -> " + str(len(animals)))