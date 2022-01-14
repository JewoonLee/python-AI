import random

number=random.randint(1,100)
while True:
    guess=int(input("숫자를 입력하시오:(1,100)"))
    if guess>number:
        print("더 작습니다")
    elif guess<number:
        print("더 큽니다.")
    else:
        print(f"{guess}가 맞습니다!")
        break

