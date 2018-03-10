# linked lists in python

class Node:

   def __init__(self,data,nextNode=None):
       self.data = data
       self.nextNode = nextNode

   def getData(self):
       return self.data.name

   def setData(self,val):
       self.data = val

   def getNextNode(self):
       return self.nextNode

   def setNextNode(self,val):
       self.nextNode = val

class LinkedList:

   def __init__(self,head = None):
       self.head = head
       self.size = 0

   def getSize(self):
       return self.size

   def addNode(self,data):
       newNode = Node(data,self.head)
       self.head = newNode
       self.size+=1
       return True

   def findNode(self, value):
       curr = self.head
       while curr:
           if curr.getData() == value:
	       return True
	   curr = curr.getNextNode()
       return False
       
   def removeNode(self, value):
       prev = None
       curr = self.head
       while curr:
           if curr.getData() == value:
	       if prev:
		   prev.setNextNode(curr.getNextNode())
	       else:
	           self.head = curr.getNextNode()
	       return True
	   prev = curr
	   curr = curr.getNextNode()
       return False

   def printNode(self):
       curr = self.head
       while curr:
           print(curr.data.name)
           curr = curr.getNextNode()


