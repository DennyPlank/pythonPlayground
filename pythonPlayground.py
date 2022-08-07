# Playing with Tuples

my_first_tupal = ("Dennis", 27, "Male")

name, age, gender = my_first_tupal
# print(my_first_tupal)
# print(name)
# print(age)
# print(gender)
# print(name + " " + str(age) + " " + gender)

# Playing with zips()

kids = ["Darryl", "Emery", "Ellie"]
ages = [8, 6, 4]

kids_and_ages = zip(kids, ages)
print(list(kids_and_ages))