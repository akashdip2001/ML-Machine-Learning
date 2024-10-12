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
11.	Write a program to find the simple interest when the value of principle,rate of interest and time period is given.
12.	Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.
13.	Write  a program that will tell whether the given number is divisible by 3 & 6.
14.	Calculate the angle between the hour hand and minute hand.
15.	Write a program that will determine weather when the value of temperature and humidity is provided by the user.
TEMPERATURE(C)      HUMIDITY(%)      WEATHER

      >= 30                             >=90                Hot and Humid
      >= 30                             < 90                 Hot
      <30                                >= 90               Cool and Humid
      <30                                 <90                 Cool
16.	Write a program that will take three digits from the user and add the square of each digit.
17.	Write a program that will check whether the number is armstrong number or not.
18.	Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.
19.	Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _   – 30%)(0-1lakh print k).
20.	Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit
21.	Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
22.	Write a program that will swap numbers
23.	Write a program to find the sum of first n numbers, where n will be provided by the user. Eg if the user provides n=10 the output should be 55.
24.	Write a program that can multiply 2 numbers provided by the user without using the * operator
25.	Write a program that can find the factorial of a given number provided by the user.
26.	Write a program to print the first 25 odd numbers
27.	Write a program to print whether a given number is prime number or not
28.	Print all the armstrong numbers in the range of 100 to 1000
29.	The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 years. For eg current population is 10000 so the output should be like this:
10th year - 10000
9th year - 9000
8th year - 8100 and so on
30.	Write a program to print all the unique combinations of 1,2,3 and 4.
31.	User will provide 2 numbers you have to find the HCF of those 2 numbers
32.	User will provide 2 numbers you have to find the by LCM of those 2 numbers
33.	Print first 25 prime numbers
34.	Print the first 20 numbers of a Fibonacci series
35.	Write a program to find the compound interest 
36.	Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
37.	Take a number from the user and find the number of digits in it. 
38.	Print all factors of a given number provided by the user.
39.	Find the reverse of a number provided by the user(any number of digit) 
40.	Write a program to print the following pattern
```go
*
**
***
****
*****
```
41.	Write a program to print the following pattern
```go
*
**
***
**
*
```
42.	Write  a program to print the following pattern
```go
        *
      * * *
    * * * * *
   * * * * * * *
* * * * * * * * *
```
43.	Write a program to print the following pattern
```go
1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
```   	
45.	Write a program to print the following pattern
```go
1
2 3
4 5 6
7 8 9 10
```  	
47.	Write a program to calculate the sum of the following series till the nth term
1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!
n will be provided by the user

49.	Write a Python Program to Find the Sum of the Series till the nth term: 
1 + x^2/2 + x^3/3 + … x^n/n
n will be provided by the user





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

### Problem 11: Simple Interest Calculation
**Question:** Write a program to find the simple interest when the values of principal, rate of interest, and time period are given.

**Answer:**
```python
# Input principal, rate of interest, and time period from the user
principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in %): "))
time_period = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = (principal * rate_of_interest * time_period) / 100

# Output the result
print("The simple interest is:", simple_interest)
```

**Explanation:**
- The formula for simple interest is \( \text{SI} = \frac{\text{P} \times \text{R} \times \text{T}}{100} \).
- The user inputs the principal, rate, and time, which are converted to floats for calculation.
- The result is printed.

**Output Example:**
If the user inputs `10000`, `5`, and `3`, the output will be:
```
The simple interest is: 1500.0
```

---

### Problem 12: Volume of Cylinder and Cost of Milk
**Question:** Write a program to find the volume of the cylinder and calculate the cost when the cost of 1 litre of milk is Rs. 40.

**Answer:**
```python
import math

# Input radius and height from the user
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate the volume of the cylinder
volume = math.pi * radius**2 * height

# Calculate the cost
cost_per_litre = 40
cost = volume * cost_per_litre

# Output the results
print(f"The volume of the cylinder is: {volume:.2f} litres")
print(f"The cost of the milk is: Rs. {cost:.2f}")
```

**Explanation:**
- The volume of a cylinder is calculated using the formula \( V = \pi r^2 h \).
- The cost is calculated by multiplying the volume by the cost per litre.
- The results are formatted to two decimal places for clarity.

