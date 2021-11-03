import random

print("홀짝 게임 시작")

a = random.randrange(1, 9)
print(a)

my = "짝"
print(my)

dab = ""
if a%2 == 0:
    print("짝")
    dab = "짝"
else :
    print("홀")
    dab = "홀"

if dab == my:
    print("정답")
else :
    print("오답")