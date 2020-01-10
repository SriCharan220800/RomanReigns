n=int(input())
s=list(map(int,input().split()))
dm=list(map(int,input().split()))
d=dm[0]
m=dm[1]
c=0
for i in range(n-1):
    x=s[i:i+m]
    if sum(x)==d:
        c+=1
print(c)