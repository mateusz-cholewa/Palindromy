def IsPalindrome(string):
    string = list(string)
    reverse_string = string[::-1]
    if string == reverse_string:
        print(True)
    else:
        print(False)
IsPalindrome("kajak")