class SortedArray:
    """
    有序数组类
    """

    def __init__(self, initial: list = None) -> None:
        """
        初始化有序数组。
        如果提供了初始列表，会将其元素逐个插入以构建有序数组。
        """
        self._data: list = []
        if initial:
            for item in initial:
                self.insert(item)

    def insert(self, item) -> None:
        """
        将元素插入到正确位置，保持数组升序。
        使用二分查找确定插入点
        """
        # 二分查找插入位置
        left, right = 0, len(self._data)
        while left < right:
            mid = (left + right) // 2
            if self._data[mid] < item:
                left = mid + 1
            else:
                right = mid
        self._data.insert(left, item)

    def __str__(self) -> str:
        """返回数组的表示，不然会成为内存地址"""
        return str(self._data)

    def __len__(self) -> int:
        """返回元素个数。"""
        return len(self._data)

sa = SortedArray([7, 1, 4, 9])
sa.insert(5)
print(sa)   