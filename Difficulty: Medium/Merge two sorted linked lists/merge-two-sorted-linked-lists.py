#User function Template for python3
'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self,head1, head2):
        # code here
        if not head1 :
            return head2 
            
        if not head2:
            return head1 
        
        if head1.data < head2.data:
            head = head1
            cur1 = head1.next
            cur2 = head2 
            
        else :
            head = head2 
            cur2 = head2.next 
            cur1 = head1 
            
        cur = head 
        
        while cur1 and cur2 :
            if cur1.data < cur2.data :
                cur.next = cur1 
                cur1 = cur1.next 
                
            else:
                cur.next =  cur2
                cur2 = cur2.next 
            cur = cur.next    
                
        if cur1 :
            cur.next = cur1 
            
        if cur2 :
            cur.next = cur2
            
        return head
                
            
                
            
            
            
        
            
        
            
        
            
        


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    print()
    print("~")


def insert_sorted(head, data):
    new_node = Node(data)
    if not head or head.data >= data:
        new_node.next = head
        return new_node

    current = head
    while current.next and current.next.data < data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        input1 = list(map(int, input().split()))
        input2 = list(map(int, input().split()))

        head1 = None
        for item in input1:
            head1 = insert_sorted(head1, item)

        head2 = None
        for item in input2:
            head2 = insert_sorted(head2, item)

        obj = Solution()
        merged_head = obj.sortedMerge(head1, head2)
        print_list(merged_head)

# } Driver Code Ends