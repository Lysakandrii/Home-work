import string
def is_palindrome(text):
    text = str(text.upper())
    for l in text:
        if l in string.punctuation:
            text = text.replace(l , "")
            text = text.replace(" ","")
    if text == text[::-1]:
        return True
    else:
        return False


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")



