import heapq

class MedianFinder:
    def __init__(self):
        # 小顶堆：存储较大的一半元素，堆顶为这一半的最小值
        self.min_heap = []
        # 大顶堆：存储较小的一半元素，堆顶为这一半的最大值（存储负数实现）
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # 先加入大顶堆（较小的一半）
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # 平衡两个堆的大小，使大顶堆比小顶堆多一个或相等
        if len(self.max_heap) > len(self.min_heap) + 1:
            # 大顶堆过多，移一个到小顶堆
            moved = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, moved)
        elif len(self.min_heap) > len(self.max_heap):
            # 小顶堆过多，移一个到大顶堆
            moved = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -moved)

    def findMedian(self) -> float:
        # 如果总数为奇数，中位数在大顶堆的堆顶
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        # 总数为偶数，中位数为两个堆顶的平均值
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0


# 测试示例
mf = MedianFinder()
mf.addNum(3)   # 中位数：3
print(mf.findMedian())
mf.addNum(1)   # 中位数：2
print(mf.findMedian())
mf.addNum(4)   # 中位数：3
print(mf.findMedian())