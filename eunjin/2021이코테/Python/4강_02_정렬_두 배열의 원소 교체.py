#두 배열의 원소 교체

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

for i in range(k):
  if a[i] < b[n-i-1]:
    a[i],b[n-i-1] = b[n-i-1], a[i]

result = 0
for i in range(n):
  result += a[i]

print(result)
