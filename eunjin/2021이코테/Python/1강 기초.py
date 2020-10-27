#정수형
a = 777
print(a)

a = a+5
print(a)

#실수형
a = 157.93
print(a)

a = .7
print(a)

a = 1e9
print(a)

a = int(1e9)
print(a)

#실수는 정확하지 않으므로 round() 함수 사용
a = 0.3 + 0.6
if round(a,4) == 0.9:
  print(True)
else:
  print(False)

#파이썬은 / 연산자 결과를 실수형으로 반환

#몫을 얻기 위해서 // 사용
print(7//3)
print(7%3)

#리스트 자료형: 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형

list1 = [1,2,3,4,5]
print(list1)
print(list1[3])

# 크기가 n이고 모든 값이 0인 1차원 리스트 초기화
n = 10
list1 = [0] * n
print(list1)

#파이썬에서 음수 인덱스로 접근하면 뒤에서부터 출력함
list1 = [1,2,3,4,5]
print(list1[-1])
print(list1[-2])

#두 번째 원소부터 세 번째 원소까지
print(list1[1:3])

# 0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)]
print(array)

# 0부터 19까지이 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i * i for i in range(10)]
print(array)

#2차원 리스트 초기화 n*m 사이즈
n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)

#append(), sort(), sort(reverse = True), reverse(), insert(), count(), remove()

#특정 값을 가진 값만을 리스트에서 제거할 때
a = [1,2,3,4,5,5,5]
#집합 자료형 {}
remove_set = {3,5}
result = [i for i in a if i not in remove_set]
print(result) 

#문자열 출력 
data = 'Hello World'
print(data)

data = "don't you know \"python\"?  or \'happy\'?"
print(data)

#문자열 연산 곱셈, 덧셈
a = "Hello"
b = "world"
print(a + " " + b)
print(a*3)
print(a[2:4])

#튜플 자료형: 한번 선언된 값을 변경할 수 없다. 소괄호()를 사용함
a = (1,2,3,4,5,6,7,8)
print(a[3])
print(a[1:4])
# 오류발생 a[2] = 7

#튜플 장점: 서로 다른 성질의 데이터를 묶어서 관리해야할 때 (비용, 노드 번호의 형태로)/ 해싱의 키 값으로 사용해야 할 때/ 리스트보다 메모리를 효율적으로 사용할 때

#사전 자료형 : 키와 값 쌍을 데이터로 가지는 자료형

data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

print(data)
if '사과' in data:
  print("사과를 키로 가지는 데이터가 존재합니다")

key_list = data.keys()
Value_list = data.values()
print(key_list)
print(Value_list)

for key in key_list:
  print(data[key])

b = {
  '홍길동': 97,
  '이순신': 939
}
print(b)

#리스트로 형변환
key_list = list(b.keys())
print(key_list)

#집합 자료형: 중복을 허용하지 않고, 순서가 없음 / 존재하는지 유무만을 판단할 때 좋음

data = set([1,1,2,3,4,4,5])
print(data)

data = {1,1,2,3,4,4,5}
print(data)

#집합 자료형 연산: 합집합, 교집합, 차집합
a = set([1,1,2,3,4,5])
b = set([3,4,5,6,7])
print(a|b)
print(a&b)
print(a-b)

a.add(4)
a.update([9,10])
a.remove(1)
print(a)

#기분 입출력 input()
# map() 

# n= int(input())
# data = list(map(int, input().split()))
# a,b,c = list(map(int, input().split()))

# data.sort(reverse=True)
# print(data)

#빨리 입력을 받기위해 
# import sys
# sys.stdin.readline().rstrip()

#줄바꿈을 원하지않으면 end속성 사용
a = "hello"
print(a, end=" ")
print("dd")

# f - String
answer = 8
print(f"정답은 {answer}")

x = 5
if x >= 10:
  print("10이상")
elif x >=5:
  print("5이상")
else:
  print("5 미만")

# and or
if x <=5 and x>0:
  print("조건 만족")

# list 연산자 in, not in

result = "success" if x >=0 else "fail"
print(result)

if 0<x<10:
  print("x는 0과 10 사이의 변수")

#while문
i = 1
result = 0
while i <=9:
  result += i
  i += 1
print(result)

result = 0
for i in range(1,10):
  print(i)


def add(a,b):
  return a+b
print(add(3,7))
print(add(b=4, a=1))

#전역변수 global
a = 10

def func():
  global a
  a += 1
  print(a)

func()
func()

#파이썬에서 함수는 여러 개의 반환 값을 가질 수 있습니다. 
def operator(a,b):
  add_var = a+b
  var2 = a*b
  return add_var, var2

a,b = operator(7,3)
print(a,b)

#람다 표현식
print((lambda a,b: a + b)(3,7))

#람다 표현식을 사용한 정렬
array = [('홍길동', 50), ('이순신', 32), ('아무개', 22)]
print(sorted(array, key = lambda x: x[1]))

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
result = map(lambda a,b: a+b, list1, list2)
print(list(result))

#실전에서 유ㅠ용한 표준 라이브러리

# itertools : 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능, 순열과 조합 라이브러리

#heapq : 힙 자료구조, 우선순위 큐 기능

#bisect : 이진탐색 기능 제공

#collections : 덱, 카운터 자료구조

#math

#내장함수
result = sum([1,2,3,4,5])
print(result)

result = min([1,2,3])
print(result)

from itertools import permutations

data = ['a', 'b', 'c']
result = list(permutations(data,3))
print(result)

from itertools import combinations
result = list(combinations(data,2))
print(result)

#counter 등장 횟수
from collections import Counter

counter = Counter([1,1,2,2,3,3,3,3,3,4])
print(counter[1])
print(counter[3])
print(dict(counter))

#최대 공약수/ 최소 공배수 math.gcd()

import math
print(math.gcd(21,14))
