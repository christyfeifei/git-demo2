import random

# 1.增加勝負判斷
# 2.贏的時候提示猜了幾次
# 3.提示區間

x = random.randint(1, 50)

win = False
start, end = 1, 100

for i in range(5):
    y = eval(input(f'[{i+1}/5]請猜一個數字({start}~{end}之間):'))
    if x == y:
        win = True
        break

    if x > y:
        print('猜大一點')
    else:
        print('猜小一點')

print(f'遊戲結束!答案為:{x}')
