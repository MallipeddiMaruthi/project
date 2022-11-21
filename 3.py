m=int(input())
def rotDigits(n):
    lst=[]
    count = 0
    for i in range(0,10000):
        Set = set(list(str(i)))
        if (not Set.intersection({'3','4','7'}) and 
                Set.intersection({'1','0','2','5','6','8','9'})):
            lst.append(i)  
    return lst[m]

print(rotDigits(m))