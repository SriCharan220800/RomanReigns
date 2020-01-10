s=input()
g=0
if len(s)%2==0:
    for i in s[:len(s)//2]:
        c=0
        for j in s[(len(s)//2):]:
            if i==j:
                print(j)
                break
            else:
                g+=1
                break
    print(g)
else:
    print("-1")