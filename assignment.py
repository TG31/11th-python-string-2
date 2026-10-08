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

# Exercise 2
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    for i in vowels:
        text = text.replace(i, "")
    return text

# Exercise 3
def get_initials(text):
    words = text.split()
    initials = ""

    for word in words:
        initials += word[0].upper() + "."

    return initials

# Exercise 4
def extract_year(text):
    words = text.split()

    for word in words:
        number = ""

        for i in word:
            if i.isdigit():
                number += i

        if len(number) == 4:
            return number

    return False

# Exercise 5
def is_palindrome(text):
    clean_text = ""

    for i in text:
        if i.isalnum():
            clean_text += i.lower()

    return clean_text == clean_text[::-1]
