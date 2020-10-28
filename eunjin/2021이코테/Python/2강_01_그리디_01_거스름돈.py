#그리디 알고리즘 문제는 탐욕법으로 얻은 해가 최적의 해가 되는 상황에 대해 출제되는 경우가 많음

#거스름돈
n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
  count += n // coin
  n %= coin

print(count)
