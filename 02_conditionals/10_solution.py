species = "Cat"
age = 3

if species == "Dog" and age < 2:
    pet_food = "Puppy food"
elif species == "Dog" and age >= 3:
    pet_food = "Mother food"
elif species == "Cat" and age < 4:
    pet_food = "Junior cat food"
elif species == "Cat" and age > 5:
    pet_food = "Senior cat food"

print(pet_food)