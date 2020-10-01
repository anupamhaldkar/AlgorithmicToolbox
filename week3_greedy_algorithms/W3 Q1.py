n=int(input())
c=0
c+=n//10
n=n%10
c+=n//5
n=n%5
c+=n
print(c)