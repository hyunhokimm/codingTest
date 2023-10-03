s = input().lower() #mississipi 소문자로 받기
s_set = list(set(s)) # m,i,s,p 집합화
cnt = []


for i in s_set: # m, i ,s ,p 하나씩 cnt 리스트에 추가
    cnt.append(s.count(i)) # [1,4,4,1]

max_num =max(cnt)
if max_num >=2 and cnt.count(max_num) >=2:
    print("?")
else :
     print(s_set[cnt.index(max_num)].upper())