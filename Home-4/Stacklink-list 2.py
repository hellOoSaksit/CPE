# Ref : https://stackoverflow.com/questions/74324611/linked-list-cant-acess-the-data-from-next-node
# Ref : https://stackoverflow.com/questions/74754134/i-have-a-problem-with-syntax-in-nodes-data-structure

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

	#append(self, data) - เป็นเมทอดที่ใช้เพิ่มข้อมูล (data) เข้าไปใน LinkedList โดยสร้างโหนดใหม่ (new_node) 
	# และตรวจสอบว่า LinkedList ว่างเปล่าหรือไม่ 
	# ถ้าว่างเปล่า ก็ให้ head และ tail ชี้ไปยังโหนดใหม่นั้นเลย 
	# ถ้าไม่ว่างเปล่า ก็ให้โหนดท้าย (tail) ชี้ไปยังโหนดใหม่ 
	# และอัพเดท tail เป็นโหนดใหม่นั้น 
	# จากนั้นก็เพิ่มขนาดของ LinkedList 
	# ด้วยการเพิ่มค่า size อีก 1
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1


class Stack:
    # เพิ่มเงือนไขทดสอบการเต็มของ stack 
    def __init__(self,max_size = -1): 
        self.slist = SLinkList()
        self.max_size = max_size
    def __len__(self):
        return self.slist.size

    def is_empty(self):
        return self.slist.is_empty()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.slist.tail.data

    def pop(self):
        # ตรวจสอบว่า stack ว่างหรือไม่
        if self.is_empty():
            print("Stack is empty")
            self.slist.size -= 1
        else:
            # ถ้าไม่ว่างก็ให้เก็บค่าข้อมูลของตัวสุดท้ายใน stack
            data = self.slist.tail.data
              # ถ้า Stack มีข้อมูลเพียงตัวเดียว
            if self.slist.size == 1:
                self.slist.head = None
                self.slist.tail = None
            else:
                # หา Node ก่อนตัวสุดท้าย
                curr_node = self.slist.head
                while curr_node.next != self.slist.tail:
                    curr_node = curr_node.next
                      # กำหนด Node ก่อนตัวสุดท้ายเป็น Node สุดท้าย
                curr_node.next = None
                self.slist.tail = curr_node
                # ลดขนาดของ Stack ลง 1 และคืนค่าข้อมูลที่ถูกลบ
            self.slist.size -= 1
            return data

    def push(self, data):
        if len(self) == self.max_size:
            print("Stack is full")
        else:  
            self.slist.append(data)

    def __repr__(self):
        if self.is_empty():
            return "Stack: []"
        else:
            node = self.slist.head
            stack_str = "Stack: ["
            # วน loop เพื่อเพิ่มข้อมูลของทุก Node ใน Stack เข้าไปใน string
            while node is not None:
                stack_str += str(node.data)
                node = node.next
                if node is not None:
                    stack_str += ", "
            stack_str += "]"
            return stack_str



s = Stack()
print("สถานะของ Stack ",s.is_empty())   
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
s.push(70)
s.push(80)
print("ค่าบนสุดของ Stack : ",s.peek())      
print("ค่าของทำการ PoP มา : ",s.pop())  
print("ค่าสูงสุดสุด (Peek) : ",s.peek())     
print("จำนวนข้อมูลทั้งหมด (Len)",int(len(s)))    
print(s) 
