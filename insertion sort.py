arr = list(map(int,input().split()))
len_arr = len(arr)
for i in range(1,len_arr) :
    marker = arr[i]
    j = i - 1
    while(j>=0 and arr[j]>=marker) :
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = marker
print(arr)
