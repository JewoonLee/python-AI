
while True:
    dan=int(input("구구단 몇단?"))
    if dan>0 and dan<10:
        for i in range(1,10):
            print(f"{dan}*{i}={dan*i}")
            
    elif dan>=10:
        print("10 이상은 안됩니다.")
        
    elif dan==0:
        print("프로그램 종료")
        break



