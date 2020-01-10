y0=float(input())
x0=float(input())
h=float(input())
n=int(input())
x=x0
y=y0
for i in range(1,n+1):
    y=y+h*(x+y)
    x=x+h
    print("x",i,"=",x,end="; ")
    print("y",i,"=",y)
