def load_numbers(file_name):
    numbers = []
    with open(file_name) as f:
        for line in f:
            # 去除換行符號並轉成整數
            numbers.append(int(line.strip()))
    return numbers