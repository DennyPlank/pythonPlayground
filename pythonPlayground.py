# # Playing with Tuples

# my_first_tupal = ("Dennis", 27, "Male")

# name, age, gender = my_first_tupal
# # print(my_first_tupal)
# # print(name)
# # print(age)
# # print(gender)
# # print(name + " " + str(age) + " " + gender)

# # Playing with zips()

# kids = ["Darryl", "Emery", "Ellie"]
# ages = [8, 6, 4]

# kids_and_ages = zip(kids, ages)
# # print(list(kids_and_ages))

# # First python loops 

# # For Loops

# statement = "Loop number"

# for x in range(100):
#     print(statement + " " + str(x))

# Loops and if statement control flow
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break;