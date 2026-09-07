

# Check if a character is uppercase, lowercase, digit, or special character

char=input("enter any character")

if char.isupper():
    print(" character is in upper case")


elif char.islower():
    print(" character is in lower case")


elif char.isdigit():
    print(" character is  in digit")


else:
    print("it is the special character")            