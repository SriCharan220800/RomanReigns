def beautifulDays(i, j, k):
    c=0
    for d in range(i,j+1):
        b=0
        t=d
        while d>0:
            a=d%10
            b=b*10+a
            d=d//10

        if t>=b:
            diff=t-b
        else:
            diff=b-t
        if diff%k==0:
            c+=1
    print(c)
if __name__ == '__main__':


    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)