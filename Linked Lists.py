class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        # self.tail.next = None
        self.length = 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            # self.tail.next = None
        else:
            self.tail.next = new_node
            self.tail = new_node
            # self.tail.next = None
        self.length += 1
        return self

    def remove_at_end(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        print(self.length)
        if self.length == 1:
            self.head = pre
            self.tail = self.head
        return temp

    def unshift(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        return self

    def shift(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.length -= 1

    def get(self):
        pass

    def set(self):
        pass

    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        listr = ""
        while itr:
            listr += str(itr.data) + "-->"
            itr = itr.next
        print(listr + "NULL")


list_one = LinkedList(1)
list_one.insert_at_end(2)
list_one.insert_at_end(3)
list_one.unshift(0)
list_one.shift()
list_one.unshift(0)
list_one.print_list()
print(list_one.length)
print(list_one.tail.data)
