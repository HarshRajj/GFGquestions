'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        
        
        temp = head 
        end = Node(x)
        
        if not head :
            return end
        while temp.next!= None :
            temp = temp.next 
            
        temp.next = end
    
        return head
        
        