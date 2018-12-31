'''
Given two linked lists, insert nodes of second list into first list at alternate positions of first list.
For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6,
the first list should become 5->12->7->10->17->2->13->4->11->6 and second list should become empty.
The nodes of second list should only be inserted when there are positions available.
For example, if the first list is 1->2->3 and second list is 4->5->6->7->8, then first list should
become 1->4->2->5->3->6 and second list to 7->8.
Use of extra space is not allowed (Not allowed to create additional nodes), i.e., insertion must be done in-place.
Expected time complexity is O(n) where n is number of nodes in first list.
'''

import linkedlist

class ll_merge_class(object):
    def __init__(self):
        pass

    def merge(self, head1, head2):
        curr_node1 = head1
        curr_node2 = head2
        while curr_node1 and curr_node2:
            next_node1= curr_node1.next_node
            next_node2 = curr_node2.next_node
            curr_node2.next_node = curr_node1.next_node
            curr_node1.next_node = curr_node2
            curr_node1 = next_node1
            curr_node2 = next_node2


#creating Linkedlist 1
ll1_node1= linkedlist.linkedlistnode(5)
ll1_node2= linkedlist.linkedlistnode(7)
ll1_node3= linkedlist.linkedlistnode(17)
ll1_node4= linkedlist.linkedlistnode(13)
ll1_node5= linkedlist.linkedlistnode(11)
ll1_node6= linkedlist.linkedlistnode(10)
ll1_node1.next_node= ll1_node2; ll1_node2.next_node=ll1_node3; ll1_node3.next_node= ll1_node4;
ll1_node4.next_node = ll1_node5; ll1_node5.next_node= ll1_node6; ll1_node6.next_node = None

#creating Linkedlist 2
ll2_node1= linkedlist.linkedlistnode(12)
ll2_node2= linkedlist.linkedlistnode(10)
ll2_node3= linkedlist.linkedlistnode(2)
ll2_node4= linkedlist.linkedlistnode(4)
ll2_node5= linkedlist.linkedlistnode(6)
ll2_node6= linkedlist.linkedlistnode(5)
ll2_node1.next_node= ll2_node2; ll2_node2.next_node=ll2_node3; ll2_node3.next_node= ll2_node4;
ll2_node4.next_node = ll2_node5; ll2_node5.next_node= ll2_node6; ll2_node6.next_node = None

if __name__ == '__main__':
    merge_ll = ll_merge_class()
    merge_ll.merge(ll1_node1, ll2_node1)
    traverse_ll = linkedlist.ll_operations()
    traverse_ll.traverse(ll1_node1)
