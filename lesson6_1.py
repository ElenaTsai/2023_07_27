import random
#自訂function
def play_game():
    min=1
    max=100
    target=random.randint(min,max)
    count=0
    print('=====猜數字遊戲====')
    while True:
        keyin=int(input(f"猜數字範圍{min}~{max}"))
        count+=1
        if keyin>=min and keyin<=max:
            if keyin==target:
                print(f"bingo,the ans is {target}")
                print(f"u had already guessed {count} times")
                break
            elif keyin>target:
                print("smaller")
                max=keyin-1
            elif keyin<target:
                print("bigger")
                min=keyin+1
            print(f"u had already guessed {count} times")
        else:
            print("over range")
while True:
    play_game()#呼叫function
    play_again=input("continue the game?(yes or no)")
    if play_again=="no":
        break
    else:
        continue
print("game over")
