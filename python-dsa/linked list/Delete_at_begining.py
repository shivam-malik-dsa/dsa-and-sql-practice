class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def delete_at_begining(self):
        if self.head is None:
            return
        self.head = self.head.next 

    def printll(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("none")    