# Python Variables Practice: 30 Tasks
# Instructions: Complete each task by writing the code below the comment.

# --- Level 1: The Basics (Naming & Assignment) ---

# 1. Create a variable named 'city' and assign it the name of your hometown.
city = "Vosloorus"
print("Question 1: ", city)
# 2. Create a variable 'age' and set it to your age.
age = 30
print("question 2: ", age)
# 3. Assign the value 100 to a variable called 'score'.
score = 100
print("Question 3: ", score)
# 4. Create a variable 'is_sunny' and set it to True.
is_sunny = bool(True)
print("Question 4: ", is_sunny)
# 5. Reassign the 'score' variable from task 3 to a new value: 150.
swap = score = 150
#score = 150
print("Question 5: ", score)
# 6. Create two variables, 'x' and 'y', and assign them both the value 5 on a single line.
x = 5
y = 5
print("Question 6: X=", x , "Y=", y)
# 7. Rename the illegal variable '2_cool' to something valid.
Too_cool = str
# 8. Create a variable using snake_case (e.g., user_favorite_color).
user_favourite_color = "Green"
print("Question 8: ", user_favourite_color)
# 9. Swap the values of two variables, a = 10 and b = 20, so a is 20 and b is 10.
a = 10
b = 20
swap = a,b = b,a
print("Question 9: A=",a, "B=", b)
# 10. Create a variable 'pi' and assign it the value 3.14159.
pi = float(3.14159)
print("Question 10: Pi = ", pi)


# --- Level 2: Data Types & Conversion ---

# 11. Use the type() function to check the data type of 'age'.
age_type = type(age)
print("Question 11: ", age_type)
# 12. Create a string 'price_str = "19.99"' and convert it to a float.
price_str = "19.99"
price_str = float(price_str)
print("Question 12: R", price_str)
# 13. Convert the float 9.99 into an integer. 
new_price_float = float(9.99)
new_price_int = int(new_price_float)
print("Question 13: ", new_price_int)
# 14. Create a variable 'greeting' that combines a string and your 'city' variable.
#Greetings = "Hey, I'm Sihle and I live in ", city
Greet = "Hey, I'm Sihle and I live in "
Greetings = Greet , city
print("Question 14: ", Greetings)
# 15. Use an f-string to print: "I am [age] years old and live in [city]."
print("Question 15: ", f"I am {age} years old and live in {city}.")
# 16. Create a variable with a long string and use len() to find its length.
Long_str = "I have so much work to do, but I'm ready for that"
print("Question 16: ", len(Long_str))
# 17. Use input() to store a name in a variable called 'user_name'.
#User_name = input("Enter your user name: ")
#print(f"Question 17: , {User_name}")
# 18. Ask a user for their birth year, convert to int, and calculate their current age.
#Birth_year = int(input("Enter your year of birth : "))
#Current_year = 2026
#Current_age = (Current_year - Birth_year)
#print("Question 18: ", Current_age)
# 19. Create a boolean variable that checks if 10 is greater than 5.
Greater = bool(10 > 5 )
# 20. Create a variable 'nothing' and assign it the value None.
nothing = None
print("Question 20: ", nothing)


# --- Level 3: Basic Math with Variables ---

# 21. Create 'length = 10' and 'width = 5'. Calculate 'area' in a new variable.
length = 10
width = 5
Area = length * width
print("Question 21: The Area is: ", Area)
# 22. Create 'count = 0'. Increment it by 1 using the += operator.
Count = 0
print("Question 22: ", Count + 1)
# 23. Calculate the remainder of 10 / 3 using the modulo operator (%).
Remainder = 10%3
print("Question 23: ", Remainder)
# 24. Create 'base = 2' and 'exponent = 3'. Calculate 2 to the power of 3.
Base = 2
Exponent = 3
Power = Base ** Exponent
print("Question 24: ", Power)
# 25. Find the average of three variables: test1, test2, and test3.
test_1 = 87
test_2 = 90
test_3 = 99
Average = ((test_1 + test_2 + test_3)/3)
print("Question 25: ", Average)
# 26. Create 'price = 50'. Calculate a 10% discount and store the final price.
price = 50
discount = 0.1
final_price = (price - (price * discount))
print("Question 26: R", final_price)
# 27. Convert a 'fahrenheit' variable to 'celsius' using: (F - 32) * 5/9.
weather = int(input())
#fahrenheit = 500
celcius = int((weather-32)* (5/9))
if celcius >= 32:
    print(celcius, "Its Hot")
elif celcius <= 10:
    print(celcius, "Its Cold")
# 28. Create 'seconds = 3660'. Convert this into minutes and remaining seconds.
seconds = int(3660)
minutes = seconds / 60
print("Question 28: ", minutes)
# 29. Use a variable to store the result of 10 // 3 (floor division).

# 30. Create a 'wallet' variable with 100. Subtract three 'purchase' variables from it.