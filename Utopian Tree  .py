t=int(input())
for i in range(t):
    n=int(input())
    h=0
    for i in range(n+1):
       if i%2==0:
           h += 1
       else:
           h *= 2

    print(h)