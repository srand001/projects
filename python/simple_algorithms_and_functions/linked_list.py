#----------------------------------------------------------------------------------------------
# A linked list is a type of linear data structure individual items are not necessarily 
# at contiguous locations. The individual items are called nodes and connected with each 
# other using links.
#
# A node contains two things first is data and second is a link that connects it with 
# another node.

# The first node is called the head node and we can traverse the whole list using this
# head and next links.
#    
#
# There are four basic forms of linked lists:
#
# Singly linked lists
# Doubly linked lists
# Circular linked lists
# Doubly circular linked list
#
# Designed by Surjit Randhawa 2026
#----------------------------------------------------------------------------------------------


# Singly linked list

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def findLowestValue(head):
  minValue = head.data
  currentNode = head.next
  while currentNode:
    if currentNode.data < minValue:
      minValue = currentNode.data
    currentNode = currentNode.next
  return minValue

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("The lowest value in the linked list is:", findLowestValue(node1))