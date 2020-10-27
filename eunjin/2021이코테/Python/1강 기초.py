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

#기분 입출력
