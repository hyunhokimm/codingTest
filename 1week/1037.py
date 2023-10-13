
# 입력받은 문자열을 int형 리스트로 만든다.
a = list(map(int,input().split()))
# 파이썬의 sort() 함수는 정렬 사용에 용이하다.
a.sort()
# a[0]와 a[마지막] 수를 곱하여 양수를 구한다.
b = a[0]*a[-1]
print(b)