**Output Example:**
If the user inputs `7` for radius and `10` for height, the output will be:
```
The volume of the cylinder is: 1539.38 litres
The cost of the milk is: Rs. 6157.50
```

---

### Problem 13: Divisibility Check
**Question:** Write a program that will tell whether the given number is divisible by 3 and 6.

**Answer:**
```python
# Input a number from the user
number = int(input("Enter a number: "))

# Check divisibility by 3 and 6
if number % 3 == 0 and number % 6 == 0:
    print(f"The number {number} is divisible by both 3 and 6.")
else:
    print(f"The number {number} is not divisible by both 3 and 6.")
```

**Explanation:**
- The program checks the divisibility of the input number using the modulus operator `%`.
- If both conditions are true, it indicates divisibility.

**Output Example:**
If the user inputs `12`, the output will be:
```
The number 12 is divisible by both 3 and 6.
```

---

### Problem 14: Angle Between Hour and Minute Hand
**Question:** Calculate the angle between the hour hand and minute hand.

**Answer:**
```python
# Input hours and minutes from the user
hours = int(input("Enter hours (0-12): "))
minutes = int(input("Enter minutes (0-59): "))

# Calculate the angles
hour_angle = (hours % 12) * 30 + (minutes / 60) * 30  # 30 degrees per hour
minute_angle = minutes * 6  # 6 degrees per minute

# Calculate the angle between the two hands
angle = abs(hour_angle - minute_angle)
angle = min(angle, 360 - angle)  # Smaller angle

# Output the result
print(f"The angle between the hour hand and minute hand is: {angle} degrees.")
```

**Explanation:**
- The angle for the hour hand is calculated as \( \text{Hour} \times 30 + \frac{\text{Minutes}}{60} \times 30 \).
- The angle for the minute hand is \( \text{Minutes} \times 6 \).
- The absolute difference gives the angle, and the smaller angle is taken if it exceeds 180 degrees.

**Output Example:**
If the user inputs `3` for hours and `30` for minutes, the output will be:
```
The angle between the hour hand and minute hand is: 15.0 degrees.
```

---

### Problem 15: Weather Based on Temperature and Humidity
**Question:** Write a program that will determine weather conditions based on temperature and humidity.

**Answer:**
```python
# Input temperature and humidity from the user
temperature = float(input("Enter temperature in Celsius: "))
humidity = float(input("Enter humidity in percentage: "))

# Determine the weather condition
if temperature >= 30 and humidity >= 90:
    weather = "Hot and Humid"
elif temperature >= 30:
    weather = "Hot"
elif temperature < 30 and humidity >= 90:
    weather = "Cool and Humid"
else:
    weather = "Cool"

# Output the result
print("The weather condition is:", weather)
```

**Explanation:**
- The program uses a series of `if-elif-else` statements to check conditions for temperature and humidity.
- It outputs the determined weather condition.

**Output Example:**
If the user inputs `32` for temperature and `95` for humidity, the output will be:
```
The weather condition is: Hot and Humid
```

---

### Problem 16: Sum of Squares of Three Digits
**Question:** Write a program that will take three digits from the user and add the square of each digit.

**Answer:**
```python
# Input three digits from the user
digits = input("Enter three digits: ")

# Calculate the sum of the squares of each digit
sum_of_squares = sum(int(digit) ** 2 for digit in digits)

# Output the result
print("The sum of the squares of the digits is:", sum_of_squares)
```

**Explanation:**
- The input string is iterated over, converting each character to an integer and squaring it.
- The `sum()` function computes the total.

**Output Example:**
If the user inputs `123`, the output will be:
```
The sum of the squares of the digits is: 14
```

---

### Problem 17: Armstrong Number Check
**Question:** Write a program that will check whether the number is an Armstrong number or not.

**Answer:**
```python
# Input a number from the user
number = int(input("Enter a number: "))

# Calculate the number of digits
num_of_digits = len(str(number))

# Calculate the sum of the cubes of its digits
sum_of_cubes = sum(int(digit) ** num_of_digits for digit in str(number))

# Check if the number is an Armstrong number
if sum_of_cubes == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
```

