t=int(input())
for i in range(t):
    n=input()
    d=0
    for j in n:
        if int(j)!=0:
            if int(n)%int(j)==0:
                d+=1
    print(d)