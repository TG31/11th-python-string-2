# Exercise 1
def is_valid_email(text):
    if "@" not in text or "." not in text:
        return "Invalid"
    parts = text.split("@")
    if len(parts) != 2:
        return "Invalid"
    if parts[0] == "" or parts[1] == "":
        return "Invalid"
    if "." not in parts[1]:
        return "Invalid"
    if parts[1].startswith(".") or parts[1].endswith("."):
        return "Invalid"
    return "Valid"

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
