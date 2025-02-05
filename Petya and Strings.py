
def compare_strings(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0


str1 = input()
str2 = input()  

print(compare_strings(str1, str2))
