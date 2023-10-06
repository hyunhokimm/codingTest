N = int(input())  # N을 입력 받음

result = 0  # 결과를 저장할 변수를 초기화

# 나머지와 몫이 같은 자연수를 찾기
for x in range(1, N):
   result += N * x + x

print(result)