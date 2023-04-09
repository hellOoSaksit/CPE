


# นายศักดิ์สิทธิ์ ชื่นไม่วาย 6402385


class SLinkedList: 
    
    class _Node:
        def __init__(self, data=None, next_node=None): # data,next_node มีค่าเป็น ค่าว่าง
            self.data = data # ลิสต์ มีค่าเท่ากับ data
            self.next = next_node # ลิสต์ next มีค่าเท่ากับ next_node
        
    def __init__(self): # ฟั่งชั่น ลิสต์
        self._size = 0 # กำหนดขนาด มีขนาดเท่ากับ 0
        self._head = None # ลิสต์มีค่า เท่ากับ ค่าว่าง
        self._tail = None # ลิสต์มีค่า เท่ากับ ค่าว่าง
        
    def __len__(self): # ฟังชั่นคืนค่า ขนาดของลิสต์
        return self._size # คืนค่าขนาดของลิสต์
    
    def add_first(self, item): # เพิ่มข้อมูลชุดแรก
        new_node = self._Node(data=item, next_node=self._head) # data , next_node , self มีค่าเป็น item และ self._head
        self._head = new_node #self._head มีค่าเท่ากับ new_node
        if self._size == 0: # ถ้าขนาดมีค่าเท่ากับ 0
            self._tail = new_node # self.tail มีค่าเท่ากับ new_node
        self._size += 1 # self._size เพิ่มขึ้น 1
    
    def add_last(self, item):
        new_node = self._Node(data=item, next_node=None) # data , next_node , self มีค่าเป็น item และ ค่าว่าง
        if self._size == 0: # ถ้าขนาดมีค่าเท่ากับ 0
            self._head = new_node # ลิส _head และ _tail มีค่าเท่ากับ new_node 
            self._tail = new_node
        else:
            self._tail.next = new_node #ให้ self._tail ชี้น ลิสต่อไป ให้มีค่าเท่ากับ new_node
            self._tail = new_node #_tail มีค่าเท่ากับ new_node
        self._size += 1
    
    def remove_first(self): #ฟังชั่นลบข้อมูล
        if self._size == 0:
            raise IndexError("Cannot remove from an empty list") # แจ้งเตือน IndexError (เกิดขึ้นเวลาที่อ้างอิงข้อมูลชนิดลำดับเช่นลิสต์ แล้วใส่ดัชนีเกินจากค่าที่มีอยู่จริง)
        node_to_remove = self._head 
        self._head = node_to_remove.next
        self._size -= 1
        if self._size == 0:
            self._tail = None
        return node_to_remove.data #คืนค่า ของ node_to_remove.data
    
    def remove_last(self):
        if self._size == 0:
            raise IndexError("Cannot remove from an empty list") # แจ้งเตือน IndexError (เกิดขึ้นเวลาที่อ้างอิงข้อมูลชนิดลำดับเช่นลิสต์ แล้วใส่ดัชนีเกินจากค่าที่มีอยู่จริง)
        if self._size == 1:
            return self.remove_first() 
        node = self._head
        while node.next != self._tail:
            node = node.next
        node_to_remove = self._tail
        node.next = None
        self._tail = node
        self._size -= 1
        return node_to_remove.data
    
    def remove_node(self, item):
        node = self._head
        prev = None
        while node is not None: # ตรวจสอบว่า node มีค่าเป็นค่าว่างไหม
            if node.data == item:
                if prev is None:
                    return self.remove_first()
                if node == self._tail:
                    return self.remove_last()
                prev.next = node.next
                self._size -= 1
                return node.data
            prev = node
            node = node.next
        raise ValueError(f"{item} not found in list") #ValueError ในที่นี้คือชนิดของความผิดพลาดซึ่งเราสามารถกำหนดได้เอง ที่จริงจะกำหนดเป็นอะไรก็ได้ แต่ต้องเป็นชนิดที่เขากำหนดให้แต่แรก
    
    def __repr__(self):
        if self._size == 0:
            return "SLinkedList([])"
        nodes = []
        node = self._head
        while node is not None:
            nodes.append(repr(node.data))
            node = node.next
        return "SLinkedList([" + ", ".join(nodes) + "])" # เพิ่มข้อมูล โดยใส่ค่าของ nodes ลงไปในลิส
    
    def __iter__(self):
        node = self._head
        while node is not None:
            yield node.data
            node = node.next
    
    def __contains__(self, item):
        node = self._head
        while node is not None:
            if node.data == item:
                return True
            node = node.next
        return False




###########################################################################
#  การเทสโปรแกรม
#  ข้างล่าง
#  มีการเรียกใช้ฟังชั่นต่างๆ
#  และแสดงค่าออก
#
###########################################################################

sll = SLinkedList()
sll.add_first(1)
sll.add_last(2)
sll.add_last(3)
print(len(sll))  # 3
print(sll)  # SLinkedList([1, 2, 3])
sll.remove_node(2)
print(sll)  # SLinkedList([1, 3])
print(2 in sll)  # False
