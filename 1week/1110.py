a = int(input())
b = a
count = 0

while True:
    # a의 각 자리의 수를 구한다.
    j = b // 10
    k = b % 10
    # 각 자리의 수를 더한 후 일의 자리 값을 구한다.
    l = (k + j) % 10
    # 원래 있던 수의 일의 자리의 수와 l 를 문자열로 합친 후 int형으로 변환한다..
    b = int(str(k) + str(l))
    count = count +1
    # 그렇게 나온 수 b와 원래의 수 a를 비교하여 같다면 while 문을 빠져나온다.
    if a == b:    
        break
print(count)


    