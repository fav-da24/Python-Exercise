text = input("Enter a string: ")
text2 = text [::-1]
if text == text2:
    print(text, " is a palindrome")
else:
    print(text, " is not a palindrome")