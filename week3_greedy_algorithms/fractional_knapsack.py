n,w=map(int,input().split())
ratiolist=[]
values=[]
weights=[]
maxval=0
for _ in range(n) :
    v,wt=map(int,input().split())
    values.append(v)
    weights.append(wt)
    r=v/wt
    ratiolist.append(r)

while True :
    if not ratiolist:
        print("{:.4f}".format(maxval))
        break
    r=max(ratiolist)
    pos=ratiolist.index(r)
    wt=weights[pos]
    v=values[pos]
    if(w>=wt):
        maxval+=v
        weights.pop(pos)
        values.pop(pos)
        ratiolist.pop(pos)
        w=w-wt

    elif(w>0) :
        fract=w/wt
        maxval+=(v*fract)
        print("{:.4f}".format(maxval))
        break
    else:
        print("{:.4f}".format(maxval))
        break