**Explanation:**
- The program first determines the number of digits.
- It computes the sum of each digit raised to the power of the number of digits.
- Finally, it checks if this sum equals the original number.

**Output Example:**
If the user inputs `153`, the output will be:
```
153 is an Armstrong number.
```

---

### Problem 18: Narcissist Number Check
**Question:** Write a program that will take user input of a four-digit number and check whether the number is a narcissist number or not.

**Answer:**
```python
# Input a four-digit number from the user
number = int(input("Enter a four-digit number: "))

# Calculate the sum of the fourth powers of its digits
sum_of_powers = sum(int(digit) ** 4 for digit in str(number))

# Check if the number is a narcissist number
if sum_of_powers == number:
    print(f"{number} is a narcissist number.")
else:
    print(f"{number} is not a narcissist number.")
```

**Explanation:**
- The program calculates the sum of each digit raised to the power of 4 (since it’s a four-digit number).
- It checks if this sum equals the original number.

**Output Example:**
If the user inputs `1634`, the output will be:
```
1634 is a narcissist number.
```

---

### Problem 19: In-Hand Salary Calculation
**Question:** Write a program that will give you the in-hand salary after deductions (HRA, DA, PF, and tax based on salary brackets).

**Answer:**
```python
# Input gross salary from the user
gross_salary = float(input("Enter your gross salary: "))

# Deductions
HRA = gross_salary * 0.10
DA = gross_salary * 0.05
PF = gross_salary * 0.03
deductions = HRA + DA + PF

# Calculate net salary
net_salary = gross_salary - deductions

# Tax Calculation
if 500000 < gross_salary

 <= 1000000:
    tax = net_salary * 0.10
elif 1000000 < gross_salary <= 2000000:
    tax = net_salary * 0.20
elif gross_salary > 2000000:
    tax = net_salary * 0.30
else:
    tax = 0

# Final in-hand salary
in_hand_salary = net_salary - tax

# Output the result
if gross_salary <= 100000:
    print("No tax applicable. In-hand salary:", in_hand_salary)
else:
    print("In-hand salary after deductions:", in_hand_salary)
```

**Explanation:**
- The program calculates deductions for HRA, DA, and PF based on percentages.
- It calculates the net salary and applies tax based on the specified brackets.
- It outputs the final in-hand salary, indicating if no tax is applicable.

**Output Example:**
If the user inputs `750000`, the output will be:
```
In-hand salary after deductions: 617500.0
```

---

### Problem 20: Unit Conversion Menu
**Question:** Write a menu-driven program to convert between different units:
1. cm to ft
2. kl to miles
3. USD to INR
4. Exit

**Answer:**
```python
# Conversion rates
cm_to_ft = 0.0328084
kl_to_miles = 0.621371
usd_to_inr = 82.67  # Example conversion rate

while True:
    print("\nMenu:")
    print("1. cm to ft")
    print("2. kl to miles")
    print("3. USD to INR")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        cm = float(input("Enter centimeters: "))
        ft = cm * cm_to_ft
        print(f"{cm} cm is equal to {ft:.2f} ft")
    elif choice == 2:
        kl = float(input("Enter kilometers: "))
        miles = kl * kl_to_miles
        print(f"{kl} km is equal to {miles:.2f} miles")
    elif choice == 3:
        usd = float(input("Enter USD: "))
        inr = usd * usd_to_inr
        print(f"{usd} USD is equal to {inr:.2f} INR")
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
```

**Explanation:**
- The program displays a menu and prompts the user to select an option.
- It performs the respective conversion based on user input.
- The loop continues until the user chooses to exit.

**Output Example:**
```
Menu:
1. cm to ft
2. kl to miles
3. USD to INR
4. Exit
Enter your choice: 1
Enter centimeters: 100
100.0 cm is equal to 3.28 ft
```

---

### Problem 21: Counting Dogs and Chickens
**Question:** Write a program that will tell the number of dogs and chickens when the user provides the total number of heads and legs.

