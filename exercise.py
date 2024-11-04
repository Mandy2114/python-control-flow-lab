# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

# Exercise 1: Vowel or Consonant
#
def check_letter():
    letter = input ("Enter a letter (a-z or A-z): ").lower()
    if letter in 'aeiou':
        print(f"The letter {letter} is a vowel.")
    elif letter.isalpha():
        print(f'The letter {letter} is a consonant.')
    else:
        print(f'Enter a alphabet letter.')

check_letter()

# Exercise 2: Old enough to vote?
#
def check_voting_eligibility():
    age = input ("Please enter your age: ")
    age = int(age)

    if age < 0:
        print('Enter a positive number.')
    elif age >= 18:
        print('You are eligible to vote.')
    else:
        print('Sorry, you are not eligible to vote.')

check_voting_eligibility()

# Exercise 3: Calculate Dog Years
# 
def calculate_dog_years():
    age = input("Input a dog's age: ")
    age = int(age)

    if age < 0:
        print("Enter a positive number.")
    elif age <= 2:
        dog_years = age * 10
    else:
        dog_years = 20 + ( age - 2 ) * 7
        print(f"The dog's age in dog years is {dog_years}.")
   
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    cold = input("Is it cold (Yes/No): ").lower() == 'yes'
    raining = input("Is it raining (Yes/No): ").lower() == 'yes'

    if cold and raining:
        print("Wear a waterproff coat.")
    elif cold and not raining:
        print("Wear a warm coat.")
    elif raining and not cold:
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")

weather_advice()

# Exercise 5: What's the Season?
#
def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ")
    day = input("Enter the day of the month: ")

    day = int(day)
    month = month.strip().lower()

    if (month == 'dec' and day >= 21 ) or (month == 'jan') or (month == 'feb') or (month == 'mar' and day < 20):
        season = 'winter'
    elif (month == 'mar' and day >= 20) or (month == 'apr') or (month == 'may') or (month == 'jun' and day < 21):
        season = 'Spring'
    elif (month == 'jun' and day >= 21) or (month == 'jul') or (month == 'aug') or (month == 'sep' and day < 22):
        season = 'Summer'
    elif (month == 'sep' and day >= 22) or (month == 'oct') or (month == 'nov') or (month == 'dec' and day < 21):
        season = 'Fall'
    else:
        print(f"Enter the correct month and day. Months inbetween (Jan-Dec) and the day should be a valid day of the month")
        return
    
    print(f"{month.capitalize()} {day} is in {season}.")
    
determine_season()




