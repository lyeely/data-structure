import random

def quick_sort_3way(arr, low=0, high=None):
    """三路快速排序"""
    if high is None:
        high = len(arr) - 1
    
    if low >= high:
        return arr
    
    # 随机选择轴并交换到开头
    pivot_idx = random.randint(low, high)
    arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]
    pivot = arr[low]
    
    # 三路分区指针
    # [low, lt) : < pivot
    # [lt, gt]  : = pivot  
    # (gt, high] : > pivot
    lt = low      # less than pivot 的边界
    gt = high     # greater than pivot 的边界
    i = low + 1   # 当前扫描位置
    
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:  # arr[i] == pivot
            i += 1
    
    # 递归处理小于和大于部分
    quick_sort_3way(arr, low, lt - 1)
    quick_sort_3way(arr, gt + 1, high)

    return arr

test_arr_with_dups = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 1]
print("原数组:", test_arr_with_dups)

# 测试
result = quick_sort_3way(test_arr_with_dups.copy())
print("三路快排结果:", result)

# 极端情况：大量重复元素
extreme_case = [5] * 1000 + [3] * 500 + [7] * 500
arr_extreme = extreme_case.copy()
quick_sort_3way(arr_extreme)
print(f"前10个: {arr_extreme[:10]}")
print(f"中间10个: {arr_extreme[995:1005]}")
print(f"后10个: {arr_extreme[-10:]}")
print("排序成功!" if arr_extreme == sorted(extreme_case) else "排序失败!")