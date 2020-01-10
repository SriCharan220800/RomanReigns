z=int(input("from "))
n=int(input("number " ))
l=["A","B","C","D","E","F"]
A=10
B=11
C=12
D=13
E=14
F=15
i=0
d=0
while n>0:
    x=n%10
    d+=(x*(z**i))
    n=n//10
    i+=1
print(d)