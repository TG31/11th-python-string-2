# Exercise 1
def is_valid_email(text):
    count_att = 0
    count_dot = 0
    for i in text:
        if i == "@":
            count_att += 1
        elif i == ".":
            count_dot += 1
    if count_att == 1 and count_dot == 1:
        return "Valid"
    else:
        return "Invalid"
print(is_valid_email("hello@gmail.com"))

# Exercise 2
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    for i in vowels:
        text = text.replace(i, "")
    return text

print(remove_vowels("Please call me tomorrow"))

# Exercise 3
def get_initials(text):
    

# Exercise 4
def extract_year(text):
    # Write your code here
    pass

# Exercise 5
def is_palindrome(text):
    # Write your code here
    pass
