# Q1
a = 10
a = a + 2
print(a*2)
a = 19
print(a+3)
a = a // 2
print(a) # Have to print to see final value the variable takes

# Q2
print(2+3*6/2)

# Q3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

# Q4
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
print(palindrome("1414884937242655719669145562427394884141")) # Not a palindrome
print(palindrome("6800923757255865070000705685527573290086"))
print(palindrome("6892149109325320763773670235239019412986"))
print(palindrome("9847255590886266818998186626880955527489"))

# Q5 - Write a function that finds all the occurrences of a certain pattern, that starts with “un” has unlimited number of letters and ends with “an”
# The function takes 1 parameter: the text to look into and returns the number of matches.
# Use only the things we have learned in class. Give some explanations besides the code.
def find_pattern(text):
    """
    Function to find occurrences of words that start with "un" and end with "an"
    :param text: The input text to search in
    :return: The number of matches found
    """
    words = text.split()  # Split text into words
    count = 0  # Counter for matches

    for word in words:
        # Check if the word starts with "un" and ends with "an"
        if word.startswith("un") and word.endswith("an"):
            count += 1  # Increment count if condition is met

    return count

# Example usage
text = "unhuman unclean uncertain unknown unusual"
print(find_pattern(text))  # Output: Number of matches


# Q6 -
list_example = ["My", "name", "is", "Nathan"]
list_example.append("Fernandez")
print(list_example)

# Q7 - Continue by replacing the numbers greater than 80 with their corresponding negative value (90 will be replaced with -90).
# Also replace the number lower than 40 with the sum of their digits: 39 is replaced by 12. print the list at the end
# Use only what we have learned in class. Provide some explanation in the form of comments.
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
print(random_numbers)

# Replacing numbers in the original list:

for i in range(len(random_numbers)): # Iterate over all numbers in list
    if random_numbers[i] > 80: # Set condition to find numbers greater than 80 using i to index
        random_numbers[i] = -(random_numbers[i]) # Replace >80 with negative version of number
    elif random_numbers[i] < 40: # Set condition to find numbers less than 40 using i to index
        random_numbers[i] = sum(int(digit) for digit in str(random_numbers[i])) # Replace with sum of their digits
print(f"Altered list {random_numbers}") # New list

# Q8 - Write a function that checks if the passed parameter is a valid URL or not.
# Please also explain your reasoning. Use only the concepts that we learned in class

def is_valid_url(url):
    """
    Checks if the given string is a valid URL based on basic structure.
    :param url: String to check
    :return: True if valid, False otherwise
    """
    # A valid URL should start with "http://" or "https://"
    if not (url.startswith("http://") or url.startswith("https://")):
        return False

    # Extract the part after "http://" or "https://"
    url = url.split("//")[1]

    # A valid URL should have at least one dot (.) in the domain name
    if "." not in url:
        return False

    # A valid URL should not have spaces
    if " " in url:
        return False

    return True

# Example usage
print(is_valid_url("https://example.com"))  # True

# Q9 - Given your birthday, in the format "DD-MM-YYYY", write a function that calculates how many days have passed since your birthday (without counting the days in your birth year and the current year, so just whole years).
# The function takes your birthday as a parameter in string format.
# Do not import anything, use only what we learned in class
def days_since_birthday(birthday):
    """
    Calculates how many days have passed since the user's birthday,
    considering only whole years between the birth year and the current year.

    :param birthday: A string in the format "DD-MM-YYYY"
    :return: The total number of days
    """
    # Extract birth year
    year = int(birthday.split("-")[2])

    # Define the current year (assuming it's 2025)
    current_year = 2025

    # Calculate the number of full years between birth year and current year
    full_years = current_year - year - 1  # Excluding birth year and current year

    # Calculate total days assuming non-leap years
    total_days = full_years * 365

    # Count leap years in between
    leap_days = 0
    for y in range(year + 1, current_year):  # Only count years in between
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            leap_days += 1

    return total_days + leap_days


# Example usage
print(days_since_birthday("15-06-2000"))  # Output will be the total days passed
