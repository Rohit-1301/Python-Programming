# Sample string
sample = " Hello, World! "

# Common string functions
lowercase = sample.lower()         # Convert to lowercase
uppercase = sample.upper()         # Convert to uppercase
titlecase = sample.title()         # Convert to title case
strip = sample.strip()             # Remove leading and trailing whitespace
replace = sample.replace("World", "Python")  # Replace a substring
split = sample.split(",")          # Split string by a delimiter
join = " ".join(["Hello", "Python"]) # Join a list of strings with a space
find = sample.find("World")        # Find the index of a substring
startswith = sample.startswith(" Hello") # Check if string starts with a substring
endswith = sample.endswith("!")    # Check if string ends with a substring
isalpha = "Hello".isalpha()        # Check if all characters are alphabetic
isdigit = "12345".isdigit()        # Check if all characters are digits

# Output the results
print(f"Original: '{sample}'")
print(f"Lowercase: '{lowercase}'")
print(f"Uppercase: '{uppercase}'")
print(f"Titlecase: '{titlecase}'")
print(f"Strip: '{strip}'")
print(f"Replace: '{replace}'")
print(f"Split: {split}")
print(f"Join: '{join}'")
print(f"Find: {find}")
print(f"Startswith: {startswith}")
print(f"Endswith: {endswith}")
print(f"Isalpha: {isalpha}")
print(f"Isdigit: {isdigit}")
