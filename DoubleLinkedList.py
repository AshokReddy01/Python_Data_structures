import time
from pympler import asizeof
class Node:
    length=0
    head=None
    def __init__(self,data=None,preNode=None,nextNode=None):
        self.data=data
        self.preNode=preNode
        self.nextNode=nextNode

    def get_data(self):
        return self.data


    def get_pre_node(self):
        return self.preNode


    def get_nextnode(self):
        return self.nextNode


    def set_data(self, value):
        self.data = value


    def set_pre_node(self, value):
        self.preNode = value


    def set_nextnode(self, value):
        self.nextNode = value
        
    def hasNext(self):
        return self.nextNode()!=None  
    
    def insertValueAtStarting(self,value):
        current=self.head
        
        newNode=Node()
        newNode.set_data(value)
        if self.length==0:
            self.head=newNode
        else:
            newNode.set_pre_node(None)
            newNode.set_nextnode(current)
            current.set_pre_node(newNode)
            self.head=newNode
            
        self.length+=1   
         
    def Display(self):
        currentNode=self.head
       
        print("From Starting to end : ",currentNode.get_data() ,end=" ")
        while currentNode.get_nextnode()!=None:
            currentNode=currentNode.get_nextnode()
            print(currentNode.get_data(),end=" ")
        print()
  
        print("From back to front : ",currentNode.get_data() ,end=" ")
        while currentNode.get_pre_node()!=None:
            currentNode=currentNode.get_pre_node()
            print(currentNode.get_data(),end=" ")
    
    def insertValueInLast(self,value):
        currentNode=self.head
        while currentNode.get_nextnode()!=None:
            currentNode=currentNode.get_nextnode()
        newNode=Node()
        newNode.data=value
        newNode.set_nextnode(None)
        newNode.set_pre_node(currentNode)
        currentNode.set_nextnode(newNode)
        self.length+=1
        
    def addValueAfter(self,data,value):
        currentNode=self.head
        prevNode=None
        while currentNode.get_data()!= value:
            prevNode=currentNode
            currentNode=currentNode.get_nextnode()
        prevNode=currentNode
        currentNode=currentNode.get_nextnode()
        
        newNode=Node()
        newNode.set_data(data)
        newNode.set_nextnode(currentNode)
        newNode.set_pre_node(prevNode)
        currentNode.set_pre_node(newNode)
        prevNode.set_nextnode(newNode)
        self.length+=1
        
    def deleteAtStarting(self):
        currentNode=self.head
        self.head=currentNode.get_nextnode()
        self.head.set_pre_node(None)  
        self.length-=1
        
    def deleteAtEnding(self):
        currentNode=self.head
        preNode=None
        while currentNode.get_nextnode()!=None:
            preNode=currentNode
            currentNode=currentNode.get_nextnode()
        preNode.set_nextnode(None)
        currentNode.set_pre_node(None)
        self.length-=1
        del currentNode     
        
# ''def inserValueAtEnd(self,value):
#         currentNode=self.head
#         while currentNode.get_nextnode()!=None :
#             currentNode=currentNode.get_nextnode()
#         newNode=Node() 
#         newNode.set_data(value)
#         newNode.set_pre_node(currentNode)
#         newNode.get_nextnode(None)
#         currentNode.get_nextnode(newNode)
#         self.length+=1


# et=time.time()   
# head=Node()
# #Size In bytes
# print("\nMemory 0st node    : ",asizeof.asizeof(head))
# head.insertValueAtStarting(21)
# print("\nMemory 1st node    : ",asizeof.asizeof(head))
# head.insertValueAtStarting(22)
#  
# print("\nMemory  2nd node  : ",asizeof.asizeof(head))
# head.insertValueAtStarting(24)
#  
# print("\nMemory  3nd node  : ",asizeof.asizeof(head))
# head.insertValueAtStarting(23)
#  
# print("\nMemory  4nd node  : ",asizeof.asizeof(head))
# head.insertValueInLast(100)
#  
# print("\nMemory  5nd node  : ",asizeof.asizeof(head))
# head.addValueAfter(215, 22)
#  
# head.deleteAtStarting()
# head.deleteAtEnding()
# head.Display()  
# print("\nMemory    : ",asizeof.asizeof(head))
# print("List Length : ",head.length)
# print("Time to do  : ",time.time()-et)