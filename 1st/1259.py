# 팰린드롬
# import copy
# input = list(input())
# reverse = copy.deepcopy(input)
# reverse.reverse()
# print(input)
# print(reverse)

# if input == reverse:
#     print('yes')
# else: print('no')




while(True):
    a = input()
    if a == "0":
        break
    elif a == a[::-1]:
        print("yes")
    else:
        print("no")

    