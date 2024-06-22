# Variables and Data Types
integer_variable = 10
float_variable = 10.5
string_variable = "Hello, Python!"
boolean_variable = True

# Printing variables
print(integer_variable)  # Output: 10
print(float_variable)    # Output: 10.5
print(string_variable)   # Output: Hello, Python!
print(boolean_variable)  # Output: True

###Arithmetic Operations:
# Addition
sum_result = 5 + 3
print("Sum:", sum_result)  # Output: Sum: 8

# Subtraction
difference = 10 - 4
print("Difference:", difference)  # Output: Difference: 6

# Multiplication
product = 7 * 6
print("Product:", product)  # Output: Product: 42

# Division
quotient = 8 / 2
print("Quotient:", quotient)  # Output: Quotient: 4.0

####String Manipulation:
# Concatenation
greeting = "Hello, " + "World!"
print(greeting)  # Output: Hello, World!

# Repetition
repeated_string = "Python! " * 3
print(repeated_string)  # Output: Python! Python! Python!

# Slicing
example_string = "Python Programming"
sliced_string = example_string[0:6]
print(sliced_string)  # Output: Python

# Length
string_length = len(example_string)
print("Length of the string:", string_length)  # Output: Length of the string: 18

###Conditional Statements:
number = 7

if number > 5:
    print("The number is greater than 5.")
elif number == 5:
    print("The number is equal to 5.")
else:
    print("The number is less than 5.")
# Output: The number is greater than 5.

###Lists:
# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Adding an element
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Accessing elements
print(fruits[1])  # Output: banana

# Removing an element
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'orange']

###Dictionaries:
# Creating a dictionary
student = {"name": "John", "age": 20, "course": "Computer Science"}
print(student)  # Output: {'name': 'John', 'age': 20, 'course': 'Computer Science'}

# Accessing values
print(student["name"])  # Output: John

# Adding a new key-value pair
student["grade"] = "A"
print(student)  # Output: {'name': 'John', 'age': 20, 'course': 'Computer Science', 'grade': 'A'}

# Removing a key-value pair
del student["age"]
print(student)  # Output: {'name': 'John', 'course': 'Computer Science', 'grade': 'A'}

###Tuples:
# Creating a tuple
coordinates = (10, 20)
print(coordinates)  # Output: (10, 20)

# Accessing elements
print(coordinates[0])  # Output: 10

# Unpacking a tuple
x, y = coordinates
print("x:", x)  # Output: x: 10
print("y:", y)  # Output: y: 20
