str1=input()
str2=input()
c=0
s=str2[-1]
for i in range(len(str1)):
    if s==str1[i]:
        c+=1
print(c)
          