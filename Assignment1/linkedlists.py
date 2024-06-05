class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:


    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    
    def display_list(self):
        current_node = self.head
        while current_node != None:
            print(f"{current_node.value} -->", end = ' ')
            current_node = current_node.next
        print("None")
        print()


    def append_first(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.count +=1
            return
        else:
            new_node.next = self.head
            self.head = new_node
            self.count +=1
            


    def add_last(self, value):
        new_node = Node(value)
        ##if theres no header, the first node is also the last one
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.count +=1
            return
        ##itterate over the current linked list to find
        ##last linked list to add as last node
        else: 
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node
            self.tail = new_node
            self.count +=1


    def insert_at_index(self, value, index):
        new_node = Node(value)
        position = 0  ##itteration counter
        current_node = self.head
        ##if position is 0, then we use previously made method to add to first
        if position == index:
            self.append_first(value)
        else:
            while(current_node.next != None and position-1 != index):
                position += 1
                current_node = current_node.next 
            ##if .next = none, then we're at the
            ##end of the linked list, so we use previously made method add to last
            if current_node.next == None: 
                self.add_last(value)
            ##if the position reached the index -1, then we add the new node
            else:
                new_node.next = current_node.next
                current_node.next = new_node
                self.count +=1


    def add_sorted(self, value):
        current_node = self.head
        new_node = Node(value)
        ##special case if linked list is empty
        if self.head is None:
            self.append_first(value)
            return
        ##special case for when new value is less than header
        elif self.head.value > value:
            new_node.next = self.head
            self.head = new_node
            return
        ##loop to find correct position for new value
        ##first argument for when at the end of the list and cant compare to empty node
        while(current_node.next is not None 
        and current_node.next.value < new_node.value):
            current_node = current_node.next
        ##put the new value in the correct place, and switching value and .next 
        new_node.next = current_node.next
        current_node.next = new_node
        self.count +=1


    def delete_get_first_node(self):
        temp_node = self.head
        self.head = temp_node.next
        self.count -=1
        return temp_node.value


        
    def delete_get_last_node(self):
        ##special case for when theres only one node in linked list
        if self.head.next == None:
            self.head = self.head.next
            self.count -=1
            return None
        temp = self.head
        prev = None
        #creating the value of previous element
        #iterating till the last Node
        while temp.next != None:
            prev = temp  
            temp = temp.next
        self.tail = prev
        prev.next = prev.next.next #returning as NONE value
        self.count -=1
        return temp.value


    def delete_index(self, index):
        ##special case for deleting first index
        if index == 0:
            self.delete_get_first_node()
            return
        ##special case for deleting last index
        elif index == (self.count + 1):
            self.delete_get_last_node()
            return
        ##special case if index is outside range
        elif index < 0 or index > self.count:
            print("Invalid index")
            return
        else:
            ##curr as head, and making the counter
            current_node = self.head
            counter = 0
            ##when counter reaches the index - 1
            ##we skip over the index, by changing the previous next value
            ##to be the value of one after the index
            while counter != index - 1:
                counter +=1
                current_node = current_node.next
            current_node.next = current_node.next.next


    def length(self):
        length = 0
        current_node = self.head
        while current_node:
            length +=1
            current_node = current_node.next
        return length
    
    def rmv_dupes(self):
        ##special case if LL is empty, or has one value
        if self.head is None or self.head.next is None:
            return
        ##creating a set to put the values in 
        hashtable = set()
        current_node = self.head
        ##intitaiting the set with the head
        hashtable.add(self.head.value)
        while current_node.next:
            ##if value exists in set, delete it
            if current_node.next.value in hashtable:
                current_node.next = current_node.next.next
            ##if value doesnt exist in set, add it to set
            else:
                hashtable.add(current_node.next.value)
                current_node = current_node.next
        return

    # def recursive_reverse(self, head):
    #     if head is None or head.next is None:
    #         return head
    #     p = self.reverse(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return p

    def reverse(self, head):
        prev_node, current_node = None, head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    # def merge(self,linked_list1, linked_list2):
    # def merge_sorted
    # def split0
    # def fold
    # def value_to_index
    # def velue_to_asteriss