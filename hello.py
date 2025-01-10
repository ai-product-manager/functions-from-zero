# create a list with different types of fruits
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# loop through the list and print the fruits and count the number of fruits
for fruit in fruits:
    # use an f-string to print the fruit name and the index of the fruit
    print(f"The fruit is: {fruit} and the index is: {fruits.index(fruit)}")

print("The number of fruits in the list is: ", len(fruits))
