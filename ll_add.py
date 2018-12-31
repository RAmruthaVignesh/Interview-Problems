'''
Given two numbers represented by two lists, write a function that returns sum of the .
The sum list is list representation of addition of two input numbers.
Input:
  First List: 5->6->3  // represents number 365
  Second List: 8->4->2 //  represents number 248
Output
  Resultant list: 3->1->6  // represents number 613
'''

import linkedlist

class ll_add_class(object):
    def __init__(self):
        pass

    def add_two_ll(self,head1,head2):
        '''
        This function adds 2 linked list where node 1 is the least significant digit
        :param head1: head node of list 1
        :param head2: head node of list 2
        :return: integer sum of the lists
        '''
        curr_node1 = head1
        curr_node2 = head2
        remainder=0
        position = 1
        sum_string= ""
        while(curr_node1 and curr_node2):
            temp = remainder+curr_node1.value+curr_node2.value
            sum_val = temp// 10**0 %10
            remainder = temp//10*1 %10
            sum_string= str(sum_val)+sum_string
            curr_node1 = curr_node1.next_node
            curr_node2 = curr_node2.next_node
        if curr_node1 is None and curr_node2 is not None:
            while curr_node2:
                temp = remainder+curr_node2.value
                sum_val = temp// 10**0 %10
                remainder = temp//10*1 %10
                sum_string = str(sum_val) + sum_string
                curr_node2 = curr_node2.next_node
        elif curr_node2 is None and curr_node1 is not None:
            while curr_node1:
                temp = remainder+curr_node1.value
                sum_val = temp// 10**0 %10
                remainder = temp//10*1 %10
                sum_string = str(sum_val) + sum_string
                curr_node1 = curr_node1.next_node
        return int(sum_string)

#creating Linkedlist 1
ll1_node1= linkedlist.linkedlistnode(5)
ll1_node2= linkedlist.linkedlistnode(6)
ll1_node3= linkedlist.linkedlistnode(3)
ll1_node1.next_node= ll1_node2; ll1_node2.next_node=ll1_node3; ll1_node3.next_node= None

#creating Linkedlist 2
ll2_node1= linkedlist.linkedlistnode(8)
ll2_node2= linkedlist.linkedlistnode(4)
ll2_node3= linkedlist.linkedlistnode(2)
ll2_node1.next_node= ll2_node2; ll2_node2.next_node=ll2_node3; ll2_node3.next_node= None

adding_ll = ll_add_class()
sum_ll = adding_ll.add_two_ll(ll1_node1, ll2_node1)
print(sum_ll)