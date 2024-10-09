# python

<img align="right" alt="python_logo" width="300" src="https://github.com/akashdip2001/Python-Course-10h/raw/main/img/py_akashdip2001.png"> 




# Python Study Guide

---

## Table of Contents
1. [History of Python](#history-of-python)
2. [Variables](#variables)
3. [Operators](#operators)
   - [Arithmetic Operators](#arithmetic-operators)
   - [Assignment Operators](#assignment-operators)
   - [Comparison Operators](#comparison-operators)
   - [Incrementing and Decrementing Operators](#incrementing-and-decrementing-operators)
   - [Logical Operators](#logical-operators)
4. [Data Types](#data-types)
   - [Constants](#constants)
5. [Conditional Statements](#conditional-statements)
6. [Arrays](#arrays)
7. [Loops](#loops)
8. [Functions](#functions)
   - [Built-in Functions](#built-in-functions)
   - [User-defined Functions](#user-defined-functions)
9. [Strings](#strings)
10. [*Source code*](https://github.com/akashdip2001/Python-Course-10h)
11. [*more*](https://www.codewithharry.com/tutorial/python/)
12. [**Part 2 (Job Preparation)**](#part-2-job-preparation)

---

## History of Python
Python was created by Guido van Rossum and first released in 1991. The language was designed to be easy to read and write, making it suitable for beginners as well as experienced programmers. Its development was influenced by ABC, a programming language that Guido worked on before Python. Over the years, Python has evolved significantly, with major versions like Python 2 and Python 3 introducing many features and enhancements. 

Today, Python is widely used in various fields, including web development, data science, artificial intelligence, automation, and more. Its large community and rich ecosystem of libraries and frameworks make it a versatile choice for many programming tasks.

---

## Variables
Variables are used to store data values. In Python, you do not need to declare a variable type explicitly; the interpreter infers the type based on the value assigned.

**Example:**
```python
name = "Alice"  # String variable
age = 30        # Integer variable
height = 5.6    # Float variable
```

---

## Operators
Operators perform operations on variables and values. Python supports various types of operators, including arithmetic, assignment, comparison, increment/decrement, and logical operators.

### Arithmetic Operators
Arithmetic operators are used to perform common mathematical operations.

| Operator | Description   | Example       | Result                     |
|----------|---------------|---------------|----------------------------|
| `+`      | Addition      | `x + y`       | Sum of `x` and `y`        |
| `-`      | Subtraction   | `x - y`       | Difference of `x` and `y` |
| `*`      | Multiplication| `x * y`       | Product of `x` and `y`    |
| `/`      | Division      | `x / y`       | Quotient of `x` and `y`   |
| `//`     | Floor Division| `x // y`      | Floor of quotient of `x` and `y` |
| `%`      | Modulus       | `x % y`       | Remainder of `x` divided by `y` |
| `**`     | Exponentiation| `x ** y`      | `x` raised to the power of `y` |

**Example:**
```python
x = 10
y = 3

print("x + y =", x + y)  # Addition
print("x - y =", x - y)  # Subtraction
print("x * y =", x * y)  # Multiplication
print("x / y =", x / y)  # Division
print("x // y =", x // y)  # Floor Division
print("x % y =", x % y)  # Modulus
print("x ** y =", x ** y)  # Exponentiation
```

### Assignment Operators
Assignment operators are used to assign values to variables.

| Operator | Description              | Example       | Result              |
|----------|--------------------------|---------------|---------------------|
| `=`      | Assign                   | `x = 5`       | Assign 5 to `x`     |
| `+=`     | Add and assign           | `x += 2`      | Equivalent to `x = x + 2` |
| `-=`     | Subtract and assign      | `x -= 2`      | Equivalent to `x = x - 2` |
| `*=`     | Multiply and assign      | `x *= 2`      | Equivalent to `x = x * 2` |
| `/=`     | Divide and assign        | `x /= 2`      | Equivalent to `x = x / 2` |

**Example:**
```python
x = 5
print("Initial x:", x)

x += 2  # Equivalent to x = x + 2
print("After x += 2:", x)

x *= 3  # Equivalent to x = x * 3
print("After x *= 3:", x)
```

### Comparison Operators
Comparison operators are used to compare two values.

| Operator | Description                 | Example       | Result            |
|----------|-----------------------------|---------------|-------------------|
| `==`     | Equal to                    | `x == y`      | True if `x` is equal to `y` |
| `!=`     | Not equal to                | `x != y`      | True if `x` is not equal to `y` |
| `>`      | Greater than                | `x > y`       | True if `x` is greater than `y` |
| `<`      | Less than                   | `x < y`       | True if `x` is less than `y` |
| `>=`     | Greater than or equal to    | `x >= y`      | True if `x` is greater than or equal to `y` |
| `<=`     | Less than or equal to       | `x <= y`      | True if `x` is less than or equal to `y` |

**Example:**
```python
x = 10
y = 20

print("x == y:", x == y)  # False
print("x != y:", x != y)  # True
print("x > y:", x > y)    # False
print("x < y:", x < y)    # True
print("x >= y:", x >= y)  # False
print("x <= y:", x <= y)  # True
```

### Incrementing and Decrementing Operators
Python does not support `++` or `--` operators as in some other languages, but you can achieve similar functionality using `+=` and `-=`.

**Example:**
```python
x = 5
x += 1  # Increment
print("After incrementing x:", x)  # Output: 6

x -= 1  # Decrement
print("After decrementing x:", x)  # Output: 5
```

### Logical Operators
Logical operators are used to combine conditional statements.

| Operator | Description            | Example           | Result                        |
|----------|------------------------|-------------------|-------------------------------|
| `and`    | True if both operands are true | `x > 5 and y < 10` | True if both conditions are true |
| `or`     | True if at least one operand is true | `x > 5 or y < 10`  | True if at least one condition is true |
| `not`    | True if operand is false | `not(x > 5)`     | True if condition is false    |

**Example:**
```python
x = 10
y = 5

print("x > 5 and y < 10:", x > 5 and y < 10)  # True
print("x > 5 or y < 3:", x > 5 or y < 3)      # True
print("not(x < 5):", not(x < 5))                # True
```

---

## Data Types
Python has various built-in data types, including:

- **Integers**: Whole numbers, e.g., `5`, `-3`
- **Floats**: Decimal numbers, e.g., `3.14`, `-2.5`
- **Strings**: Sequences of characters, e.g., `"Hello"`
- **Booleans**: `True` or `False`

### Constants
Constants are immutable values that do not change during program execution. Python uses naming conventions to indicate constants, typically uppercase letters.

```python
PI = 3.14159  # Example of a constant
```

---

## Conditional Statements
Conditional statements allow you to execute code based on specific conditions.

**Example:**
```python
x = 10

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

---

## Arrays
In Python, arrays can be implemented using lists, but for more advanced functionality, the `array` module or `numpy` library can be used.

**Example using lists:**
```python
# List as an array
numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # Accessing the first element
```

---

## Loops
Loops are used to execute a block of code repeatedly.

### For Loop
```python
# For loop
for i in range(5

):
    print(i)
```

### While Loop
```python
# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```

---

## Functions
Functions are reusable blocks of code that perform a specific task.

### Built-in Functions
Python provides many built-in functions like `len()`, `print()`, and `type()`.

**Example:**
```python
names = ["Alice", "Bob", "Charlie"]
print("Number of names:", len(names))  # Output: 3
```

### User-defined Functions
You can create your own functions using the `def` keyword.

**Example:**
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```

---

## Strings
Strings are sequences of characters and can be manipulated in various ways.

**Example:**
```python
text = "Hello, World!"
print(text[0])  # Accessing the first character
print(text.lower())  # Convert to lowercase
print(text.upper())  # Convert to uppercase
print(text.replace("World", "Python"))  # Replace substring
```
![](https://github.com/akashdip2001/college-final-year-project/raw/main/img/colour_line.png)

## Part 2 (Job Preparation)
# Python Study Guide for Job Exam

## Table of Contents:
1. [Python Basics](#1-python-basics)
2. [Data Structures](#2-data-structures)
   - [Lists](#lists)
   - [Tuples](#tuples)
   - [Dictionaries](#dictionaries)
   - [Sets](#sets)
3. [Functions](#3-functions)
4. [Object-Oriented Programming (OOP)](4-object-oriented-programming-oop)
   - [Classes & Objects](#classes--objects)
   - [Inheritance](#inheritance)
   - [Encapsulation](#encapsulation)
   - [Polymorphism](#polymorphism)
5. [File Handling](#5-file-handling)
6. [Libraries & Modules](#6-libraries--modules)
7. [Exception Handling](#7-exception-handling)
8. [Common Interview Questions](#8-common-interview-questions)
9. [Best Documentation Resources](#9-best-documentation-resources)

---

### 1. Python Basics
Python is a powerful and easy-to-learn language. It uses dynamic typing, meaning you don't have to declare variable types.

**Example:**
```python
name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

**Syntax Explanation:**
- `name = "John"`: Assigns the string "John" to the variable `name`.
- `age = 25`: Assigns the integer `25` to the variable `age`.
- `print(...)`: Outputs the formatted string to the console.

---

### 2. Data Structures
Data structures in Python help store and organize data efficiently.

#### **Lists**
- **Description**: Lists are ordered, mutable sequences.
- **Syntax**: `list_name = [item1, item2, ...]`

**Example:**
```python
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')  # Add item
print(fruits[1])         # Accessing item
```

| Operation      | Description                  | Syntax                    |
|----------------|------------------------------|---------------------------|
| Create         | Create a new list            | `fruits = []`            |
| Add item       | Append an item               | `fruits.append('orange')`|
| Access item    | Get an item by index         | `fruits[1]`              |
| Remove item    | Remove an item               | `fruits.remove('banana')`|

---

#### **Tuples**
- **Description**: Tuples are ordered, immutable sequences.
- **Syntax**: `tuple_name = (item1, item2, ...)`

**Example:**
```python
coordinates = (10, 20)
print(coordinates[0])  # Accessing tuple item
```

| Operation      | Description                  | Syntax                      |
|----------------|------------------------------|-----------------------------|
| Create         | Create a new tuple           | `coordinates = ()`         |
| Access item    | Get an item by index         | `coordinates[0]`           |

---

#### **Dictionaries**
- **Description**: Dictionaries store data as key-value pairs.
- **Syntax**: `dict_name = {key1: value1, key2: value2, ...}`

**Example:**
```python
person = {'name': 'Alice', 'age': 30}
print(person['name'])  # Accessing value by key
```

| Operation      | Description                  | Syntax                      |
|----------------|------------------------------|-----------------------------|
| Create         | Create a new dictionary      | `person = {}`              |
| Add item       | Add a new key-value pair     | `person['name'] = 'Alice'` |
| Access item    | Get value by key             | `person['age']`            |
| Remove item    | Remove key-value pair        | `del person['age']`        |

---

#### **Sets**
- **Description**: Sets are unordered collections with no duplicate elements.
- **Syntax**: `set_name = {item1, item2, ...}`

**Example:**
```python
unique_numbers = {1, 2, 3, 4, 5}
unique_numbers.add(6)  # Adding element
```

| Operation      | Description                  | Syntax                      |
|----------------|------------------------------|-----------------------------|
| Create         | Create a new set             | `unique_numbers = set()`   |
| Add item       | Add an element               | `unique_numbers.add(6)`    |
| Remove item    | Remove an element            | `unique_numbers.remove(1)` |

---

### 3. Functions
Functions in Python are defined using the `def` keyword.

**Syntax**: 
```python
def function_name(parameters):
    # Function body
```

**Example:**
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Akashdip"))
```

**Function with Default Parameter:**
```python
def greet(name="Stranger"):
    return f"Hello, {name}!"

print(greet())  # Outputs: Hello, Stranger!
```

| Operation        | Description                       | Syntax                      |
|------------------|-----------------------------------|-----------------------------|
| Define function   | Create a function                 | `def function_name():`      |
| Call function     | Execute the function              | `function_name(arguments)`   |

---

### 4. Object-Oriented Programming (OOP)

OOP is a programming paradigm where you model real-world things as objects with attributes (data) and behaviors (methods).

#### **Classes & Objects**
- **Description**: A class defines a blueprint for creating objects.
- **Syntax**: 
```python
class ClassName:
    def __init__(self, parameters):
        # Constructor
```

**Example:**
```python
class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
    
    def display_info(self):
        return f"{self.name}, ID: {self.id}, Salary: {self.salary}"

emp1 = Employee("Akashdip", 101, 50000)
print(emp1.display_info())
```

| Operation       | Description                      | Syntax                        |
|-----------------|----------------------------------|-------------------------------|
| Define class    | Create a class                   | `class ClassName:`            |
| Initialize      | Define constructor                | `def __init__(self, ...):`   |
| Create object   | Instantiate a class              | `obj = ClassName()`          |

---

#### **Inheritance**
- **Description**: Inheritance allows a class to inherit properties and methods from another class.
- **Syntax**: 
```python
class ChildClass(ParentClass):
    def __init__(self, parameters):
        super().__init__(parameters)
```

**Example:**
```python
class Manager(Employee):
    def __init__(self, name, id, salary, department):
        super().__init__(name, id, salary)
        self.department = department

mgr1 = Manager("Shubham", 102, 60000, "Sales")
print(mgr1.department)  # Outputs: Sales
```

| Operation       | Description                     | Syntax                        |
|-----------------|---------------------------------|-------------------------------|
| Create subclass  | Define a child class            | `class ChildClass(Parent):`   |
| Call parent class| Access parent class attributes   | `super().__init__(...)`      |

---

#### **Encapsulation**
- **Description**: Encapsulation hides private data and only allows access through public methods.
- **Syntax**: Use double underscore `__` to denote private variables.

**Example:**
```python
class Employee:
    def __init__(self, name, salary):
        self.__name = name  # Private variable
        self.__salary = salary
    
    def get_salary(self):
        return self.__salary

emp = Employee("Jyoti", 55000)
print(emp.get_salary())  # Correct way to access private data
```

| Operation       | Description                     | Syntax                        |
|-----------------|---------------------------------|-------------------------------|
| Define private variable| Use double underscore   | `self.__variable`            |
| Access private data | Use public methods          | `obj.get_salary()`           |

---

#### **Polymorphism**
- **Description**: Polymorphism allows methods to be defined differently based on the object.
- **Syntax**: Define methods with the same name in different classes.

**Example:**
```python
class Bird:
    def sound(self):
        return "Chirp"
    
class Dog:
    def sound(self):
        return "Bark"

def animal_sound(animal):
    print(animal.sound())

bird = Bird()
dog = Dog()

animal_sound(bird)  # Outputs: Chirp
animal_sound(dog)   # Outputs: Bark
```

| Operation       | Description                     | Syntax                        |
|-----------------|---------------------------------|-------------------------------|
| Define method   | Create methods with the same name| `def sound(self):`          |
| Call method     | Call the method on the object   | `animal.sound()`            |

---

### 5. File Handling
File handling is essential for reading and writing files in Python.

#### **Opening a File**
```python
file = open("test.txt", "r")
content = file.read()
print(content)
file.close()
```

| Operation       | Description                     | Syntax                        |
|-----------------|---------------------------------|-------------------------------|
| Open file       | Open a file in read mode       | `open("file.txt", "r")`     |
| Read file       | Read contents of the file      | `file.read()`                |
| Close file      | Close the file                 | `file.close()`               |

#### **Writing to a File**
```python
file = open("test.txt", "w")
file.write("Hello, World!")
file.close()
```

| Operation       | Description                     | Syntax                        |
|-----------------|---------------------------------|-------------------------------|
| Write file      | Write to a file                | `file.write("content")`      |

#### **Using `with` Statement**
Using `with` ensures proper file closure.
```python
with open("test.txt", "r") as file:
    content = file.read()
    print(content)
```

| Operation       | Description                     | Syntax                        |
|-----------------|---------------------------------|-------------------------------|
| Use `with`      | Automatically handles file closure | `with open(...) as file:`    |

---

### 6. Libraries & Modules
Libraries and modules allow code reusability. A module is a file containing Python code.

#### **Importing a Module**
Example of using the `math` module:
```python
import math
print(math.sqrt(16))  # Outputs: 4.0
```

| Operation       | Description                     | Syntax                        |
|-----------------|---------------------------------|-------------------------------|
| Import module    | Import built-in or external module| `import module_name`        |

#### **Creating Your Own Module**
Save the following code in `mymodule.py`:
```python
def greet(name):
    return f"Hello, {name}!"
```
Then, import it in your program:
```python
import mymodule
print(mymodule.greet("Akashdip"))
```

| Operation       | Description                     | Syntax                        |
|-----------------|---------------------------------|-------------------------------|
| Create module   | Create a `.py` file            | `def function_name():`       |
| Import module   | Use the defined functions       | `import module_name`         |

---

### 7. Exception Handling
Exceptions allow you to handle errors gracefully.

#### **Try-Except Block**
Example:
```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

| Operation       | Description                     | Syntax                        |
|-----------------|---------------------------------|-------------------------------|
| Try block       | Code that may raise an exception| `try:`                       |
| Except block    | Handle specific exceptions      | `except ExceptionType:`      |

#### **Finally Block**
The `finally` block runs no matter what.
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("This block always executes.")
```

| Operation       | Description                     | Syntax                        |
|-----------------|---------------------------------|-------------------------------|
| Finally block   | Code that always runs           | `finally:`                   |

---

### 8. Common Interview Questions
- **What are the differences between a list and a tuple?**
  - Lists are mutable, while tuples are immutable.
- **Explain inheritance in Python.**
  - Inheritance allows one class to inherit properties and methods from another.
- **How does Python handle memory management?**
  - Python uses automatic garbage collection and reference counting.
- **What are decorators in Python?**
  - Decorators are functions that modify the functionality of another function.
- **Explain the use of `self` in classes.**
  - `self` refers to the instance of the class and is used to access variables that belong to the class.

---

### 9. Best Documentation Resources
- **Python Official Docs:** [Python.org Documentation](https://docs.python.org/3/)
- **Real Python:** [RealPython.com](https://realpython.com)
- **W3Schools Python Tutorial:** [W3Schools Python](https://www.w3schools.com/python/)
- **GeeksforGeeks Python:** [GeeksforGeeks Python](https://www.geeksforgeeks.org/python-programming-language/)

---

### Conclusion
This study guide provides you with a strong foundation in Python for your upcoming exam. Be sure to practice coding challenges and familiarize yourself with the concepts mentioned. Good luck!


### Enhancements Made:
1. **Headings and Tables**: Improved the organization of the content with tables for quick reference on operations for data structures, functions, and OOP concepts.
2. **Syntax Explanations**: Added explanations for syntax to clarify usage.
3. **Navigation Links**: Included clickable links in the Table of Contents for easy navigation within the document.
4. **General Formatting**: Ensured clear separation of sections and enhanced readability.
