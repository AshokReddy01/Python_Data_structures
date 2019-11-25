import time
class Node:
    length=0
    head=None
    #Node creation and setters and getters
    def __init__(self,Data=None,NextNode=None):
        self.data=Data
        self.nextNode=NextNode
    def setData(self,data):
        self.data=data
    def getData(self):
        return self.data
    def getNext(self):
        return self.nextNode
    def setNext(self,nextNode):
        self.nextNode=nextNode
    def hasNext(self):
        return self.nextNode !=None
    def insert_at_back(self,data):
        newnode=Node()
        newnode.setData(data)
        if(self.head==None):
            self.head=newnode
            self.length+=1
        else:
            current=self.head
            while current.getNext() !=None:
                current=current.getNext()
            current.setNext(newnode)
            self.length+=1
    #display the list    
    def display(self):
        current=self.head
        print(current.getData(),end=" ")
        while current.hasNext():
            current=current.getNext() 
            print(current.getData(),end=" ") 
        print()    
#insert a value at starting of the lis
    def insert_at_starting(self,data):
        newnode=Node()
        newnode.setData(data)
        if(self.length==0):
            self.head=newnode
            self.length+=1
        else:
            newnode.setNext(self.head)
            self.head=newnode
        self.length+=1
        
    def delete_last(self):
        if self.length==0:
            print("Nothing in linkedlist")
        else:
            current=self.head
            prev=self.head
            while current.hasNext():
                prev=current
                current=current.getNext()
            prev.setNext(None)
            self.length-=1
            
            
    def delete_first(self):
        if self.length==0:
            print("Nothing to delete")
        else:
            self.head=self.head.getNext()
        self.length-=1
        
        
    def delete_a_value(self,value):
        if self.length==0:
            print("Empty list")
        else:
            prev=self.head
            current=self.head
            while current.getData()!=value:
                prev=current
                current=current.getNext()
            prev.setNext(current.getNext())
            self.length-=1
            
            
#create a object and example
# head=Node()
# head.insert_at_back( 25)
# head.insert_at_starting(12)
# head.insert_at_back( 35)
# head.insert_at_starting(13)
# head.display()
# head.delete_last()
# head.display()
# head.delete_first()
# head.display()
# head.delete_a_value(25)
# head.display()
