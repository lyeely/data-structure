# 定义链表节点类
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

    # 1. 删除【指定值】的节点
    def delete_by_value(self, val):
        # 情况1：要删除的是头节点
        if self.head and self.head.val == val:
            self.head = self.head.next
            return

        # 情况2：删除非头节点
        current = self.head
        prev = None  # 记录当前节点的前一个节点
        while current:
            if current.val == val:
                # 跳过当前节点，实现删除
                prev.next = current.next
                return
            prev = current
            current = current.next
        print(f"值 {val} 不在链表中")

    # 2. 删除【头节点】
    def delete_head(self):
        if not self.head:
            print("链表为空，无法删除头节点")
            return
        self.head = self.head.next

    # 3. 删除【尾节点】
    def delete_tail(self):
        if not self.head:
            print("链表为空，无法删除尾节点")
            return
        # 只有一个节点
        if not self.head.next:
            self.head = None
            return
        # 找到倒数第二个节点
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    # 4. 删除【指定索引位置】的节点（从0开始）
    def delete_at_index(self, index):
        if index < 0:
            print("索引不能为负数")
            return
        if not self.head:
            print("链表为空")
            return

        # 删除头节点
        if index == 0:
            self.head = self.head.next
            return

        # 找到要删除节点的前一个节点
        current = self.head
        for i in range(index - 1):
            if not current.next:
                print("索引超出范围")
                return
            current = current.next

        # 删除节点
        if current.next:
            current.next = current.next.next
        else:
            print("索引超出范围")

if __name__ == "__main__":
    # 创建链表
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)

    print("原始链表：")
    ll.print_list()

    # 测试删除指定值
    print("\n删除值为 30 的节点：")
    ll.delete_by_value(30)
    ll.print_list()

    # 测试删除头节点
    print("\n删除头节点：")
    ll.delete_head()
    ll.print_list()

    # 测试删除尾节点
    print("\n删除尾节点：")
    ll.delete_tail()
    ll.print_list()

    # 测试删除指定索引
    print("\n删除索引 1 的节点：")
    ll.delete_at_index(1)
    ll.print_list()