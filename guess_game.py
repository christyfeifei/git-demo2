import random

# 1.增加勝負判斷
# 2.贏的時候提示猜了幾次
# 3.提示區間

x = random.randint(1, 50)

win = False
start, end = 1, 50
for i in range(5):
    y = eval(input(f'[{i+1}/5]請猜一個數字(1~50之間):'))
    if x == y:
        win = True
        break

    if x > y:
        # 如果y大於原本最小值再進行替換
        if y > start:
            start = y
        print(f'猜大一點({start}~{end})')
    else:
        # 如果y小於原本最高值再進行替換
        if y < end:
            end = y
        print(f'猜小一點({start}~{end})')


if win:
    print(f'恭禧過關!總共猜:{i+1}次')
else:
    print(f'遊戲結束!答案為:{x}')
