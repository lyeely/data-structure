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

def has_cycle(self):
        # 快慢指针
        slow = self.head
        fast = self.head

        while fast and fast.next:  # 快指针不走到空
            slow = slow.next        # 慢指针走1步
            fast = fast.next.next   # 快指针走2步

            if slow == fast:       # 相遇 = 有环
                return True
        return False               # 快指针到末尾 = 无环