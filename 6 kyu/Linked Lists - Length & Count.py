class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def length(node):
    if node:
        node_count = 0
        while node:
            node = node.next
            node_count += 1
        return node_count
    return 0


def count(node, data):
    if node:
        node_count = 0
        while node:
            if node.data == data:
                node_count += 1
            node = node.next
        return node_count
    return 0
