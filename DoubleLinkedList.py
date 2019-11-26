import time

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
        
     
# ''''''    def inserValueAtEnd(self,value):
#         currentNode=self.head
#         while currentNode.get_nextnode()!=None :
#             currentNode=currentNode.get_nextnode()
#         newNode=Node() 
#         newNode.set_data(value)
#         newNode.set_pre_node(currentNode)
#         newNode.get_nextnode(None)
#         currentNode.get_nextnode(newNode)
#         self.length+=1'''
# et=time.time()   
# head=Node()
# head.insertValueAtStarting(21)
# head.insertValueAtStarting(22)
# 
# head.insertValueAtStarting(24)
# 
# head.insertValueAtStarting(23)
# 
# head.insertValueInLast(100)
# 
# head.addValueAfter(215, 22)
# 
# head.deleteAtStarting()
# 
# head.Display()  
# print()
# print(time.time()-et)