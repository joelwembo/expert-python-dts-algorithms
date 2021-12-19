# Python program to convert list to a string

def listToString(s):
    
    # initialize an empty string
    str1 = ""
    
    # traverse in the string
    for ele in s:
        str1 += ele
        
    # return string
    return str1

# Driver code

s = ['I am' , ' your' , ' friend']

print(listToString(s))    