class Node:
    """
    儲存單個節點的物件。
    包含兩個屬性：data（資料）和 next_node（下一個節點的連結）。
    """
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        # 讓 search 找到節點時，顯示內容而不是記憶體位址
        return "<Node data: %s>" % self.data

class LinkedList:
    """
    單向鏈結串列 (Singly Linked List)
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def size(self):
        """
        計算串列長度，時間複雜度 O(n)
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    
    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
        
            while position < index:
                current = current.next_node
                position += 1
            return current

    def add(self, data):
        """
        在串列頭部新增節點，時間複雜度 O(1)
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        尋找第一個匹配 key 的節點，時間複雜度 O(n)
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next_node
        return None
    
    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) time but finding the node at the
        insertion point takes O(n) time.

        Takes overall O(n) time
        """
        
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = node.next_node
                position -= 1
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node
    def remove(self, key):
        """
        Remove Node containing data that matches the key
        Return the node or None if key doesn't exist
        Takes O(n) time
        """

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
                
        return current


    def __repr__(self):
        """
        回傳串列的字串表示，時間複雜度 O(n)
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        
        # 如果串列為空，回傳表示訊息
        if not nodes:
            return "[Empty List]"
            
        return " -> ".join(nodes)