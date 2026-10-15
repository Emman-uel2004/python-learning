n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    for j in range( n-1):
      if arr[j]>arr[j+1]:
        arr[j+1],arr[j]=arr[j],arr[j+1]

minimum = arr[1] - arr[0]

for i in range(1, n - 1):
    diff = arr[i + 1] - arr[i]

    if diff < minimum:
        minimum = diff

print(minimum)
