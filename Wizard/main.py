# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers(l1, l2):
    s1 = "".join(map(str,l1))
    s2 = "".join(map(str,l2))
    n1 = int(s1) 
    n2 = int(s2)
    s=n1+n2
    return list(map(int,str(s)))
  
l1 = [1,2,3,4]
l2 = [1,0]
print(addTwoNumbers(l1,l2))
        