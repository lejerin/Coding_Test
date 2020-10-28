#1이 될 때까지

n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target

    #n이 k보다 작을 때 (더이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break

    result += 1
    n //= k

result += (n -1)
print(result)

