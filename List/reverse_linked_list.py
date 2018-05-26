class Node:
    def __init__(self, a, d, n):
        self.address = a
        self.data = d
        self.next = n
        self.prev = -1

def createNodeList(start, list_address, list_data, list_next):
    list_node = []
    prev = 's'
    cur_address = start

    while cur_address != -1:
        i = list_address.index(cur_address)
        newNode = Node(list_address[i], list_data[i], list_next[i])
        newNode.prev = prev
        prev = newNode.address
        cur_address = newNode.next

    return list_node


    