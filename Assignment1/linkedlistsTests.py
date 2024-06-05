from linkedlists import LinkedList


def test_append_first():
    linked_list = LinkedList()
    linked_list.append_first(1)
    assert linked_list.head.value == 1
    assert linked_list.head.next == None
    assert linked_list.count == 1

    linked_list.append_first(2)
    assert linked_list.head.value == 2  
    assert linked_list.head.next.value == 1  
    assert linked_list.count == 2
    print("")
    print("inputting 1, 2 into append_first.")
    print("append_first Linked list:")
    linked_list.display_list()
    print("")


def test_add_last():
    linked_list = LinkedList()
    linked_list.add_last(1)
    assert linked_list.head.value == 1
    assert linked_list.head.next == None
    assert linked_list.count == 1

    linked_list.add_last(2)
    assert linked_list.head.value == 1  
    assert linked_list.tail.value == 2
    assert linked_list.count == 2
    print("inputting 1, 2 into add_last.")
    print("add_last Linked list:")
    linked_list.display_list()
    print("")

def test_add_sorted():
    linked_list = LinkedList()
    print("inputting 3, 5, 1, 7, 2 into add_sorted.")
    print("add_sorted Linked list:")
    linked_list.add_sorted(3)
    linked_list.display_list()
    linked_list.add_sorted(5)
    linked_list.display_list()
    linked_list.add_sorted(1)
    linked_list.display_list()
    linked_list.add_sorted(7)
    linked_list.display_list()
    linked_list.add_sorted(2)
    linked_list.display_list()
    print("")

def test_delete_get_first_node():
    linked_list = LinkedList()
    print("delete_get_first_node Linked list:")
    linked_list.add_sorted(3)
    linked_list.add_sorted(5)
    linked_list.add_sorted(1)
    linked_list.add_sorted(7)
    linked_list.add_sorted(2)
    linked_list.display_list()
    x = linked_list.delete_get_first_node()
    print(f"Value returned: {x}")
    linked_list.display_list()
    x = linked_list.delete_get_first_node()
    print(f"Value returned: {x}")
    linked_list.display_list()
    x = linked_list.delete_get_first_node()
    print(f"Value returned: {x}")
    linked_list.display_list()
    x = linked_list.delete_get_first_node()
    print(f"Value returned: {x}")
    linked_list.display_list()
    print("")

def test_delete_get_last_node():
    linked_list = LinkedList()
    print("delete_get_last_node Linked list:")
    linked_list.add_sorted(3)
    linked_list.add_sorted(5)
    linked_list.add_sorted(1)
    linked_list.add_sorted(7)
    linked_list.add_sorted(2)
    linked_list.display_list()
    x = linked_list.delete_get_last_node()
    print(f"Value returned: {x}")
    linked_list.display_list()
    x = linked_list.delete_get_last_node()
    print(f"Value returned: {x}")
    linked_list.display_list()
    x = linked_list.delete_get_last_node()
    print(f"Value returned: {x}")
    linked_list.display_list()
    x = linked_list.delete_get_last_node()
    print(f"Value returned: {x}")
    linked_list.display_list()
    x = linked_list.delete_get_last_node()
    print(f"Value returned: {x}")
    linked_list.display_list()
    print("")

def test_delete_index():
    linked_list = LinkedList()
    print("delete_index Linked list:")
    linked_list.append_first(3)
    linked_list.append_first(5)
    linked_list.append_first(1)
    linked_list.append_first(7)
    linked_list.append_first(2)
    linked_list.display_list()
    print("deleting the 4th index(last)")
    linked_list.delete_index(4)
    linked_list.display_list()
    print("deleting the 0th index(first)")
    linked_list.delete_index(0)
    linked_list.display_list()
    print("deleting the 1st index(middle)")
    linked_list.delete_index(1)
    linked_list.display_list()
    print("")

def test_length():
    linked_list = LinkedList()
    print("length Linked list:")
    print("EMPTY")
    len = linked_list.length()
    print(f"Value returned: {len}")
    print("adding node with value 3")
    linked_list.append_first(3)
    linked_list.display_list()
    len = linked_list.length()
    print(f"Value returned: {len}")
    print("adding node with value 2")
    linked_list.append_first(2)
    linked_list.display_list()
    len = linked_list.length()
    print(f"Value returned: {len}")
    print("adding node with value 1")
    linked_list.append_first(1)
    linked_list.display_list()
    len = linked_list.length()
    print(f"Value returned: {len}")
    print("")

def test_rmv_dupes():
    linked_list = LinkedList()
    linked_list.append_first(1)
    linked_list.append_first(2)
    linked_list.append_first(3)
    linked_list.append_first(3)
    linked_list.append_first(2)
    linked_list.append_first(5)
    linked_list.append_first(6)
    linked_list.append_first(1)
    linked_list.append_first(5)
    print("rmv_dupes Linked list:")
    linked_list.display_list()
    print("running rmv_dupes on the linked list....")
    linked_list.rmv_dupes()
    linked_list.display_list()
    print("")    

def test_reverse():
    print("creating a Linked list:")
    linked_list = LinkedList()
    linked_list.append_first(1)
    linked_list.append_first(2)
    linked_list.append_first(3)
    linked_list.append_first(4)
    linked_list.append_first(5)
    linked_list.append_first(6)
    linked_list.append_first(7)
    linked_list.display_list()
    print("running reverse on linked list")
    linked_list.reverse(linked_list.head)
    linked_list.display_list()



if __name__ == "__main__":
    test_append_first()
    test_add_last()
    test_add_sorted()
    test_delete_get_first_node()
    test_delete_get_last_node()
    test_delete_index()
    test_length()
    test_rmv_dupes()
    test_reverse()
    print("Tests Passed")