**Answer:**
```python
# Input total heads and legs
heads = int(input("Enter the total number of heads: "))
legs = int(input("Enter the total number of legs: "))

# Using equations: 
# Let d = number of dogs, c = number of chickens
# d + c = heads
# 4d + 2c = legs

# Solving equations
# c = legs / 2 - heads
# d = heads - c

chickens = (legs // 2) - heads
dogs = heads - chickens

# Output the result
print(f"Number of dogs: {dogs}, Number of chickens: {chickens}")
```

**Explanation:**
- The program uses the equations based on the heads and legs of dogs and chickens to find their counts.
- It outputs the calculated number of each.

**Output Example:**
If the user inputs `10` for heads and `34` for legs, the output will be:
```
Number of dogs: 6, Number of chickens: 4
```

---

### Problem 22: Swap Numbers
**Question:** Write a program that will swap two numbers.

**Answer:**
```python
# Input two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Swap using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Output the swapped values
print("After swapping:")
print(f"First number: {num1}")
print(f"Second number: {num2}")
```

**Explanation:**
- The program takes two numbers as input and uses a temporary variable to swap their values.
- The swapped values are then printed.

**Output Example:**
If the user inputs `5` and `10`, the output will be:
```
After swapping:
First number: 10.0
Second number: 5.0
```

---

### Problem 23: Sum of First n Numbers
**Question:** Write a program to find the sum of the first n numbers, where n will be provided by the user.

**Answer:**
```python
# Input n from the user
n = int(input("Enter a number: "))

# Calculate the sum of the first n numbers
sum_of_n = sum(range(1, n + 1))

# Output the result
print(f"The sum of the first {n} numbers is: {sum_of_n}")
```

**Explanation:**
- The program uses the `range()` function to create a list of numbers from 1 to n and sums them using the `sum()` function.
- The result is printed.

**Output Example:**
If the user inputs `10`, the output will be:
```
The sum of the first 10 numbers is: 55
```

---

### Problem 24: Multiplication Without `*` Operator
**Question:** Write a program that can multiply two numbers provided by the user without using the `*` operator.

**Answer:**
```python
# Input two numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Multiply using addition
product = 0
for _ in range(abs(num2)):  # Loop through num2 times
    product += num1

# Adjusting for negative values
if (num1 < 0) ^ (num2 < 0):  # If one is negative and the other is positive
    product = -product

# Output the result
print(f"The product of {num1} and {num2} is: {product}")
```

**Explanation:**
- The program adds `num1` to itself `num2` times to simulate multiplication.
- It checks for negative numbers and adjusts the product accordingly.

**Output Example:**
If the user inputs `5` and `3`, the output will be:
```
The product of 5 and 3 is: 15
```

---

### Problem 25: Factorial Calculation
**Question:** Write a program that can find the factorial of a given number provided by the user.

**Answer:**
```python
# Input a number from the user
number = int(input("Enter a number: "))

# Calculate factorial
factorial = 1
for i in range(1, number + 1):
    factorial *= i

# Output the result
print(f"The factorial of {number} is: {factorial}")
```

**Explanation:**
- The program uses a loop to multiply numbers from 1 to the input number to compute the factorial.
- The result is printed.

**Output Example:**
If the user inputs `5`, the output will be:
```
The factorial of 5 is: 120
```

---

### Problem 26: Print First 25 Odd Numbers
**Question:** Write a program to print the first 25 odd numbers.

**Answer:**
```python
# Print the first 25 odd numbers
print("The first 25 odd numbers are:")
for i in range(1, 50, 2):  # Start from 1, go till 50, step by 2
    print(i, end=' ')
```

**Explanation:**
- The loop starts from 1 and goes up to 50 with a step of 2 to get odd numbers.
- It prints them in a single line.

**Output Example:**
```
The first 25 odd numbers are:
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49
```

---

### Problem 27: Prime Number Check
**Question:** Write a program to print whether a given number is a prime number or not.

**Answer:**
```python
# Input a number from the user
number = int(input("Enter a number: "))

# Check for prime
if number > 1:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
```

**Explanation:**
- The program checks if the number is greater than 1 and tests divisibility from 2 to the square root of the number.
- It outputs whether the number is prime.

**Output Example:**
If the user inputs `11`, the output will be:
```
11 is a prime number.
```

---

### Problem 28: Armstrong Numbers in Range
**Question:** Print all the Armstrong numbers in the range of 100 to 1000.

