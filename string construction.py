s=input()
l=[]
c=0
for i in s:
    if i not in l:
        l.append(i)
        c+=1
print(c)