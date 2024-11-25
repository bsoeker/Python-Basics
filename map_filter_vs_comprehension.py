myList = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, myList))
print(squared)

mod2 = list(filter(lambda x: x % 2 == 0, myList))
print(mod2)


# General formula for comprehensions = [expression for item in iterable]
squared_with_comprehension = [num**2 for num in myList]
print(squared_with_comprehension)

mod2_with_comprehension = [num for num in myList if num % 2 == 0]
print(mod2_with_comprehension)

# Note that when else statement is included too, the place of our condition block moves to the middle
another_filter = [num if num % 2 == 0 else num + 1 for num in myList]
print(another_filter)

# We can also use list comprehensions to flatten nested lists for example
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [num for sublist in nested for num in sublist]
print(flattened)

# can also be used with dictionaries
myDict = {
    1: "a",
    2: "b",
    3: "c"
}

reversed_myDict = {value: key for key, value in myDict.items()}
print(reversed_myDict)

squared_dict = {num: num**2 for num in myList}
print(squared_dict)

even_squares = {num: num**2 for num in myList if num % 2 == 0}
print(even_squares)

parity = {num: ('even' if num % 2 == 0 else 'odd') for num in myList}
print(parity)

abcde = ["a", "b", "c", "d", "e"]
combined = {num: letter for num, letter in zip(myList, abcde)}
print(combined)

string = "Hello World!"
char_counter = {char: string.count(char) for char in string}
print(char_counter)
