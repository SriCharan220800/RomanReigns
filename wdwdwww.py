def kangaroo(x1, v1, x2, v2):
    i=1
    k1=x1
    k2=x2
    if v1 <= v2:
        while i>0:
            if k1!=k2:
                k1+=v1
                k2+=v2
                i+=1
            else:
                i=-1
        if i==-1:
            print("YES")
        else:
            print("NO")
    if v1>=v2:
        while i>0:
            if k1!=k2:
                k1+=v1
                k2+=v2
                i+=1
            else:
                i=-1
        if i==-1:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
