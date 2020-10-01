d=int(input())
m=int(input())
n=int(input())
stations=list(map(int,input().split()))
stations.append(d)
minst=0
lastfull=0
flag=0
for station in stations:
    if (station - lastfull > m):
        print(-1)
        flag=1
        break
    elif (station!=d and stations[stations.index(station)+1]-lastfull>m):
            lastfull=station
            minst+=1
if flag==0:
    print(minst)