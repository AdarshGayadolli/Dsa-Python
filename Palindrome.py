def is_palindrome(text):
    if text == text[::-1]:
        print("{} is Palindrome".format(text))
        return True
    else:
        print("{} is Not Palindrome".format(text))
        return False

x="madam"
y="bfbgsbdsnknndnsndjknsjk"

is_palindrome(x)
is_palindrome(y)
