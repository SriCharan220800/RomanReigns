n=int(input())
a=list(map(int,input().split()))
noofswaps=0
for i in range(n):

    for j in range(n-1):
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
            noofswaps+=1
    if noofswaps==0:
        break
print("Array is sorted in",noofswaps,"swaps.")
print("First Element:",a[0])
print("Last Element:",a[n-1])