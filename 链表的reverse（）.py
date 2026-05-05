class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 节点值
        self.next = next  # 指向下一个节点的指针

# 链表操作类
class LinkedList:
    def __init__(self):
        self.head = None  # 链表头节点，初始为空

    def append(self, val):
        new_node = ListNode(val)
        # 如果链表为空，新节点作为头节点
        if not self.head:
            self.head = new_node
            return
        # 找到最后一个节点
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

        # 打印链表，方便查看结果
    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

def reverse(self):
        prev = None  # 前一个节点，初始为空
        current = self.head  # 当前节点从头开始

        while current:
            next_node = current.next  # 先保存下一个节点
            current.next = prev       # 反转当前节点的指针（指向前一个）
            prev = current            # prev 向前移动
            current = next_node       # current 向前移动

        # 循环结束后，prev 就是新的头节点
        self.head = prev