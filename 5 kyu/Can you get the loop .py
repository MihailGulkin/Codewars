def loop_size(node):
    currNode = node
    allNodes = {}
    length = 1
    while True:
        if (currNode in allNodes):
            return length - allNodes[currNode]
        allNodes[currNode] = length
        currNode = currNode.next
        length += 1
