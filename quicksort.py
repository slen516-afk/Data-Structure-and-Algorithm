import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def quicksort(values):
    if len(values) <= 1:
        return values
    
    pivot = values[0]
    less_than_pivot = []
    greater_than_pivot = []
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
            
    # 遞迴排序並合併結果
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)