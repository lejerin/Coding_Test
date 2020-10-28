#곱하기 혹은 더하기

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

#계산하는 두 수중 둘 중 하나라도 0, 1이면 더하기를, 아니면 곱하기를 수


