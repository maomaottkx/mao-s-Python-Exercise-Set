from datetime import datetime
import os

RECORD_PATH = r'E:\python项目\账单记录.txt'


def bill(item, price, budget):
    print(f'{item}: {price} 元')
    return budget - price


def month_header_exists(month):
    if not os.path.exists(RECORD_PATH):
        return False
    with open(RECORD_PATH, 'r', encoding='utf-8') as f:
        return f'=== {month} ===' in f.read()


budget = float(input('这个月预算多少？'))
remaining = budget
bills = []

while True:
    item = input('账单名称（输入 q 结束）：')
    if item == 'q':
        break
    price = float(input('花了多少钱？'))
    if price <= remaining:
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        bills.append((item, price, now))
        remaining = bill(item, price, remaining)
    else:
        print(f'超支！{item} 需要 {price} 元，但只剩 {remaining} 元，这笔没有记账')
    if remaining == 0:
        print('刚好花完')
        break

print(f'余额还剩 {remaining} 元')

month = datetime.now().strftime('%Y-%m')
with open(RECORD_PATH, 'a', encoding='utf-8') as f:
    if not month_header_exists(month):
        f.write(f'\n=== {month} ===\n')
    for item, price, now in bills:
        f.write(f'{now} {item} {price} 元\n')
print('账单已保存到 账单记录.txt')
