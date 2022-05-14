'''def reverse_string(string):
    n = len(string)
    rev = ""
    i = n -1
    while i>0:
        rev = rev + string[i]
        i = i -1
    return rev
if __name__ == "__main__":
    if reverse_string("python")=="nohtyp" and reverse_string("rotator")=="rotator":
        print("Test for reverse_string() function was successful!!")
    else:
        print("The reverse_string() function is not working properly")'''

import doctest
def reverse_string(string):
    """>>> reverse_string("hello")
'olleh'
>>> reverse_string("madam")
'madam'
>>> reverse_string("TestinG")
'GnitesT'
>>>"""
    n= len(string)
    rev = ""
    i = n-1
    while i >=0:
        rev = rev + string[i]
        i = i -1
    return rev
if __name__ == "__main__":
    doctest.testmod()


