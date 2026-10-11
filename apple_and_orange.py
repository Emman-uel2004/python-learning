s,t=map(int,input().split())
a,b=map(int,input().split())
m,n=map(int,input().split())
apple=list(map(int,input().split()))
orange=list(map(int,input().split()))
count=0
for ap in range(m):
    fal=a+apple[ap]
    if fal>=s and fal<=t:
        count+=1
print(count)
count=0
for ora in range(n):
    fali=b+orange[ora]
    if fali>=s and fali<=t:
        count+=1
print(count)
