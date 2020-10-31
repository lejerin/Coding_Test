#파라메트릭 서치: 최적화 문제를 결정문제(예, 아니오)로 바꾸어 해결

n, m = map(int, input().split())

array = list(map(int, input().split()))


start = 0
end = max(array)

result = 0
while start <= end:
  total = 0
  mid = (start + end) // 2
  for x in array:
    if x > mid:
      total += x - mid
  if total < m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1

print(result)