**Answer:**
```python
# Find Armstrong numbers in the range of 100 to 1000
print("Armstrong numbers between 100 and 1000 are:")
for num in range(100, 1000):
    # Calculate the sum of cubes of its digits
    sum_of_cubes = sum(int(digit) ** 3 for digit in str(num))
    if sum_of_cubes == num:
        print(num, end=' ')
```

**Explanation:**
- The program iterates through each number in the specified range and calculates the sum of the cubes of its digits.
- If the sum equals the

 original number, it is printed as an Armstrong number.

**Output Example:**
```
Armstrong numbers between 100 and 1000 are:
153 370 371 407
```

---

### Problem 29: Population Growth Calculation
**Question:** Calculate the population of a town over the last 10 years given the current population and growth rate.

**Answer:**
```python
# Initial population
population = 10000
growth_rate = 0.10  # 10% growth rate

# Calculate and print the population for each of the last 10 years
for year in range(10, 0, -1):
    print(f"{year} year(s) ago - Population: {int(population)}")
    population /= (1 + growth_rate)  # Reverse the growth for previous year
```

**Explanation:**
- The program uses a loop to calculate the population for each of the last 10 years by reversing the growth rate.
- It prints the population for each year.

**Output Example:**
```
10 year(s) ago - Population: 10000
9 year(s) ago - Population: 9090
8 year(s) ago - Population: 8264
7 year(s) ago - Population: 7513
...
```

---

### Problem 30: Unique Combinations of Numbers
**Question:** Print all the unique combinations of 1, 2, 3, and 4.

**Answer:**
```python
from itertools import combinations

# Generate and print unique combinations of 1, 2, 3, and 4
numbers = [1, 2, 3, 4]

print("Unique combinations of 1, 2, 3, and 4:")
for r in range(1, len(numbers) + 1):
    for combo in combinations(numbers, r):
        print(combo)
```

**Explanation:**
- The program uses `itertools.combinations` to generate all unique combinations of the numbers from size 1 to 4.
- It prints each combination.

**Output Example:**
```
Unique combinations of 1, 2, 3, and 4:
(1,)
(2,)
(3,)
(4,)
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)
(1, 2, 3)
(1, 2, 4)
(1, 3, 4)
(2, 3, 4)
(1, 2, 3, 4)
```

---

### Problem 31: Find HCF (Highest Common Factor)
**Question:** User will provide two numbers, and you have to find the HCF of those two numbers.

**Answer:**
```python
import math

# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate HCF using math.gcd
hcf = math.gcd(num1, num2)

# Output the result
print(f"The HCF of {num1} and {num2} is: {hcf}")
```

**Explanation:**
- The program uses Python's built-in `math.gcd()` function to compute the highest common factor of the two input numbers.
- It outputs the calculated HCF.

**Output Example:**
If the user inputs `48` and `18`, the output will be:
```
The HCF of 48 and 18 is: 6
```

---

### Problem 32: Find LCM (Lowest Common Multiple)
**Question:** User will provide two numbers, and you have to find the LCM of those two numbers.

**Answer:**
```python
import math

# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate LCM using the formula: LCM(a, b) = abs(a*b) // HCF(a, b)
lcm = abs(num1 * num2) // math.gcd(num1, num2)

# Output the result
print(f"The LCM of {num1} and {num2} is: {lcm}")
```

**Explanation:**
- The program calculates the LCM using the formula that relates LCM and HCF, employing the `math.gcd()` function.
- It outputs the computed LCM.

**Output Example:**
If the user inputs `4` and `5`, the output will be:
```
The LCM of 4 and 5 is: 20
```

---

### Problem 33: Print First 25 Prime Numbers
**Question:** Print the first 25 prime numbers.

**Answer:**
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Print the first 25 prime numbers
count = 0
num = 2

print("The first 25 prime numbers are:")
while count < 25:
    if is_prime(num):
        print(num, end=' ')
        count += 1
    num += 1
