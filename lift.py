n=int(input())
n1=int(input())
n2=int(input())
n3=int(input())
d1=n-n1
if d1<0:
    d1=-d1
d2=n-n2
if d2<0:
    d2=-d2
d3=n-n3
if d3<0:
    d3=-d3
if d1<d2 and d1<d3:
    print(n1)
elif d2<d1 and d2<d3:
    print(n2)
elif d3<d1 and d3<d2:
    print(n3)
elif d1==d2 and d1<d3:
    print(n2)
elif d1==d3 and d1<d2:
    print(n3)
elif d2==d3 and d2<d1:
    print(n3)
