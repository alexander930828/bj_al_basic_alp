str = input()

lst = [0] * 26

for i in str:
    lst[ord(i) - 97] += 1 #이게 곧 영어의 번호가 되니까

for i in lst:
    print(i, end=' ')