```

**Explanation:**
- The program defines a function to check for prime numbers and uses a loop to find and print the first 25 prime numbers.
- It increments the count and checks each subsequent number for primality.

**Output Example:**
```
The first 25 prime numbers are:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```

---

### Problem 34: Print First 20 Fibonacci Numbers
**Question:** Print the first 20 numbers of a Fibonacci series.

**Answer:**
```python
# Print the first 20 Fibonacci numbers
a, b = 0, 1
print("The first 20 Fibonacci numbers are:")
for _ in range(20):
    print(a, end=' ')
    a, b = b, a + b
```

**Explanation:**
- The program initializes the first two Fibonacci numbers and iteratively computes and prints the next numbers in the series.
- It continues for 20 iterations.

**Output Example:**
```
The first 20 Fibonacci numbers are:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
```

---

### Problem 35: Calculate Compound Interest
**Question:** Write a program to find the compound interest.

**Answer:**
```python
# Input principal, rate of interest, and time period from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))

# Calculate compound interest
amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

# Output the result
print(f"The compound interest is: {compound_interest:.2f}")
```

**Explanation:**
- The program takes the principal amount, rate of interest, and time period as inputs and calculates the compound interest using the formula.
- It outputs the calculated compound interest.

**Output Example:**
If the user inputs a principal of `10000`, a rate of `5`, and a time of `2`, the output will be:
```
The compound interest is: 1025.00
```

---

### Problem 36: Compute n + nn + nnn
**Question:** Write a Python program that accepts an integer \( n \) and computes the value of \( n + nn + nnn \).

**Answer:**
```python
# Input an integer from the user
n = input("Enter an integer: ")

# Compute n + nn + nnn
nn = n * 2  # String concatenation
nnn = n * 3  # String concatenation
result = int(n) + int(nn) + int(nnn)

# Output the result
print(f"The result of {n} + {nn} + {nnn} is: {result}")
```

**Explanation:**
- The program concatenates the string representation of \( n \) to create \( nn \) and \( nnn \), converts them to integers, and calculates the sum.
- It prints the resulting value.

**Output Example:**
If the user inputs `5`, the output will be:
```
The result of 5 + 55 + 555 is: 615
```

---

### Problem 37: Count Digits in a Number
**Question:** Take a number from the user and find the number of digits in it.

**Answer:**
```python
# Input a number from the user
number = input("Enter a number: ")

# Count digits
num_digits = len(number)

# Output the result
print(f"The number of digits in {number} is: {num_digits}")
```

**Explanation:**
- The program takes the number as a string input and uses `len()` to count the digits.
- It outputs the count of digits.

**Output Example:**
If the user inputs `12345`, the output will be:
```
The number of digits in 12345 is: 5
```

---

### Problem 38: Print All Factors of a Given Number
**Question:** Print all factors of a given number provided by the user.

**Answer:**
```python
# Input a number from the user
number = int(input("Enter a number: "))

# Print factors
print(f"The factors of {number} are:")
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=' ')
```

**Explanation:**
- The program iterates from 1 to the input number and checks divisibility to find and print the factors.

**Output Example:**
If the user inputs `12`, the output will be:
```
The factors of 12 are:
1 2 3 4 6 12
```

---

### Problem 39: Find the Reverse of a Number
**Question:** Find the reverse of a number provided by the user (any number of digits).

**Answer:**
```python
# Input a number from the user
number = input("Enter a number: ")

# Find the reverse
reverse_number = number[::-1]

# Output the result
print(f"The reverse of {number} is: {reverse_number}")
```

**Explanation:**
- The program uses string slicing to reverse the number and prints it.

**Output Example:**
If the user inputs `12345`, the output will be:
```
The reverse of 12345 is: 54321
```

---

### Problem 40: Print a Pattern
**Question:** Write a program to print the following pattern:
```go
*
**
***
****
*****
```

**Answer:**
```python
# Print pattern
for i in range(1, 6):
    print('*' * i)
```

**Explanation:**
- The program uses a loop to print asterisks for each row, multiplying the asterisk character by the current row number.

**Output Example:**
```
*
**
***
****
*****
```

---

### Problem 41: Print a Diamond Pattern
**Question:** Write a program to print the following pattern:
```go
*
**
***
**
*
```

**Answer:**
```python
# Print the first half of the pattern
for i in range(1, 4):
    print('*' * i)

