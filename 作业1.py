class Collection:
    """
    一个集合类，可进行元素的插入、删除和查询操作。
    内部使用 set 存储，保证元素唯一性。
    """

    def __init__(self) -> None:
        """初始化空集合。"""
        self._items = set()  # 使用 set 存储任意类型的元素

    def add(self, item: object) -> None:
        """
        向集合中添加一个元素。
        """
        self._items.add(item)

    def remove(self, item: object) -> bool:
        """
        从集合中移除指定元素。
        返回 True 表示移除成功,False 表示元素不存在。
        """
        if item in self._items:
            self._items.remove(item)
            return True
        return False
    def __str__(self) -> str:
        """返回集合的表示，不然会成为内存地址"""
        return str(self._items)
    
    def contains(self, item: object) -> bool:
        """检查元素是否存在于集合中。"""
        return item in self._items
col = Collection()
col.add(42)
col.add("hello")
col.add(3.14)
print(col.remove(42)) 
print(col)