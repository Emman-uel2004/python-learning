k,n=map(int,input().split())
items=list(map(int,input().split()))
pay=int(input())
total=0
remain=0
for i in range(len(items)):
    if n!=i:
        total+=items[i]
ann_pay=total//2
if ann_pay==pay:
    print("Bon Appetit")
else:
    remain= ann_pay-pay
    remain=-remain
    print(remain)
Overwriting billing.py
