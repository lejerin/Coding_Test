# 이진 탐색: 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터 탐색
# 순차 탐색: 데이터를 찾기위해 앞에서부터 데이터를 하나씩 확인

#이진 탐색 - 재귀함수
def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) //2 
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array, target, start, mid -1)
  else:
    return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)

#이진 탐색 - 반복문
def binary_search2(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

result = binary_search2(array, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)


from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a,x))

def count_by_range(a, left_value,  right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a,  left_value)
  return right_index - left_index

a = [1,2,3,3,3,3,3,4,4,8,9]

print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))
