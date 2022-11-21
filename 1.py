def find_ter(num): 
    quot = num/3   
    rem = num%3
    if quot == 0:   
        return ""
    else:
        return find_ter(int(quot)) + str(int(rem))    
number = int(input()) 
print(find_ter(number))