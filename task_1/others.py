#list comprehension

#simulating lines like in a file
text = "HELLO\nWHY\nLMAO"
lines = text.split("\n")
[line.strip() for line in lines]  # ['HELLO', 'WHY', 'LMAO']


print([v.upper() for v in "hello"])
print([x * 2 for x in {1, 2, 3}])
print([k for k in {"a": 1, "b": 2}])
print([v for v in {"a": 1, "b": 2}.values()])
print([line.strip() for line in "HELLO\nWHY\nLMAO".split('\n')])

#error catching

# ValueError – when the type is right but the value is wrong
try:
    int("abc")
except ValueError:
    print("Cannot convert to integer")

# TypeError – when an operation is applied to an object of inappropriate type
try:
    "2" + 3
except TypeError:
    print("Can't add string and integer")

# ZeroDivisionError – division by zero
try:
    x = 5 / 0
except ZeroDivisionError:
    print("You can't divide by zero")

# IndexError – accessing list index that doesn't exist
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index out of range")

# KeyError – accessing a dictionary with a missing key
try:
    my_dict = {"a": 1}
    print(my_dict["b"])
except KeyError:
    print("Key not found in dictionary")

# FileNotFoundError – trying to open a file that doesn't exist
try:
    with open("missing.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")

# AttributeError – when an invalid attribute is accessed
try:
    x = 5
    x.append(2)
except AttributeError:
    print("Object has no such attribute")

# ImportError – when an import fails
try:
    import non_existing_module
except ImportError:
    print("Module not found")

# NameError – when a variable or function name is not defined
try:
    print(xyz)
except NameError:
    print("Variable is not defined")

# RuntimeError – generic error when no other type applies
try:
    raise RuntimeError("Something bad happened")
except RuntimeError as e:
    print(f"Runtime error: {e}")

# IndentationError and SyntaxError – these can't be caught at runtime
# They happen at parse/compile time, so you'll fix them before code runs
