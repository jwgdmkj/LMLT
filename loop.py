import random
print("홀짝 게임 시작")

a = random.randrange(1, 9)
print(a)

my = "짝"
my = input("홀 짝? 잘 못 쓰면 뻥")
print(my)

for i in range(2) :
    if my == "홀" or my == "짝" :
        print("잘못 입력. 다시 입력하라")

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
    else : 
        print("다시 입력하라")