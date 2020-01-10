n=int(input())
marks=[]
names=[]
for i in range(n):
    nm=list(input().split())
    names.append(nm[0])
    marks.append([])
    for j in range(1,4):
        p=float(nm[j])
        marks[i].append(p)
x=input()
for i in range(n):
    if x==names[i]:
        avg=float(sum(marks[i])/3)
print('%.2f' %(avg))
