""" Doubly Link List """
class Node:
    def __init__(self, prev=None, item=None, next=None) -> None:
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start=None) -> None:
        self.start = start
    
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
         n = Node(None, data, self.start)
         if not  self.is_empty():
            self.start.prev = n
         self.start = n
    
    def insert_at_last(self, data):
        temp = self.start
        if temp != None:
            while temp.next != None:
                temp = temp.next
        n = Node(temp, data, None)
        if temp == None:
            self.start = n
        else:
            temp.next = n
    
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
    
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
    
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
            temp.prev = None
    
    def delete_item(self, data):
        if self.start is None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next
    
    def __iter__(self):
        return DLLIterator(self.start)
    
    def __len__(self):
        temp = self.start
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count
    
    def __getitem__(self, index):
        count = 0
        temp = self.start
        while temp is not None:
            if count == index:
                return temp.item
            count += 1
            temp = temp.next
        raise IndexError("Doubly Link List is out of range")

class DLLIterator:
    def __init__(self, start) -> None:
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
    

myList = DLL()
myList.insert_at_start(10)
myList.insert_at_last(20)
myList.insert_after(myList.search(10), 15)
myList.insert_at_last(30)
myList.insert_at_last(40)
# print(len(myList))
print(myList[1])
for x in range(len(myList)):
    print(myList[x], end=' ')

 