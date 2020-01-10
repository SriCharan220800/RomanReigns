n=int(input())
l=list(map(int,input().split())) [:n]
k=int(input())
low=0
high=n-1
mid=(low+high)//2
while high>=low:
    mid = (low + high) // 2
    if k<l[mid]:
        high=mid-1
    elif k==l[mid]:
        print(mid)
        break
    elif  k>l[mid]:
        low=mid+1
