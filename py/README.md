<img align="right" alt="python_logo" width="300" src="https://github.com/akashdip2001/Python-Course-10h/raw/main/img/py_akashdip2001.png"> 




# Python Study Guide

```yaml
Taste of Pyrhon
   │
   │── Jpython
   │── PyPy
   │── Anaconda Python
   └── Cpython: Core Python
```

100 Python Practice Problems. [Link](https://github.com/akashdip2001/ML-Machine-Learning/blob/main/py/QA.md)

---

## Table of Contents
1. [History of Python](#history-of-python)
2. [Introduction]()
   - [Input Output](#input-output)
   - [Print](#print)
        - [custom separator]()
        - [custom ending]()
   - [Keywords](#keywords)
3. [Variables](#variables)
4. [Data Types](#data-types)
   - [String, int, float, bool](#Examples)
   - [Data Structure](#list-tuple-set-dict) ☀️
      1. [List](#list)
      2. [Tuple](#tuple)
      3. [Set](#set)
      4. [Dictionary](#dictionary)
      5. [DSA](https://github.com/akashdip2001/dsa-using-python)
5. [Operators](#operators)
   - [Arithmetic Operators](#arithmetic-operators)
   - [Assignment Operators](#assignment-operators)
   - [Comparison Operators](#comparison-operators)
   - [Incrementing and Decrementing Operators](#incrementing-and-decrementing-operators)
   - [Logical Operators](#logical-operators)
6. [Flow Control Statement](#flow-control-statement)
   - [Conditional Statements - If-Else](#conditional-statements)
   - [Iterative Statements - Loop](#loops)
   - [Trandfer Statement](#trandfer-statement)
        - [pass]()
        - [continue]()
        - [break]()
7. [Arrays](#arrays)
8. [Strings](#strings)
9. [Loops](#loops)
10. [Modules](#modules)
11. [Functions](#functions)
   - [Built-in Functions](#built-in-functions)
   - [User-defined Functions](#user-defined-functions)
        - [positional parameters](#parameters)
        - [keyword argument](#keyword-argument)
        - [default argument](#default-argument)
12. [Exception Handling](#3-exception-handling)
13. [File Handling](#2-file-handling)
14. [Object-Oriented Programming (OOP)](#oop)
      - [Classes & Objects](#classes--objects)
         1. [Constructor](#constructor) ☀️
            - [Default constructor](#default-constructor)
            - [Parameteriged constructor](#parameteriged-constructor)
         3. [Access Modifires](#access-modifires) 🌳
      - [Inheritance](#inheritance)
           1. [Single Inheritance](#single-inheritance)
           2. [Multiple Inheritance](#multiple-inheritance)
           3. [Multilevel Inheritance](#multilevel-inheritance)
           4. [Hierarchical Inheritance](#hierarchical-inheritance)
           5. [Hybrid Inheritance](#hybrid-inheritance)
      - [Encapsulation](#encapsulation)
      - [Polymorphism](#polymorphism)
           1. [Over-loading](#overloading)
           2. [Over-riding](#overriding)
15. [Multi Threading](#multi-threading)
16. [Python DATABASE Connectivity](#python-database-connectivity)

17. [*Source code*](https://github.com/akashdip2001/Python-Course-10h)
18. [*more*](https://www.codewithharry.com/tutorial/python/)
19. [**Part 2 (Job Preparation - in One Short)**](#part-2-job-preparation)
20. [Projects](#Projects)
21. [**EXAM**](#EXAM)

---

# Python?
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

## History of Python
Python was created by `Guido van Rossum` and first released in `1991` at CWI in Netherland. It's a `general purpose dynamically typr high level language`. Its development was influenced by `ABC`, a programming language that Guido worked on before Python. Over the years, Python has evolved significantly, with major versions like Python 2 and Python 3 introducing many features and enhancements. 

Today, Python is widely used in various fields, including web development, data science, artificial intelligence, automation, and more. Its large community and rich ecosystem of libraries and frameworks make it a versatile choice for many programming tasks.

---
## ✅ Input Output <a name="input-output"></a>

- **In python , always take input as a String.**
- 1st we take an input and store in a variable.

```python
# python always take user input as a String
variable = input("Enter number: ")
print(variable)
print(type(variable))

# Output
# Enter number: 12
# 12
# 'str' ---> String
```

```python
# But we Manually change it
variable = int(input("Enter number: "))
print(variable)
print(type(variable))

# Output
# Enter number: 12
# 12
# 'int'
```
All in one : Automatically detect `int`, `float`, `String`, ...
```yaml
DataType
│
│── int
│── float
│── bool
│── complex
│── ...
└── eval: int + float + bool + ...
```

## ✅ Print <a name="print"></a>

```python
print("Hello","Akash","dip")
# Output: Hellow Akash dip
```
```python
print("Hello","Akash","dip",sep="-") # custom separator
# Output: Hellow-Akash-dip
```
```python
print("Hello")
print("Akash")
# Output: Hellow
          Akash
```
```python
print("Hello"end=" ") # end with a space, \n for new line
print("Akash")
# Output: Hellow Akash
```
## ✅ Keywords <a name="keywords"></a>

**case sensitive**

```python
import keyword
var = keyword.kwlist
print(var)
```
Output

```go
'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
```
---

# Variables

- Variable is the name of `memory location`.
- Variables are used to store data values. In Python, you do not need to declare a variable type explicitly; the interpreter infers the type based on the value assigned.
- Data values Can hold different types of data depending on the `Data-type`.

## ➡️ Data Types <a name="data-types"></a> 
#### [PDF notes](https://github.com/akashdip2001/ML-Machine-Learning/blob/main/py/sources/pdf/Data%20Types%20in%20Python.pdf)

![datatypes in python](https://github.com/user-attachments/assets/a7fcfc92-6b4e-4e21-b849-c62de0fb96b5)

Python has various built-in data types, including:

- **Integers**: Whole numbers, e.g., `5`, `-3`
- **Floats**: Decimal numbers, e.g., `3.14`, `-2.5`
- **Strings**: Sequences of characters, e.g., `"Hello"`
- **Booleans**: `True` or `False`

```python
a = 10
b = "python"

type(a)
#int #output

type(b)
#str
```

### Constants
Constants are immutable values that do not change during program execution. Python uses naming conventions to indicate constants, typically uppercase letters.

```python
PI = 3.14159  # Example of a constant
```

---

**Example of ✅ Variables with ➡️ Data-Types:** <a name="Examples"></a>
```python
name = "Alice"  # String variable
age = 30        # Integer variable
height = 5.6    # Float variable
mathEq = 12+5j  # Complex
ans = True      # Bool
```
- ✅ Python auto detect the DataType.
- ✅ But for user input py always take String

Output
```python
print(type(name))
# Srting
print(type(age))
# int
print(type(height))
# float
```

### 🛩️ List, Tuple, set, dictionary <a name="list-tuple-set-dict"></a>

```python
list = [10,"Akashdip", 45.2, 10]
tuple = (10,"Akashdip",45.2)
set = {10,"Akashdip",45.2}
dictionary = {'age': 21} # get value --> print(dictonary.get('age'))
```

- List & Tuple : list & Tuple allow duplicate value [10, 10, "akash", 15, 8.5], diff is [] & ()
- set : Ignore duplicate values , Just print one time.
- Dictionary : Not use duplicate key , Ex: 'age'

---

## ☀️ List <a name="list"></a>
- **Description**: Lists are ordered, mutable sequences.

List is a Data structure which is also called collection of items, in which we can store anything like - string, float, integer.
- items inside "Square brackets" [] and each items saperated by "comma" (,). Ex: [10, 10, 2]
- Dublicates are `allowed`.
- Mutable in nature (✅ edite, modefi, update, delete)
-  **Syntax**: `list_name = [item1, item2, ...]`

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


```yaml
List
│
│── Create emply list: list1=[]
│                      list2=list() #create a list using list function
│                      print(type(list1))
│                      print(type(list2))
│── List with some values: list3[10,'Akashdip',True, 10.5, 10]
│                          print(list3)                         
│── methods
│   │
│   │── indexing: print(list3[1]) #output: Akashdip -----> find data using index.
│   │             print(list3.index(10.5)) #outpot: 3 ---> find index using data.
│   │             print(list3.index(10,1)) #outpot: 4 ---> ,1 for find 10 But not 1st one.
│   │── count list items: print(list3.count("Akashdip")) #output: 1 (one Time in the list)
│   │── insert: list3.insert(2, "Mahapatra") #output: 10, Akashdip, Mahapatra, ...
│   │── append: list3.append("car") #output: ..., True, 10.5, 10, car ---> add at the last
│   │── pop (Delete): list3.pop(2) #pop() --> if I give no index, by default Delete the last one.
│   │── extend: list4=["sun","Moon"]
│   │           list3.extend(list4)
│   │           #output: 10,'Akashdip',True, 10.5, 10, sun, Moon
│   │── Copy: list5 = list3.copy() or,
│   │         list5 = list3.[:] #by default [0:n-1] ==> all items
│   │── sort: list3.sort() #output: ⚠️ Type-Error
│   │         list6[10, 130, 34, 1, 0] ---> list6.short() #output: [0, 1, 10, 34, 130]
│   │         ----------------> list6.short(reverse=true) #output: [130, 34, 10, 1, 0]
│   │── reverse: list3.reverse() #output: [10, 10.5, True, 'Akashdip', 10]
│   │── Neated list: list6=[10, 130, 34, 1, 0,["Akash","True",[78.5,"Mahapatra"]]] #List inside List
│   │── List Comprehension: list7=["Akash","Suman","Tathagata","Soumyadeep"]
│   │                       a=[word for word in list7 if word.startswith("s")]
│   │                       #output: ["Suman", "Soumyadeep"]
│   └── List Unpacking: n1,n2=list7
│                       print(n1)
│                       print(n2)
│                       #output: Akash
│                       #        Suman
│── slicing: print(list3[1:4]) #output: 'Akashdip', True, 10.5
└── length of list

```
---
## ☀️ Tuple <a name="tuple"></a>
- **Description**: Tuples are ordered, immutable sequences.

Tuple is a Data structure which is also called collection of items, in which we can store anything like - string, float, integer.
- items inside "parenthesis" () and each items saperated by "comma" (,). Ex: (10, 10, 2)
- Dublicates are `allowed`.
- Immutable in nature (❌ edite, modefi, update, delete)
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


```python
var=(1,2,3,4,5,True,"Akashdip")
print(var)
#output: (1,2,3,4,5,True,"Akashdip"),

# But What If, ❌ not use ()
var=1,2,3,4,5,True,"Akashdip"
print(var)
print(type(var))
#output: (1,2,3,4,5,True,"Akashdip"),
#        'tuple'

# But What If,
var=1  #output: 'int'
var=1, #output: 'tuple'

# length
print(len(var)) #output: 7

# Copy
var2=var

# indexing
print(var[5])     #output: True
var.index("True") #output: 5

# insert ❌ Immutable
# append ❌ Immutable
# pop ❌ Immutable
```
---

## ☀️ Set <a name="set"></a>
- **Description**: Sets are unordered collections with no duplicate elements.
```python
set = {10,"Akashdip",45.2}
```

- Same as List ot Tuple
- But, Ignore duplicate values , Just print one time.
- Indexing & order not present.
- Indexing & slicing not work.
- Hetrogenout element are allowed.
- Mutable in nature ✅
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


```python
# creating a emply set
var={}
print(type(var)) #output: Dist ✅, not ❌ set

var=set()
print(type(var)) #output: set ✅

var={10, "Akashdip", 56.7, True}
print(type(var)) #output: set
# Not Dist, because in Dist you must have a key value --> dictionary = {'age': 10}
```
```python
print(var) #output: 56.7, True, 10, 'Akashdip' ❌ input order not work

# indexing ❌
# slicing ❌
```
#### unique value
```python
var={10, "Akashdip", 56.7, True, "Akashdip"}
print(var)
#output: 10, 56.7, True, "Akashdip"
```
#### Immutable in nature
```yaml
│── var.add("Mahapatra") #onlu one argument at a time.
│
│── Update: 
│   │── var.update("Mahapatra") #output: M a h a p a t r a
│   │── var.update(["Mahapatra"]) #output: Mahapatra
│   └── var.update(["Mahapatra","Maa"]) #output: ..., Mahapatra, ... , Maa, ...
│       # it's use for input many at a Time, & must use [ ]
│
│── Delete: pop, remove, clear
│   │── print=(var.pop()) #Rrandomly remove any one.
│   │── print=(var.remove(10))
│   └── print=(var.clear()) #Delete allin set.
```
#### Mathematical operations
```python
print(var.union(var2)) #add two sets & print all values in one time.
print(var | var2) #union using or operator

print(var.intersection(var2)) #only print unique values of two set.
print(var & var2) #intersection using operator.

print(var.difference(var2)) #only preset those values which not exist in two set.
print(var - var2)

print(var.symmetric_difference(var2)) #only print unique values from two sets.
```

---

## ☀️ Dictionary <a name="dictionary"></a>
- **Description**: Dictionaries store data as key-value pairs.
```python
dictionary = {'age': 21} #key value)
```
- Indexing & slicing not work.
- Insertion (input) ored is preserved.
- Hetrogenout element are allowed.
- Mutable in nature ✅
- `key` must be unique.

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

```python
var=dict()
var={}

var={"Name":"Akashdip","age":"21","place":"Haldia"}

print(var["age"])
print(var.pop("Name"))
print(var.get("Place"))
print(var.get("XYZ","Not available message"))
print(var.keys())  #output: All keys.
print(var.values())  #output: All values.
print(var.items())  #output: All keys,values

for key, values in var.items()
   print(key,values,sap=" - ") #sap is opsonal.

var.clear()
print(var) #output: enmty Dict.
```

---

# Operators
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

## Flow Control Statements <a name="flow-control-statement"></a>

```yaml
Flow Control Statements
│
│── Conditional Statements: If else
│── Iterative Statements: Loop
└── Trandfer Statement: break
                        continue
                        pass
```

## Conditional Statements <a name="conditional-statements"></a>
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

# Arrays
In Python, arrays can be implemented using lists, but for more advanced functionality, the `array` module or `numpy` library can be used.

**Example using lists:**
```python
# List as an array
numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # Accessing the first element
```

---

# Loops
Loops are used to execute a block of code repeatedly.

### For Loop
```python
var_name in range(start,end)
   statement
```      
```python
user_input = int(input("Enter a number: "))
# For loop
for i in range(1,11): #1 to 10
    print(user_input * i)
#output:
# Enter a number: 2
# 2
# ...
# 18
# 20
```
```python
user_input = int(input("Enter a number: "))
# For loop
for i in range(1,11):
    print(user_input,"X",i," = ", user_input * i)
#output:
# Enter a number: 5
# 5 X 1  =  5
# 5 X 2  =  10
# ...
# 5 X 9  =  45
# 5 X 10  =  50

```

### While Loop
```python
while condition:
   statement
```
```python
# While loop
count = 0
while count < 5:
    print(count)
    count += 1
#output:
# 0
# 1 
# 2
# 3
# 4
```
```python
# Mobile passward Unlock
password = "123XYZ"
user_password = input("Enter the pass: ")

while password != user_password:  # Loop until the password matches
    user_password = input("Enter the pass: ")  # Prompt user again

print("Unlocked !!")

```
---

## Trandfer Statement <a name="trandfer-statement"></a>

```yaml
Flow Control Statements
│
│── Conditional Statements - If else
│── Iterative Statements - Loop
└── Trandfer Statement: pass
                        continue
                        break
```
#### ✅ Pass
```python
if "a" in "akashdip":
    #print("a is present in akashdip")
    pass
```
###### Output:
```python
```
#### ✅ continue
```python
for num in range(1,11):
    if num % 2 == 0:
        continue #skip if number is even
    else:
        print(num)
```
###### Output:
```python
1
3
5
7
9
```
#### ✅ break
```python
for num in range(1,11):
    if num % 5 == 0: #break the loop if number is divisible by 5
        break
    else:
        print(num)
```
###### Output:
```python
1
2
3
4
```

---

## Modules

- Modules are nothing but group of functions, variable and classes that are saved to a file.
- use another py-code file in new python file using `import`
```python
import old # old.py
```
```yaml
Type
│
│── Pre defined
│    │
│    │── random
│    │── calender
│    └── keyword
│
└── User defined
     │
     │── old
     │── first
     └── akashdip
```
🚀 Pre defined module
```python
import calendar
print(calendar.month(2021, 1))

# output:

#     January 2021
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31
```
Example of using the `math` module:
```python
import math
print(math.sqrt(16))  # Outputs: 4.0
```
| Operation       | Description                     | Syntax                        |
|-----------------|---------------------------------|-------------------------------|
| Import module    | Import built-in or external module| `import module_name`        |

#### **Creating Your Own Module**
🚀 User defined module
**Example_01**

![module](https://github.com/user-attachments/assets/00e4a621-deaf-473b-93f8-639c46a0c1af)

**Example_02**
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

## Functions
- Functions are reusable blocks of code that perform a specific task.
- It's increse code reusability.
- we can pass value to the function called parameters.

```yaml
Type
│
│── Pre defined: Built-in Functions
│    │
│    │── len()
│    │── print()
│    └── type()
│
└── User defined: def
     │
     │── greet()
     │── fun()
     └── akashdip()
```

### Built-in Functions
Python provides many built-in functions like `len()`, `print()`, and `type()`.

**Example:**
```python
names = ["Alice", "Bob", "akashdip"]
print("Number of names:", len(names))  # Output: 3
```

### User-defined Functions
You can create your own functions using the `def` keyword.
```python
def function(parameter):
   body

function() #call the function
```
**Example:**
```python
def calculator(a,b):
   print("add :",a+b)
   print("sub :",a-b)

calculator(8,4)
calculator(2,6)
calculator(10,54)
calculator(254,23)
```
```python
def greet():
   print("Good morning")

greet() #output: Good morning
print(greet())  # Output: None because greet() function does not return anything
```
**BUT :**
```python
def greet():
   print("Good morning")

msg = greet()
print(msg) #output: None
```
```python
def greet():
   return"Good morning"

msg = greet()
print(msg) #output: Good morning
```
**Positional parameters** : (name)
```python
def greet(name):
    return f"Hello, {name}!"

# print(greet("Alice"))  # Output: Hello, Alice!
print(greet(input("Enter your name: ")))  # Output: Hello, [User Input Name]!
```
#### arguments <a name="parameters"></a>
```yaml
argument
│
│── positional parameters: You have to maintain the input orders.
│                          no of parameters = no of arguments.
│── keyword argument: You may not follow parameter's orders.
│                     keyword argument should follow positional argument.
│                     no of parameters = no of arguments.
└── default argument: You have to follow order.
                      no of parameters != no of arguments
```
### 🌳 positional argument <a name="positional-argument"></a>
```python
# positional argument
def greet(name,msg):
   print("Hello",name + ', ' + msg)
greet("Akash","Good Morning")
# output: Hello Akash, Good Morning
```
### 🌳 keyword argument <a name="keyword-argument"></a>
```python
# keyword argument
def greet(name,msg):
   print("Hello",name + ', ' + msg)

greet(msg="Good Morning",name="Akash") #You may not follow parameter's orders.
# output: Hello Akash, Good Morning
```
#### keyword argument should follow positional argument
```python
# keyword argument should follow positional argument
def greet(name,msg):
   print("Hello",name + ', ' + msg)
greet("Akash",msg="Good Morning")
# output: Hello Akash, Good Morning
```
### 🌳 default argument <a name="default-argument"></a>
```python
# default argument
def greet(name,msg="Good Morning"):
   print("Hello",name + ', ' + msg)
greet("Akash")
# output: Hello Akash, Good Morning
```
#### no of parameters = no of arguments
```python
# no of parameters = no of arguments
def greet(name,msg):
   print("Hello",name + ', ' + msg)
greet("Akash","Good Morning","How are you?")
# output: TypeError: greet() takes 2 positional arguments but 3 were given
```
---
# One short ✅
Functions in Python are defined using the `def` keyword.

**Syntax**: 
```python
def function_name(parameters):
    # Function body
```

**Example: 1**
```python
def calSum(a, b):
    x = (a*b)+(a/b)        # Calculate the expression
    print(x)               # Print the result

c = 9                     # Assign value to c
d = 8                     # Assign value to d
calSum(c, d)             # Call the function with c and d

```

**Example: 2**
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

# Strings
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

## Contents:
1. [Object-Oriented Programming (OOP)](#oop)
   - [Classes & Objects](#classes--objects)
   - [Inheritance](#inheritance)
   - [Encapsulation](#encapsulation)
   - [Polymorphism](#polymorphism)
2. [File Handling](#2-file-handling)
3. [Exception Handling](#3-exception-handling)
4. [Common Interview Questions](#common-interview-questions)
5. [Best Documentation Resources](#best-documentation-resources)
6. [**Projects**](#Projects)
7. [**EXAM**](#EXAM)

---

# 1. Object-Oriented Programming (OOP) <a name="oop"></a>

## ❌ POP: Procedure-Oriented Programming
- **Run Code line by line (like: jupyter notebook) using `Loops` & `Functions`.**
- We can't combnied single functions in Large projects.
- Can't easily manupulate codes.

## ✅ OOP [video](https://youtu.be/6soT3DMBJGQ)
- Work with `Objects`.
- We have `Class`, can combined `Variables` & `Functions`, and access this `classes` through `Obj`.
  
- OOP is a programming paradigm where you model **real-world things** as objects with attributes (data) and behaviors (methods).

```yaml
OOPS features
│
│── Class & Obj: class is a BluePrint which have no memeory, But through obj. we access the class's members(Variable & Functions).
│── inheritance: with this you can access a class obj. in another class.
│── encapsulation: bind Variables & Functions in a single unit. (Ex: Class)
│── abstraction: use for security, removing unnecessary details from an object to make it simpler and more efficient.
└── polymorphism: create multiple obj with a same class, for many operations.
```

## **Classes & Objects**
- **class**: A class defines a blueprint for creating objects. (No memory created).
- **Syntax**:
```python
class ClassName:
    # variables
    # methods
```
```python
class ClassName:
    def __init__(self, parameters):
        # Constructor
```
- **object**: Object is Real-World entity has some `properties` or `behaviour` whish is represented by `class Variables & methods`. it's create memory for class.
```python
obj_name = class_name()
```
**Example:**
```python
class A:
   pass
obj=A()
```

**Example:**  [video - Classes & Objects](https://youtu.be/pdEA5Qkgraw)
```python
#with default python constructor
class A:
    age=10
    print(age)

#output: 10 (One Time)
```
```python
class A:
    age=10
    print(age)
obj=A()
obj2=A()

#output: 10 (One Time)
```
###### ⬆️ with default python constructor, you have to print every time to get the value.
```python
#create a class with constructor
class A:
    def __init__(self): #self is default reference parameter which refers to the object
        age=10
        print(age)
obj=A()
obj2=A()

#output: 10
#        10
```
###### ⬆️ if you create your own constrictor, you must have an object.
```python
#call document object in side a function
class A:
    "Akashdip Mahapatra 01" #The document must in 1st line.
    age = 10
    "Akashdip Mahapatra 02" #output: None
    def fun(self):
        "Akashdip Mahapatra 03"
        name="Akash coding"
        print(self.age)
        print(name)
obj=A()
print(obj.age) # call through object
print(A.age) # call through class 
print(obj.__doc__)

obj.fun()
print(obj.fun.__doc__) # call through object
```
```python
# with default python constructor
class A:
    def fun(self,age,name,address):
        print(age," ",name," ",address)

obj=A()
obj.fun(10,"Akash","Kalkata")


# without default python constructor
class A:
    def __init__(self,age,name,address):
        print(age," ",name," ",address)

obj=A(10,"Akash","Kalkata")
```
 ⬆️ [Hard to understand](https://youtu.be/pdEA5Qkgraw)
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
### 🌳 Constructor ? <a name="constructor"></a>
- Constructor is a special function that gets `automaticall called` when object of class created.
- **purposes**: create and initialize the object.
```python
def __init__(self):
   #code
```
```python
#create 2 constructor
class A:
    def __init__(self):
        print("Akashdip")

    def __init__(self):
        print("Megha")

obj=A()

#output: Megha
# Always prefar the last one.
```
```yaml
constructor
│
│── default constructor: empty constructor with no parameters, add automatically by python.
└── parameteriged constructor: 
```
### ☀️ Default constructor <a name="default-constructor"></a>
**Syntax**:
```python
# default constructor:
class A:
    def __init__(self):
        print("This is default constructor")

obj=A()
```
```python
class A:
    name="Akashdip" #create a class variable (member)
    def __init__(self):
        print(self.name)

obj=A()
```
##### ⬇️ create a normal function (methode)
```python
class A:
    name="Akashdip"
    age=20

    def __init__(self):
        address="Kolkata" #member (local variable) inside constructor
        print(self.name)
        print(address) #No need to use self with local variable

    #normal methode
    def show(self): 
        print(self.age)

obj=A()
obj.show() #manually call the method.
```

### ☀️ Parameteriged constructor <a name="parameteriged-constructor"></a>
```python
# Parameteriged constructor
class A:
    def __init__(self,age,name,address):
        print(age," ",name," ",address)

obj=A(10,"Akash","Kalkata")
#output: 10   Akash   Kolkata
```
##### use None
```python
class A:
    def __init__(self,age,name,address):
        address="Kolkata" #optional
        print(age," ",name," ",address)

obj=A(10,"Akash",None)
#output: 10   Akash   Kolkata
```
---
### 🌳🌳 Access Modifires <a name="access-modifires"></a>

| **Name**  | **Access Modifier** | **Description**            | **Same Class** | **Same Package** | **Derived Class** `🛩️Inheritance` | **Other Classes** |
|-----------|---------------------|----------------------------|----------------|------------------|-------------------|-------------------|
| `van`     | **Public**          | Accessible from anywhere.  | ✅             | ✅               | ✅                | ✅                |
| `_van`    | **Protected**       | Accessible in the same class, same package, and derived (sub) classes. | ✅ | ✅               | ✅                | ❌                |
|| **Default (Package-Private)** | Accessible only within the same package. If no modifier is specified, this is the default. | ✅ | ✅               | ❌                | ❌                |
| `__van`   | **Private**         | Accessible only within the same class. | ✅ | ❌               | ❌                | ❌                |

### Notes:
- **Public**: Provides the highest level of accessibility, visible everywhere.
- **Protected**: Often used to allow derived classes to access parent class members, while still restricting access from unrelated classes outside the package.
- **Default**: Limits accessibility to classes within the same package. There is no explicit keyword for default access; it's implied when no modifier is specified.
- **Private**: Provides the most restricted access, available only within the class where it is defined.

### Examples
##### 🌳 use those members in only inside the class
```python
class A:
    a=10   # Public member
    _b=20  # Protected member
    __c=30 # Private member

    print("In same class:",a," ",_b," ",__c)  

#output:
# In same class: 10   20   30
```
```python
class A:
    a = 10   # Public member
    _b = 20  # Protected member
    __c = 30 # Private member
    print("In same class:",a," ",_b," ",__c) 
    # Constructor to print values inside the class
    def show(self):
        print("Inside the same class members:", self.a, self._b, self.__c)

# Creating an object of class A
obj = A()
obj.show()

#output:
# In same class: 10   20   30
# Inside the same class members: 10 20 30
```
##### 🌳 use those members outside the class
```python
class A:
    a = 10   # Public member
    _b = 20  # Protected member
    __c = 30 # Private member

obj = A()
#print("Outside the class:", obj.a, obj._b) #output:10   20
print("Outside the class:", obj.a, obj._b, obj.__c) #output: ⚠️ Error
```
```python
class Car:
    def __init__(self):
        self.van = "Public Variable"      # Public: accessible anywhere
        self._van = "Protected Variable"  # Protected: meant for internal use
        self.__van = "Private Variable"   # Private: name mangling applied

car = Car()
print(car.van)        # Accessible
print(car._van)       # Accessible but discouraged
print(car._Car__van)  # Accessing via name mangling (discouraged)
```
##### 🌳 create a another class - B, 🛩️ Inherit class - A 
```python
class A: #Parent class
    a = 10
    _b = 20
    __c = 30

class B(A): # Child class
    def show(self):
        print("Inherit class:", self.a, self._b)

obj=B()
obj.show() #output: Inherit class: 10 20
```
- use Public in antwhere.
- use Protected in 🛩️ Inherit class. ⬆️ 
- use private in only ❌ Parent class 

### Key Points
- **`van`**: No underscores. This is a public variable, accessible from anywhere.
- **`_van`**: Single underscore. Conventionally, it suggests a "protected" variable, but it can still be accessed from outside. It’s a hint to other developers.
- **`__van`**: Double underscore. Triggers name mangling to prevent accidental access, particularly in subclasses.

---
---

## 🛩️ **Inheritance**
###### If you access all properties of a class in other class called Inheritance.
- **Description**: Inheritance allows a class to inherit properties and methods from another class.
- **Syntax**:
```
class Father:
    # Properties

class Son(Father):
    # Properties
```
**Example 01:**
```python
class Father:
    def sky(self):
        print("sky is Blue")

class Son(Father):
    def grass(self):
        print("grass is Green")

#obj = Son()
X = Son() # X is an object of class Son
X.sky() # method of class Father (other class)
X.grass() # method of class Son (own class)
```
**Example 02:**
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

| **Type of Inheritance**    |
|----------------------------|
| |
| Single Inheritance         |
| Multiple Inheritance       |
| Multilevel Inheritance     |
| Hierarchical Inheritance   |
| Hybrid Inheritance         |

In object-oriented programming, **inheritance** allows a class to acquire properties and behaviors (methods) of another class. There are several types of inheritance:

---

### 1. 🛩️ **Single Inheritance** <a name="single-inheritance"></a>
   - A subclass inherits from only one superclass.
<img align="right" alt="python_logo" width="650" src="https://github.com/user-attachments/assets/dce45b71-bcbd-4e25-bc8e-d88baa36df14">
   
**Example**:
   ```python

     class Parent:
         pass

     class Child(Parent):
         pass
   ```
---

### 2. 🛩️ **Multiple Inheritance** <a name="multiple-inheritance"></a>
   - A subclass inherits from more than one superclass.
     <img align="right" alt="python_logo" width="550" src="https://github.com/user-attachments/assets/eae48197-63bf-4ec8-804d-5abe6aedcc66">

**Example**:
```python
     class Parent1:
         pass

     class Parent2:
         pass

     class Child(Parent1, Parent2):
         pass
```
   - In Python, multiple inheritance can lead to complexities, which are managed using the **Method Resolution Order (MRO)**.

---

### 3. 🛩️ **Multilevel Inheritance** <a name="multilevel-inheritance"></a>
   - A class inherits from a superclass, which in turn inherits from another superclass, forming a hierarchy.
<br>
     <img align="right" alt="python_logo" width="200" src="https://github.com/user-attachments/assets/b8942370-bc45-40b6-9c9d-f54207be4ce0">   

**Example**:
```python
     class Grandparent:
         pass

     class Parent(Grandparent):
         pass

     class Child(Parent):
         pass
```

---

### 4. 🛩️ **Hierarchical Inheritance** <a name="hierarchical-inheritance"></a>
   - Multiple subclasses inherit from the same superclass.
     <img align="right" alt="python_logo" width="480" src="https://github.com/user-attachments/assets/e7e19b6f-0b77-4017-87aa-5ba6be0a4329">
     
**Example**:
```python
     class Parent:
         pass

     class Child1(Parent):
         pass

     class Child2(Parent):
         pass
```

---

### 5. 🛩️ **Hybrid Inheritance** <a name="hybrid-inheritance"></a>
   - A combination of two or more types of inheritance, often involving multiple and multilevel inheritance. 
   - **Example**:
     ```python
     class Grandparent:
         pass

     class Parent1(Grandparent):
         pass

     class Parent2(Grandparent):
         pass

     class Child(Parent1, Parent2):
         pass
     ```
   - Hybrid inheritance can also lead to complex hierarchies and relies on MRO to resolve method conflicts.


---
---

## **Encapsulation**
```yaml
OOPS features
│
│── # Class & Obj: class is a BluePrint which have no memeory, But through obj. we access the class's members(Variable & Functions).
│── # inheritance: with this you can access a class obj. in another class.
│── encapsulation: bind Variables & Functions in a single unit. (Ex: Class)
│── # abstraction: use for security, removing unnecessary details from an object to make it simpler and more efficient.
└── # polymorphism: create multiple obj with a same class, for many operations.
```
- **Description**: Encapsulation hides private data and only allows access through public methods.
    - Python provides acces to all the variable and methods globally.
    - By using encapsulation acces globally by making it private at protected.
      
- **Syntax**: Use double underscore `__` to denote private variables.

| **Name**  | **Access Modifier** | **Description**            | **Same Class** | **Same Package** | **Derived Class** `🛩️Inheritance` | **Other Classes** |
|-----------|---------------------|----------------------------|----------------|------------------|-------------------|-------------------|
| `_van`    | **Protected**       | Accessible in the same class, same package, and derived (sub) classes. | ✅ | ✅               | ✅                | ❌                |
| `__van`   | **Private**         | Accessible only within the same class. | ✅ | ❌               | ❌                | ❌                |

**Example 01:**
```python
class A:
    _a=10 # protected #data
    __b=20 # private
    def dis_fun(self): #function, ----> &, data + Function = Encapsulation
        print(self._a)
        print(self.__b)

x=A() #object
x.dis_fun()

print("Outside of class ",x._a) #call using Class-obj
print("Outside of class ",x.__b)
## same output:
#print("Outside of class ",A._a) ✅ #call using Class-name
#print("Outside of class ",A.__b) ⚠️
```
output:
```go
PS C:\Users\akash\Desktop\Py Projects\Python-Projects> python -u "c:\Users\akash\Desktop\Py Projects\Python-Projects\00 Test\Encapsulation.py"
10 ✅
20 ✅
Outside of class  10 ✅ 
Traceback (most recent call last): ⚠️
  File "c:\Users\akash\Desktop\Py Projects\Python-Projects\00 Test\Encapsulation.py", line 12, in <module>
    print("Outside of class ",x.__b)
                              ^^^^^
AttributeError: 'A' object has no attribute '__b'
```
- we use __b only inside the class using Class-members
- we use _b also outside the class using Class-obj. 

**Example 02:**
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

## **Polymorphism**
```yaml
OOPS features
│
│── # Class & Obj: class is a BluePrint which have no memeory, But through obj. we access the class's members(Variable & Functions).
│── # inheritance: with this you can access a class obj. in another class.
│── # encapsulation: bind Variables & Functions in a single unit. (Ex: Class)
│── # abstraction: use for security, removing unnecessary details from an object to make it simpler and more efficient.
└── polymorphism: create multiple obj with a same class, for many operations.
      │
      │── Over-loading
      └── Over-riding
```
<img align="right" alt="python_logo" width="400" src="https://github.com/user-attachments/assets/22e41b7c-8422-45a5-a6bd-2d1751cd61b9"> 

##### ➡️ **same obj having different behaviour : like Me**
**Example 01:**
```python
print(5+5)     #output: 10 --> 1st time its add this
print("5"+"5") #output: 55 --> 2nd time its concate this.
```
**Example 02:**
The function is same (len), But it's change behaviour with values.
```python
print(len("Akashdip"))     #output: 8 --> find length caracter-wise.
print(len(["Akashdip","Arkadip"])) #output: 2 --> 2nd time fond len string-wise.
```
- **Description**: Polymorphism allows methods to be defined differently based on the object.
- **Syntax**: Define methods with the same name in different classes.

**Example 03:**
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
### ✈️ Over loading <a name="overloading"></a>
```python
#Over-loading
# The function is "show" but the behavior is different (based on the number of arguments)
# same functon but no of parameters are different
class A:
    def show(self):
        print("Wellcome")

    def show(self, firstname=''):
        print("Wellcome", firstname)

    def show(self, firstname='', lastname=''):
        print("Wellcome", firstname, lastname)

a = A()
a.show()                        #output: Wellcome
a.show('Akash')                 #output: Wellcome Akashdip
a.show('Akashdip', 'Mahapatra') #output: Wellcome Aka.. Ma...
```
⬆️ This called function Over-loading. one function can Over-load another function.
⚠️But also use: But it's not ❌ Polymorphism.
```python
class A:
    def show(self, firstname='', lastname=''):
        print("Wellcome", firstname, lastname)

a = A()
a.show()                        #output: Wellcome
a.show('Akash')                 #output: Wellcome Akashdip
a.show('Akashdip', 'Mahapatra') #output: Wellcome Aka.. Ma...
```
**Explane:**
##### Difference Between the Two Examples

1. **First Example**: Tries to define multiple `show` methods with different parameters (method overloading). However, **Python only keeps the last definition**, so only the last `show` method is used. This is not true ❓ polymorphism.

2. **Second Example**: Uses a single `show` method with default values for parameters. This lets it handle different numbers of arguments without needing multiple methods. This is **not polymorphism**; it’s just using default arguments.

---
### ✈️ Over riding <a name="overriding"></a>

❓ **true polymorphism** in Python, we can use **inheritance** and **method overriding**. This allows different classes to have methods with the same name but different implementations, which is a core principle of polymorphism.
**Example 01:**
```python
class A:
    def show(self, firstname='', lastname=''):
        print("Welcome", firstname, lastname)

class B(A):
    def show(self, firstname='', lastname=''):
        print("Hello from B:", firstname, lastname)

class C(A):
    def show(self, firstname='', lastname=''):
        print("Greetings from C:", firstname, lastname)

# Demonstrating polymorphism
a = A()
b = B()
c = C()

a.show("Alice", "Anderson")   # Output: Welcome Alice Anderson
b.show("Bob", "Brown")        # Output: Hello from B: Bob Brown
c.show("Charlie", "Clark")    # Output: Greetings from C: Charlie Clark
```
#### Explanation

- **Class `A`** has a `show` method that prints "Welcome".
- **Class `B`** and **Class `C`** inherit from `A` but **override** the `show` method with different messages.
- **Polymorphism** is demonstrated here because `show` behaves differently based on the object type (`A`, `B`, or `C`).

#### Key Point
With polymorphism, the same method name (`show`) can be used in different classes to perform different actions.

**Example 02:**
```python
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):  # Overriding the sound method in Animal
        print("Woof Woof")

class Cat(Animal):
    def sound(self):  # Overriding the sound method in Animal
        print("Meow Meow")

# Demonstrating overriding
animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()   # Output: Some generic animal sound
dog.sound()      # Output: Woof Woof
cat.sound()      # Output: Meow Meow
```

#### Explanation
- **Class `Animal`** has a method `sound` that gives a generic animal sound.
- **Class `Dog`** and **Class `Cat`** inherit from `Animal` but **override** the `sound` method to provide specific sounds.
- When calling `sound()` on `dog` and `cat`, we get behavior specific to `Dog` and `Cat`, respectively.

#### Key Point
In overriding, the subclass method **replaces** the superclass method. When we call `sound()` on a `Dog` or `Cat` object, we see the overridden version of `sound` defined in each subclass.

---

# 2. File Handling

- File is nothing but name of `memory location` on disk that stores data permanantly.
- Why not Variable, a=10 ❓ Because of, after code Run complete, the data auto Delete by system (pc)
- File Handling is a mechanism through, which we can handle (read, write, create, append, etc...) the file.

File handling is essential for reading and writing files in Python.

#### **Create a New file**
```python
f=open("C:\\Users\\...\\test.txt", "x")
print("File created Sucessfully .... !")
```
#### **Opening a File**
```python
file = open("test.txt", "r")
content = file.read()
print(content)
file.close()
```
#### ⚠️ **Exception Handling**
```python
try:
   with file = open("XYZ.txt", "r")
   print(file.readlines())
except:
   print("File may not exist ... create first !")
else:
   file.close()
   print("File Closed ... !")
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
#### **Read a File**
```python
print(file.read(30)) #for displaing 30 character.
print(file.readline()) #Display only one line.
```

| Operation       | Description                     | Syntax                        |
|-----------------|---------------------------------|-------------------------------|
| Write file      | Write to a file                | `file.write("content")`      |

#### **Using `with` Statement**
- Using `with` ensures proper file closure.
- The `with` statement is often used for file handling, as it ensures the file is properly closed after operations.
```python
with open("test.txt", "r") as file:
    content = file.read()
    print(content)
```
```python
with open("example.txt", "w") as file:   # Opens the file in write mode
    file.write("Hello, World!")          # Writes to the file
# File automatically closes after the with block
```

| Operation       | Description                     | Syntax                        |
|-----------------|---------------------------------|-------------------------------|
| Use `with`      | Automatically handles file closure | `with open(...) as file:`    |

### One Short ✅

#### file handling modes & operations:

| **Mode** | **Description**                          | **Syntax**                             | **Operation**                 |
|----------|------------------------------------------|----------------------------------------|-------------------------------|
| `'r'`    | Read mode (default)                      | `file = open("filename.txt","r")`     | Opens file for reading. File must exist. |
|||||
| `'w'`    | Write mode                               | `file = open("filename.txt","w")`     | Opens file for writing. Creates a new file if it doesn't exist, or truncates it if it does. |
|||||
| `'a'`    | Append mode                              | `file = open("filename.txt","a")`     | Opens file for appending. Creates file if it doesn’t exist. Writes data at the end of the file. |
|||||
| `'x'`    | Exclusive creation                       | `file = open("filename.txt","x")`     | Creates a new file and opens it for writing. Fails if the file exists. |
|||||
| `'r+'`   | Read and write mode                      | `file = open("filename.txt","r+")`    | Opens file for both reading and writing. File must exist. |
|||||
| `'w+'`   | Write and read mode                      | `file = open("filename.txt","w+")`    | Opens file for reading and writing. Truncates the file if it exists or creates a new one. |
|||||
| `'a+'`   | Append and read mode                     | `file = open("filename.txt","a+")`    | Opens file for reading and appending. Creates a new file if it doesn’t exist. |
|||||
| `'t'`    | Text mode (default)                      | `file = open("filename.txt","rt")`    | Opens file in text mode. Can be combined with other modes like `r`, `w`, `a`. |
|||||
| `'b'`    | Binary mode                              | `file = open("filename.txt","rb")`    | Opens file in binary mode. Can be combined with other modes like `r`, `w`, `a`. Used for non-text files like images. |

---

### Common File Operations

| **Operation**          | **Syntax**                   | **Description**                                                |
|------------------------|------------------------------|----------------------------------------------------------------|
| Open a file            | `file = open("filename", "mode")` | Opens the specified file in the specified mode.              |
| Read entire file       | `content = file.read()`      | Reads the entire content of the file.                         |
| Read one line          | `line = file.readline()`     | Reads a single line from the file.                            |
| Read all lines         | `lines = file.readlines()`   | Reads all lines and returns them as a list.                   |
| Write to file          | `file.write("text")`         | Writes the specified text to the file.                        |
| Append to file         | `file.write("text")`         | Appends the specified text at the end of the file in `'a'` mode. |
| Close file             | `file.close()`               | Closes the file and frees up system resources.                |
| Iterate lines          | `for line in file:`          | Iterates through each line in the file.                       |

#### ✅ **Copy File**
```python
try:
    source_path = "C:\\Users\\akash\\Desktop\\Py Projects\\Python-Projects\\00 Test\\File Handling\\a.txt"
    destination_path = "C:\\Users\\akash\\Desktop\\Py Projects\\Python-Projects\\00 Test\\File Handling\\B.txt"
    
    with open(source_path, "r") as file_01:
        with open(destination_path, "w") as file_02:
            for line in file_01: # Read line by line
                file_02.write(line)  # Write line by line
    
except FileNotFoundError:
    print("Source file not found. Please check the file path.")
except PermissionError:
    print("Permission denied. Check read/write permissions.")
except Exception as e:
    print("An error occurred:", e)
else:
    print("File Copied Successfully")
```
#### ✅ **Delete File**
```python
# Delete File
f_path = "C:\\Users\\akash\\Desktop\\Py Projects\\Python-Projects\\00 Test\\File Handling\\a.txt"

import os
if os.path.exists(f_path): #1st check if the file is exist or not?
    os.remove(f_path)
else:
    print("File not available ... !")
```

---

# 3. Exception Handling
- It's nothing but `runtime-errors`.
- It's occurs due to incorrect implementation of logic.

Exceptions allow you to handle errors gracefully.

#### **Try-Except Block**
Example:
```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
```
```python
a=int(input("Enter 1st no: "))
b=int(input("Enter 2nd no: "))

try:
    x = a/b
    print("The ans is : ",x)
except:
    print("can't division by zero")

print("Thanks")

#output:
# Enter 1st no: 1
# Enter 2nd no: 0
# can't division by zero
# Thanks ✅
```
```python
a=int(input("Enter 1st no: "))
b=int(input("Enter 2nd no: "))

try:
    x = a/b
    print("The ans is : ",x)
except:
    print("can't division by zero")
else:
    print("Thanks")

#output_01:
# Enter 1st no: 1 
# Enter 2nd no: 0
# can't division by zero ⚠️
# ❌

# #output_02:
# Enter 1st no: 9
# Enter 2nd no: 3
# The ans is :  3.0 ✅
# Thanks ✅
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
# Multi Threading <a name="multi-threading"></a>

Multi Threading is a technique which allows a CPU to execute multiple threads (small small programs) of one process at a same Time.

### ☁️ Why MultiThreading ?
The purpose od MultiThreading is to run multiple task & functions at the same time.

### ☁️ Single-Threading Vs Multi-Threading
<img align="middle" alt="python_logo" width="800" src="https://github.com/user-attachments/assets/4b9d4275-aec4-4712-a796-61fcd3d28b77"> 

### ☁️ What is Thread ?
- Thread is a `pre-define class` which is available in `threading module`.
- Thread is a basic unit of CPU & it is well known for independent execution.

#### ☁️ Thread class methods:

| **Method**               | **Description**                                                                                   |
|--------------------------|---------------------------------------------------------------------------------------------------|
| `start()`                | Starts the thread’s activity by calling its `run` method.                                         |
| `run()`                  | Defines the thread’s activity. Called when `start()` is invoked; can be overridden in a subclass. |
| `join(timeout=None)`     | Waits for the thread to finish; optional `timeout` specifies max time to wait.                    |
| `is_alive()`             | Returns `True` if the thread is still running; otherwise, `False`.                               |
| `getName()`              | Returns the name of the thread.                                                                   |
| `setName(name)`          | Sets a new name for the thread.                                                                   |
| `isDaemon()`             | Returns `True` if the thread is a daemon thread; otherwise, `False`.                              |
| `setDaemon(daemonic)`    | Sets the thread as a daemon thread (`True`) or a non-daemon thread (`False`).                     |
| `current_thread()`       | Returns the current thread object; used to get the main or any active thread.                     |
| `active_count()`         | Returns the number of currently active threads.                                                   |
| `enumerate()`            | Lists all active thread objects.                                                                  |

#### ☁️☁️ **Single Threading:** Run one by one using only one Thread (MAIN THREAD) by default in Python.
###### To experiance the 10 sec time ---> use sleep class from Time package. So it can exicute every line after 1 sec.
<img align="right" alt="singleThreading" width="400" src="https://github.com/user-attachments/assets/3dd81f06-dd26-44d3-b33d-1647500a51fd"> 

```python
## Single Threading
#from time import sleep
class A:
    def run(self):
        for i in range(5):
            print("Hello")
#           sleep(1)
                                       # output:
class B:                               # Hello
    def run(self):                     # Hello
        for i in range(5):             # Hello
            print("Hi")                # Hello
#           sleep(1)                   # Hello
                                       # Hi
t1 = A()                               # Hi
t2 = B()                               # Hi
                                       # Hi
t1.run()                               # Hi
t2.run()                               

```
#### ☁️☁️ **Multi Threading:** Run at same time using threads (parallel execution).
```python
# #Multi Threading
from time import sleep
from threading import Thread

class A(Thread):  # Inherit from Thread
    def run(self):  # Correctly define the run method
        for i in range(5):
            print("Hello")
            sleep(1)

class B(Thread):  # Inherit from Thread
    def run(self):  # Correctly define the run method
        for i in range(5):
            print("Hi")
            sleep(1)

# Create instances of A and B
t1 = A()
t2 = B()

# Start the threads
t1.start()
t2.start()


# output:
# Hello
# Hi
# HiHello

# HelloHi

# Hi
# Hello
# Hi
# Hello
```
```python
# Start the threads
# ⬆️ ... 
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

# output:
# Hello
# Hi
# Hello
# Hi
# Hello
# Hi
# Hello
# Hi
# Hello
# Hi
```

---

# Common Interview Questions
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

# Best Documentation Resources
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

---

### Projects

```yaml
Py Projects
│
│── Python Projects
│── Django Projects
│     │
│     │── Twitter: (under Devlopment)
│     └── ...
└── ...    
```

| [notes](https://github.com/akashdip2001/ML-Machine-Learning/blob/main/py/README.md) | [Python Projects](https://github.com/akashdip2001/Python-Projects) | [Django Projects](https://github.com/akashdip2001/pyTweet) | [python-advance](https://github.com/akashdip2001/python-advance) |
| --- | --- | --- | --- |

<div style="display: flex; justify-content: space-around;">
   <img src="sources/pdf/img/python_roadmap.jpg" alt="python projects" style="width: 28%; height: auto;"/>
  <img src="sources/pdf/img/python_projects.jpg" alt="python projects" style="width: 35%; height: auto;"/>
  <img src="sources/pdf/img/python_H@cking_projects.jpg" alt="pythonprojects" style="width: 35%; height: auto;"/>
</div>

<div style="display: flex; justify-content: space-around;">
  <img src="sources/pdf/img/python_projects_01.jpg" alt="python project" style="width: 32%; height: auto;"/>
  <img src="sources/pdf/img/python_projects_02.jpg" alt="python project" style="width: 31%; height: auto;"/>
  <img src="sources/pdf/img/python_projects_03.jpg" alt="python project" style="width: 30%; height: auto;"/>
</div>

<img src="https://github.com/akashdip2001/college-final-year-project/blob/main/img/colour_line.png">

# EXAM

# 1) Problem 01

<img align="right" alt="python_logo" width="300" src="https://github.com/user-attachments/assets/9bdddbd5-70c8-4aea-9a61-91a4acaafb55"> 

This programming task requires finding the first moment when all traffic lights are green at various intersections.

### Problem Breakdown
- You are given a grid (2D array) where each row represents a traffic light's status at different time moments.
- Each column in the grid represents a specific moment in time, with traffic lights either:
  - `0` (Red)
  - `1` (Green)
- You need to find the first time moment where all lights are green (i.e., all elements in a column are `1`). If no such moment exists, return `-1`.

### Input and Output
- **Input**:
  - `input1`: Number of traffic lights, `N` (number of rows in the grid).
  - `input2`: Number of time moments, `T` (number of columns in the grid).
  - `input3`: 2D array `A` of size `N x T` where each element is either `0` or `1`.
- **Output**:
  - An integer representing the first moment (index) when all lights are green, or `-1` if there is no such moment.

### Example Walkthrough
1. **Example 1**:
   - **Input**:
     ```
     input1 = 3
     input2 = 5
     input3 = [
       [1, 0, 1, 0, 1],
       [0, 1, 1, 1, 0],
       [1, 1, 1, 0, 0]
     ]
     ```
   - At moment 2 (index `2`), all lights are green (i.e., all elements in the third column are `1`).
   - **Output**: `2`

2. **Example 2**:
   - **Input**:
     ```
     input1 = 3
     input2 = 4
     input3 = [
       [0, 1, 0, 1],
       [1, 0, 1, 1],
       [0, 1, 1, 1]
     ]
     ```
   - There is no time moment where all lights are green.
   - **Output**: `-1`

### Solution ✅
1. Loop over each time moment (column) in the array.
2. Check if all elements in the current column are `1`.
3. Return the index of the first such column. If none are found, return `-1`.

Here’s the Python code implementing this logic:

```python
class UserMainCode(object):
    @classmethod
    def temperatureFluctuation(cls, input1, input2, input3):
        # Loop through each time moment (column)
        for t in range(input2):
            all_green = True
            # Check if all traffic lights are green at this time moment
            for light in range(input1):
                if input3[light][t] == 0:
                    all_green = False
                    break
            # If all are green, return the time moment
            if all_green:
                return t
        # If no moment was found where all are green, return -1
        return -1
```

### Explanation of Code
1. **Loop through each time moment**: We go column by column (using `t` as the index) to check each moment in time.
2. **Check for green lights**: For each column, we check if all rows (lights) are `1`. If any light is `0`, we skip to the next time moment.
3. **Return first all-green moment**: If a column with all `1`s is found, we return the index of this column.
4. **Return `-1` if no such column is found**: If the loop finishes without finding any all-green column, we return `-1`.

### Complexity
- **Time Complexity**: \(O(N \times T)\), where \(N\) is the number of lights, and \(T\) is the number of time moments, as we check each cell in the grid once.
- **Space Complexity**: \(O(1)\), as we only use a few additional variables.

---

# 2) Problem 02

<img align="right" alt="python_logo" width="300" src="https://github.com/user-attachments/assets/05e3c8f8-754e-413c-bebd-9ea0f646993b"> 

The problem is about determining the party with the highest total votes across multiple blocks. If two or more parties have the same total votes, the party that appears earlier in the given list of party names should be declared the winner.

### Problem Breakdown
1. **Input Specifications**:
   - `input1`: An integer, `N`, representing the number of blocks.
   - `input2`: A string representing party names.
   - `input3`: An integer array where each row contains the votes each party received in a block.

2. **Output**:
   - A string in the format: `"PartyName TotalVotes"` for the party with the highest total votes.
   - If there's a tie, the party that appears earlier in `input2` wins.

3. **Example**:
   - **Example 1**:
     - Input:
       ```
       input1 = 5
       input2 = "B,A,A,A,B"
       input3 = [30, 20, 30, 20, 30]
       ```
     - Party `B` and `A` both have a total of 60 votes, but since `B` appears first, `B` is declared the winner.
   - **Example 2**:
     - Input:
       ```
       input1 = 10
       input2 = "A,B,D,C,A,B,D,A,A,C"
       input3 = [49, 40, 20, 30, 15, 6, 22, 10, 12, 29]
       ```
     - Party `A` has the highest total of 86 votes, so the output is `"A 86"`.

### Solution Approach
1. Parse the `input2` string to get the list of winning parties in each block.
2. Initialize a dictionary to store the total votes for each party.
3. Loop through the list of blocks and add the corresponding votes from `input3` to each party’s total.
4. Determine the party with the highest votes. In case of a tie, select the one that appears first in `input2`.

### Python Code

```python
class UserMainCode(object):
    @classmethod
    def electionResult(cls, input1, input2, input3):
        # Split input2 to get the parties in each block
        parties = input2.split(',')
        
        # Dictionary to store total votes for each party
        vote_counts = {}
        
        # Loop over each block and add votes to the respective party
        for i in range(input1):
            party = parties[i]
            votes = input3[i]
            if party in vote_counts:
                vote_counts[party] += votes
            else:
                vote_counts[party] = votes

        # Find the party with the highest votes
        max_votes = -1
        winner_party = ""
        
        for party in parties:
            if party in vote_counts:
                if vote_counts[party] > max_votes:
                    max_votes = vote_counts[party]
                    winner_party = party
                elif vote_counts[party] == max_votes:
                    # If there is a tie, prioritize the first occurrence in `parties` list
                    if winner_party == "":
                        winner_party = party
                    elif parties.index(party) < parties.index(winner_party):
                        winner_party = party

        # Return the result in the specified format
        return f"{winner_party} {max_votes}"
```

### Explanation of Code

1. **Parse Input**:
   - `parties` holds the list of party names for each block.
2. **Vote Aggregation**:
   - `vote_counts` dictionary accumulates votes for each party.
3. **Determine Winner**:
   - `max_votes` keeps track of the highest vote count.
   - `winner_party` stores the name of the current winning party.
   - If two parties have the same vote count, the one appearing first in `parties` is chosen.
4. **Output Format**:
   - Returns the name and total votes of the winning party in the specified format.

### Example Execution

- For **Example 1** with `input2 = "B,A,A,A,B"` and `input3 = [30, 20, 30, 20, 30]`:
  - `vote_counts` becomes `{'B': 60, 'A': 60}`.
  - `B` wins as it appears first, so output is `"B 60"`.

### Complexity
- **Time Complexity**: \(O(N)\) for iterating through the blocks.
- **Space Complexity**: \(O(P)\) for storing votes per party, where \(P\) is the number of unique parties.

### Tasting the Code
```python
# Example usage:
# For input1 = 5, input2 = ["B", "A", "A", "A", "B"], input3 = [30, 20, 20, 30, 20]
print(UserMainCode.electionResult(5, ["B", "A", "A", "A", "B"], [30, 20, 20, 30, 20]))  # Expected output: "B 60"

# For input1 = 10, input2 = ["A", "B", "D", "C", "A", "B", "D", "A", "A", "C"], input3 = [49, 20, 40, 30, 15, 60, 22, 10, 12, 29]
print(UserMainCode.electionResult(10, ["A", "B", "D", "C", "A", "B", "D", "A", "A", "C"], [49, 20, 40, 30, 15, 60, 22, 10, 12, 29]))  # Expected output: "A 86"
```

---
