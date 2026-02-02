
import random

# 設定要產生的數字數量
count = 1000000

# 產生 10000 個隨機數字並寫入檔案
with open("10000.txt", "w") as f:
    for _ in range(count):
        # 產生 1 到 10000 之間的隨機數
        number = random.randint(1, 10000)
        f.write(f"{number}\n")

print("成功生成 10000.txt！")