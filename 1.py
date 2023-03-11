import random

# 樂透號碼開獎：1 5 10 35 50
# 特別號：49

numbers = random.sample(range(1, 50), 6)
print('樂透號碼開獎: '+' '.join(map(str, sorted(numbers))))

print(f'特別號：{random.randint(1, 50)}')
