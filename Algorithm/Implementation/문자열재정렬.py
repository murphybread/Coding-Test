# 구혀-문자열문제

# input으로 받아 숫자인지 문자인지 판단
# 숫자면 특정 변수에 더하기, 글자면 글자 변수에 더하기
# 마지막에 숫자들 더해주고, 문자열로 바꾼후 글자변수에 더하기

# 구현이기에 isdigit함수, 문자열 리스트변환, 문자여과 숫자 합으로 구하기 등이 요구됨

string = input()

sum = 0
name = ""


for s in string:
    if s.isdigit():
        sum += int(s)
    else:
        name += s
name = list(name)
name.sort()
name = "".join(name)

sum = str(sum)

print(name + sum)
