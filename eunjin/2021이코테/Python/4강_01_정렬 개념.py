#정렬: 데이터를 특정한 기준에 따라 순서대로 나열

#선택 정렬: 처리되지 않은 데이터중 가장 작은 데이터를 선택해 맨앞 데이터와 바꿈
#선택 정렬 시간 복잡도 o(n^2)
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_index = i #가장 앞쪽 원소
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] #swap

print(array)

#삽입 정렬: 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입, 구현 난이도가 높지만, 일반적으로 선택정렬보다 효율적
#삽입 정렬 시간 복잡도 o(n)
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
  for j in range(i, 0, -1): #인덱스 i부터 1까지 1씩 감소하며 반복
    if array[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break

print(array)

#퀵 정렬: 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법, 첫 번째 데이터를 기준 데이터(pivot)으로 설정함
#삽입 정렬 시간 복잡도 o(nlogn) or 최악의 경우 o(n^2)
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
  if start >= end: # 원소가 1개인 경우 종료
    return
  pivot = start
  left = start + 1
  right = end
  while(left <= right):
    #피봇보다 큰 데이터를 찾을 때까지 반복
    while(left <= end and array[left] <= array[pivot]):
      left += 1
    #피봇보다 작은 데이터를 찾을 때까지 반복
    while(right > start and array[right] >= array[pivot]):
      right -= 1
    if(left > right):
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]

  quick_sort(array, start, right -1)
  quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

#퀵정렬 다르게 구현
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort2(array):
  if len(array) <= 1:
    return array
  pivot = array[0]
  tail = array[1:] #피봇을 제외한 리스트

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(array))


#계수 정렬: 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 작동함, 각각의 원소가 몇번씩 등장했는지 셈
#시간복잡도 & 공간 복잡도 o(n+k)
array = [7,5,9,0,3,1,6,2,4,8]

count = [0] * (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end= ' ')

#동일한 값을 가지는 데이터가 여러개 들어있을 때 효율적임

