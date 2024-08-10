# Sample string with escape sequences
escape_sequences = "Hello,\nWorld!\tThis is a test.\nHere's a quote: \"Hello, Python!\"\nAnd a backslash: \\"

# Output the original string
print("Original string with escape sequences:")
print(escape_sequences)

# Demonstrating various escape sequences
newline = "Line1\nLine2"           # Newline
tab = "Column1\tColumn2"           # Tab
backslash = "This is a backslash: \\" # Backslash
single_quote = 'It\'s a single quote.' # Single quote
double_quote = "He said, \"Hello!\""   # Double quote
carriage_return = "Hello\rWorld"    # Carriage return
backspace = "Hello\bWorld"          # Backspace
formfeed = "Hello\fWorld"           # Form feed
octal_value = "\101\102\103"        # Octal value (A, B, C)
hex_value = "\x41\x42\x43"          # Hex value (A, B, C)
unicode_char = "\u0041\u0042\u0043" # Unicode character (A, B, C)

# Output the results of various escape sequences
print("\nExamples of various escape sequences:")
print(f"Newline: \n{newline}")
print(f"Tab: \n{tab}")
print(f"Backslash: \n{backslash}")
print(f"Single quote: \n{single_quote}")
print(f"Double quote: \n{double_quote}")
print(f"Carriage return: \n{carriage_return}")
print(f"Backspace: \n{backspace}")
print(f"Form feed: \n{formfeed}")
print(f"Octal value: \n{octal_value}")
print(f"Hex value: \n{hex_value}")
print(f"Unicode character: \n{unicode_char}")
