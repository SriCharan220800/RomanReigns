if __name__ == '__main__':
    n=int(input())
    scores=[]
    names=[]
    for i in range(n):
        x=[]
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    mini=min(scores)
    l=[]
    for i in  range(n):
        if scores[i]>mini:
            l.append(scores[i])
    z=min(l)
    d=[]
    for i in range(n):
        if scores[i]==z:
            d.append(names[i])
    d.sort()
    for i in d:
        print(i)
