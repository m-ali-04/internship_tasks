# ---------------------------
# STRING (str)
# ---------------------------
# A string is a sequence of characters, used to represent text.
# Immutable: Cannot be changed after creation.
# Benefits: Easy to use, supports powerful methods for manipulation, and is memory efficient.
# Limitations: Since it's immutable, any modification creates a new object (costly in large operations).

text = "Hello, World!"

# Accessing
print(text[0])        # H

# Slicing
print(text[7:12])     # World

# "Changing" (actually creating a new one)
new_text = text.replace("World", "Python")
print(new_text)       # Hello, Python
# name[0] = 'B'  # Error: Strings are immutable

# Use Case: Displaying names, messages, file paths, etc.


# ---------------------------
# LIST (list)
# ---------------------------
# A list is an ordered collection of elements.
# Mutable: You can change, add, or remove elements.
# Benefits: Dynamic, can store mixed data types, and is ideal for collections.
# Limitations: Slower than arrays for large numerical computations.

my_list = [1, 2, 3]

# Accessing
print(my_list[0])      # 1

# Adding (push)
my_list.append(4)      # [1, 2, 3, 4]

# Extending
my_list.extend([5, 6]) # [1, 2, 3, 4, 5, 6]

# Removing
my_list.pop()          # Removes last element: 6
my_list.remove(3)      # Removes first occurrence of 3

# Sorting
my_list.sort()         # [1, 2, 4, 5]

# Copying
new_list = my_list.copy()

print(my_list)
print(new_list)

# Use Case: To store user inputs, to-do tasks, logs, etc.


# ---------------------------
# TUPLE (tuple)
# ---------------------------
# A tuple is like a list, but immutable.
# Immutable: Once defined, cannot be changed.
# Benefits: Faster than lists and safe for fixed data.
# Limitations: Cannot change size or contents after creation.

dimensions = (1920, 1080)

# Accessing
print(dimensions[0])

# Trying to change value (Error)
# dimensions[0] = 1280  → Not allowed

# Useful when returning multiple values:
def get_location():
    return (33.6844, 73.0479)

lat, lon = get_location()
# dimensions[0] = 1280  # Error

# Use Case: Storing constants, fixed coordinates, RGB values, etc.


# ---------------------------
# DICTIONARY (dict)
# ---------------------------
# A dictionary stores key-value pairs.
# Mutable: Values and keys can be added or changed.
# Benefits: Fast lookup by key, ideal for mappings.
# Limitations: Slightly more memory overhead, unordered before Python 3.7.

student = {
    "name": "Ali",
    "age": 22,
    "course": "Python"
}

# Accessing
print(student["name"])

# Adding or Updating
student["grade"] = "A"

# Removing
student.pop("age")

# Copying
new_student = student.copy()

print(student)
print(new_student)

# Use Case: Conditional flags, status indicators.

# ---------------------------
# SETS (set)
# ---------------------------
# Mutable (but elements must be immutable)
# Use case: Unordered unique values
# Benefits: Fast membership test, automatic duplicate removal
# Limitations: No indexing, unordered, not hashable

my_set = {1, 2, 3}

# Adding
my_set.add(4)         # {1, 2, 3, 4}

# Removing
my_set.remove(2)      # {1, 3, 4}

# Accessing: Can't use index, use loop
for item in my_set:
    print(item)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))     # {1, 2, 3, 4, 5}
print(a.intersection(b))  # {3}


# ---------------------------
# INTEGER (int)
# ---------------------------
# Whole numbers without a fractional part.
# Immutable.
# Benefits: Fast and simple, no precision issues.
# Limitations: Not suitable for very precise values like money.

age = 25
print(age + 5)  # Output: 30

# Use Case: Counting, indexing, looping.


# ---------------------------
# FLOAT (float)
# ---------------------------
# A number with a decimal point.
# Immutable.
# Benefits: Suitable for real-world data (e.g., temperature, currency).
# Limitations: Can have precision errors.

temperature = 36.6
print(temperature + 1.4)  # Output: 38.0

# Use Case: Scientific measurements, ratios, currency.

