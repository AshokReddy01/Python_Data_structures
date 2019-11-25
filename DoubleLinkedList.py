from pip._vendor.requests.api import head

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
    
    def insert_value_at_starting(self,value):
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
        
head=Node()
head.insert_value_at_starting(21)
head.insert_value_at_starting(22)

head.insert_value_at_starting(24)

head.insert_value_at_starting(23)
head.Display()  