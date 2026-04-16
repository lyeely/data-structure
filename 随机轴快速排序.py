import random

def quick_sort_random(arr):
    """随机选择轴的快速排序"""
    if len(arr) <= 1:
        return arr
    
    # 随机选择轴（而不是总是选最后一个）
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]
    
    # 将轴元素移到末尾以便分区
    arr[pivot_idx], arr[-1] = arr[-1], arr[pivot_idx]
    
    # 分区
    i = 0
    for j in range(len(arr) - 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    # 将轴放到正确位置
    arr[i], arr[-1] = arr[-1], arr[i]
    
    # 递归排序左右两部分
    left = quick_sort_random(arr[:i])
    right = quick_sort_random(arr[i+1:])
    
    return left + [arr[i]] + right


# 测试
test_arr = [3, 6, 8, 10, 1, 2, 1]
print("原数组:", test_arr)
print("排序后:", quick_sort_random(test_arr))

# 测试最坏情况
sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\n已排序数组:", sorted_arr)
print("随机快排结果:", quick_sort_random(sorted_arr))