# Print the second half of the pattern
for i in range(2, 0, -1):
    print('*' * i)
```

**Explanation:**
- The program uses two loops: the first loop prints increasing rows of asterisks, and the second loop prints decreasing rows.
- The outer loop runs from 1 to 3 for the increasing part, while the second loop runs from 2 to 1 for the decreasing part.

**Output Example:**
```
*
**
***
**
*
```

---

### Problem 42: Print a Pyramid Pattern
**Question:** Write a program to print the following pattern:
```go
        *
      * * *
    * * * * *
   * * * * * * *
* * * * * * * * *
```

**Answer:**
```python
# Number of rows
rows = 5

# Print the pyramid pattern
for i in range(rows):
    # Print leading spaces
    print(' ' * (rows - i - 1), end='')
    # Print asterisks
    print('* ' * (2 * i + 1))
```

**Explanation:**
- The program uses a single loop to control the number of rows and prints leading spaces followed by asterisks in a specific format.
- The number of asterisks printed is `2 * i + 1` to ensure the correct odd count for each row.

**Output Example:**
```
        * 
      * * * 
    * * * * * 
   * * * * * * * 
* * * * * * * * * * 
```

---

### Problem 43: Print a Numeric Pyramid Pattern
**Question:** Write a program to print the following pattern:
```go
1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
```

**Answer:**
```python
# Number of rows
rows = 5

# Print the numeric pyramid pattern
for i in range(1, rows + 1):
    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end=' ')
    # Print decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end=' ')
    # Move to the next line
    print()
```

**Explanation:**
- The program has a nested loop: the outer loop controls the rows, and the inner loops print increasing and then decreasing sequences of numbers for each row.
- The first inner loop prints numbers from 1 to `i`, while the second inner loop prints numbers from `i-1` down to 1.

**Output Example:**
```
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 
```

---

### Problem 44: Print an Incremental Number Pattern
**Question:** Write a program to print the following pattern:
```go
1
2 3
4 5 6
7 8 9 10
```

**Answer:**
```python
# Initialize starting number
num = 1

# Number of rows
rows = 4

# Print the incremental number pattern
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()  # Move to the next line
```

**Explanation:**
- The program uses a nested loop to print an increasing number of integers on each row.
- It maintains a counter (`num`) that increments with each printed number.

**Output Example:**
```
1 
2 3 
4 5 6 
7 8 9 10 
```

---

### Problem 45: Calculate the Sum of a Series
**Question:** Write a program to calculate the sum of the following series till the nth term:
```
1/1! + 2/2! + 3/3! + 4/4! + ... + n/n!
```
**Answer:**
```python
import math

# Input n from the user
n = int(input("Enter the value of n: "))

# Initialize sum
sum_series = 0

# Calculate the sum of the series
for i in range(1, n + 1):
    sum_series += i / math.factorial(i)

# Output the result
print(f"The sum of the series till {n} terms is: {sum_series:.6f}")
```

**Explanation:**
- The program uses a loop to compute each term of the series by dividing `i` by `i!`, utilizing the `math.factorial()` function.
- It adds each term to a running total (`sum_series`) and prints the final result.

**Output Example:**
If the user inputs `4`, the output will be:
```
The sum of the series till 4 terms is: 2.708333
```

---

### Problem 46: Calculate the Sum of Another Series
**Question:** Write a Python Program to Find the Sum of the Series till the nth term:
```
1 + x^2/2 + x^3/3 + … + x^n/n
```
**Answer:**
```python
# Input n and x from the user
n = int(input("Enter the value of n: "))
x = float(input("Enter the value of x: "))

# Initialize sum
sum_series = 0

# Calculate the sum of the series
for i in range(1, n + 1):
    sum_series += (x ** i) / i

# Output the result
print(f"The sum of the series till {n} terms for x = {x} is: {sum_series:.6f}")
```

**Explanation:**
- The program takes two inputs: the number of terms `n` and the value of `x`.
- It calculates each term in the series by computing \( x^i/i \) and adds it to `sum_series`.

**Output Example:**
If the user inputs `4` for `n` and `2` for `x`, the output will be:
```
The sum of the series till 4 terms for x = 2.0 is: 4.500000
```

---



