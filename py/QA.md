# Python Practice Problems

1.	User will input (3ages).Find the oldest one
2.	Write a program that will convert celsius value to fahrenheit
3.	User will input (2numbers).Write a program to swap the numbers
4.	Write a program that will give you the sum of 3 digits
5.	Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
6.	Write a program that will tell whether the number entered by the user is odd or even.
7.	Write a program that will tell whether the given year is a leap year or not.
8.	Write a program to find the euclidean distance between two coordinates.
9.	Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.
10.	Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

---

### Problem 1: Find the Oldest Age
**Question:** User will input three ages. Find the oldest one.

**Answer:**
```python
# Input ages from the user
ages = input("Enter three ages separated by spaces: ").split()
ages = [int(age) for age in ages]  # Convert input strings to integers

# Find the oldest age
oldest_age = max(ages)

# Output the result
print("The oldest age is:", oldest_age)
```

**Explanation:**
- `input("...")`: Prompts the user to enter data.
- `.split()`: Splits the input string into a list using spaces as delimiters.
- `int(age) for age in ages`: List comprehension to convert the string list to an integer list.
- `max(ages)`: Finds the maximum value in the list, which is the oldest age.
- `print()`: Outputs the oldest age.

**Output Example:**
If the user inputs `23 35 29`, the output will be:
```
The oldest age is: 35
```

---

### Problem 2: Celsius to Fahrenheit Conversion
**Question:** Write a program that will convert a Celsius value to Fahrenheit.

**Answer:**
```python
# Input Celsius value from the user
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Output the result
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
```

**Explanation:**
- `float(input("..."))`: Takes a floating-point number as input.
- The formula for conversion is `(Celsius * 9/5) + 32`.
- `print()`: Outputs the result with formatted strings.

**Output Example:**
If the user inputs `25`, the output will be:
```
25.0 degrees Celsius is equal to 77.0 degrees Fahrenheit.
```

---

### Problem 3: Swap Two Numbers
**Question:** User will input two numbers. Write a program to swap the numbers.

**Answer:**
```python
# Input two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Swapping using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Output the swapped numbers
print("After swapping: First number =", num1, ", Second number =", num2)
```

**Explanation:**
- Two numbers are inputted and stored in `num1` and `num2`.
- A temporary variable `temp` is used to hold the value of `num1` during the swap.
- The values are then swapped and printed.

**Output Example:**
If the user inputs `5` and `10`, the output will be:
```
After swapping: First number = 10.0 , Second number = 5.0
```

---

### Problem 4: Sum of Three Digits
**Question:** Write a program that will give you the sum of three digits.

**Answer:**
```python
# Input three digits from the user
digits = input("Enter three digits separated by spaces: ").split()
digits = [int(digit) for digit in digits]  # Convert input strings to integers

# Calculate the sum
sum_of_digits = sum(digits)

# Output the result
print("The sum of the three digits is:", sum_of_digits)
```

**Explanation:**
- Similar to previous problems, input is taken and split into a list.
- `sum(digits)`: Computes the sum of the elements in the list.
- The result is printed.

**Output Example:**
If the user inputs `3 5 7`, the output will be:
```
The sum of the three digits is: 15
```

---

### Problem 5: Reverse a Four-Digit Number
**Question:** Write a program that will reverse a four-digit number and check whether the reverse is the same as the original.

**Answer:**
```python
# Input a four-digit number from the user
number = input("Enter a four-digit number: ")

# Reverse the number
reversed_number = number[::-1]

# Check if the reversed number is equal to the original
is_palindrome = number == reversed_number

# Output the results
print("Reversed number is:", reversed_number)
if is_palindrome:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
```

**Explanation:**
- `number[::-1]`: Slices the string in reverse order to get the reversed number.
- The equality check (`==`) determines if the original and reversed numbers are the same.
- Outputs both the reversed number and whether it's a palindrome.

**Output Example:**
If the user inputs `1221`, the output will be:
```
Reversed number is: 1221
The number is a palindrome.
```

---

### Problem 6: Odd or Even
**Question:** Write a program that will tell whether the number entered by the user is odd or even.

**Answer:**
```python
# Input a number from the user
number = int(input("Enter a number: "))

# Check if the number is odd or even
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```

**Explanation:**
- `number % 2`: Computes the remainder when `number` is divided by 2.
- An `if` statement checks if the remainder is zero (even) or not (odd).
- Outputs the result accordingly.

**Output Example:**
If the user inputs `4`, the output will be:
```
The number is even.
```

---

### Problem 7: Leap Year Check
**Question:** Write a program that will tell whether the given year is a leap year or not.

**Answer:**
```python
# Input a year from the user
year = int(input("Enter a year: "))

# Check for leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

**Explanation:**
- Leap year rules are checked using a compound `if` condition.
- The output indicates whether the input year is a leap year.

**Output Example:**
If the user inputs `2020`, the output will be:
```
2020 is a leap year.
```

---

### Problem 8: Euclidean Distance
**Question:** Write a program to find the Euclidean distance between two coordinates.

**Answer:**
```python
import math

# Input coordinates from the user
x1, y1 = map(float, input("Enter coordinates x1 y1: ").split())
x2, y2 = map(float, input("Enter coordinates x2 y2: ").split())

# Calculate Euclidean distance
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Output the result
print("The Euclidean distance is:", distance)
```

**Explanation:**
- The `math.sqrt` function calculates the square root.
- The formula for Euclidean distance is applied: \(\sqrt{(x2 - x1)^2 + (y2 - y1)^2}\).
- The result is printed.

**Output Example:**
If the user inputs `1 2` and `4 6`, the output will be:
```
The Euclidean distance is: 5.0
```

---

### Problem 9: Triangle Formation Check
**Question:** Write a program that takes user input of three angles and finds out whether it can form a triangle.

**Answer:**
```python
# Input three angles from the user
angles = list(map(int, input("Enter three angles separated by spaces: ").split()))

# Check if the angles can form a triangle
if len(angles) == 3 and sum(angles) == 180:
    print("The angles can form a triangle.")
else:
    print("The angles cannot form a triangle.")
```

**Explanation:**
- The angles are input and converted to integers using `map()`.
- The program checks if there are exactly three angles and if their sum equals 180.
- Outputs whether a triangle can be formed.

**Output Example:**
If the user inputs `60 60 60`, the output will be:
```
The angles can form a triangle.
```

---

### Problem 10: Profit or Loss
**Question:** Write a program that takes user input of cost price and selling price to determine whether it's a loss or a profit.

**Answer:**
```python
# Input cost price and selling price from the user
cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

# Determine profit or loss
if selling_price > cost_price:
    print("You made a profit of:", selling_price - cost_price)
elif selling_price < cost_price:
    print("You incurred a loss of:", cost_price - selling_price)
else:
    print("There is no profit or loss.")
```

**Explanation:**
- The cost and selling prices are taken as input and converted to floats.
- An `if-elif-else` statement checks for profit, loss, or break-even conditions.
- Outputs the result accordingly.

**Output Example:**
If the user inputs `100` for cost price and

 `120` for selling price, the output will be:
```
You made a profit of: 20.0
```

---
