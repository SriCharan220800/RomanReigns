n=int(input())
sh=5
li=0
cum=0
for i in range(n):
    li = sh // 2
    sh=(li*3)
    cum+=li

print(cum)