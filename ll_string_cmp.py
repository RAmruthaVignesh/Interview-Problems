'''
Given two linked lists, represented as linked lists (every character is a node in linked list).
Write a function compare() that works similar to strcmp(), i.e., it returns 0 if both strings are same,
1 if first linked list is lexicographically greater, and -1 if second string is lexicographically greater.
Input: list1 = g->e->e->k->s->a
       list2 = g->e->e->k->s->b
Output: -1

Input: list1 = g->e->e->k->s->a
       list2 = g->e->e->k->s
Output: 1

Input: list1 = g->e->e->k->s
       list2 = g->e->e->k->s
Output: 0
'''

import linkedlist

class cmp_ll:
    def __init__(self):
        pass

    def get_string_from_ll(self, head):
        '''
        This function traverses through the linked list and returns a string of the items in the list
        :param head: head node of the linked list
        :return: str_from_ll : string
        '''
        curr_node = head
        str_from_ll = ""
        while curr_node.next_node is not None:
            str_from_ll= str_from_ll+ curr_node.value
            curr_node = curr_node.next_node
        return str_from_ll+curr_node.value

    def compare_ll_notoptimal(self,head1,head2):
        """
        This function takes in head nodes of 2 linked lists, converts them to string and
        compares the 2 strings directly. This has complexity O(4n) as it traverses both the lists and then
        compares them. This can be optimized still. see the next function for optimal solution.
        :param head1: head node of list 1
        :param head2: head node of list 2
        :return: comparison result
        """
        string1 = self.get_string_from_ll(head1)
        string2 = self.get_string_from_ll(head2)
        print("The strings to compare are {} and {}".format(string1, string2))
        if string1 > string2:
            return 1
        elif string1 < string2:
            return -1
        else:
            return 0

    def cmp_ll_optimal(self,head1, head2):
        '''
        This function compares 2 lists while traversing. The complexity is O(2n)
        :param head1:
        :param head2:
        :return:
        '''
        curr_node1 = head1
        curr_node2= head2
        while curr_node1 and curr_node2:
            if curr_node1.value != curr_node2.value:
                #If the values of current node of list 1 and 2 are different and
                # if the list 1 value > list2 value, return 1
                #else return -1
               if curr_node1.value > curr_node2.value:
                   return 1
               else:
                   return -1
            #If the next node of list 1 is not none, set current node as next node
            if curr_node1.next_node is not None:
                curr_node1 = curr_node1.next_node
            #If the next node of list 1 is None, but the next node of list 2 is not none, return -1
            else:
                if curr_node2.next_node is not None:
                    return -1
            #If the next node of list 2 is not none, set current node as next node, else return 1
            if curr_node2.next_node is not None:
                curr_node2 = curr_node2.next_node
            else:
                return 1
        #If all matches return 0
        return 0


#creating Linkedlist 1
ll1_node1= linkedlist.linkedlistnode("g")
ll1_node2= linkedlist.linkedlistnode("e")
ll1_node3= linkedlist.linkedlistnode("e")
ll1_node4= linkedlist.linkedlistnode("k")
ll1_node5= linkedlist.linkedlistnode("s")
ll1_node6= linkedlist.linkedlistnode("a")
ll1_node1.next_node= ll1_node2; ll1_node2.next_node=ll1_node3; ll1_node3.next_node= ll1_node4;
ll1_node4.next_node = ll1_node5; ll1_node5.next_node= ll1_node6; ll1_node6.next_node = None

#creating Linkedlist 2
ll2_node1= linkedlist.linkedlistnode("g")
ll2_node2= linkedlist.linkedlistnode("e")
ll2_node3= linkedlist.linkedlistnode("e")
ll2_node4= linkedlist.linkedlistnode("k")
ll2_node5= linkedlist.linkedlistnode("s")
ll2_node6= linkedlist.linkedlistnode("b")
ll2_node1.next_node= ll2_node2; ll2_node2.next_node=ll2_node3; ll2_node3.next_node= ll2_node4;
ll2_node4.next_node = ll2_node5; ll2_node5.next_node= ll2_node6; ll2_node6.next_node = None

#compare 2 linked lists and get 1 if the list 1 > list2, get -1 if list 1< list 2 and 0 if they are same
cmp_class = cmp_ll()
get_cmp_out = cmp_class.compare_ll_notoptimal(ll1_node1, ll2_node1)
# print("The comparison output is {}".format(get_cmp_out))

get_cmp = cmp_class.cmp_ll_optimal(ll1_node1,ll2_node1)
print("The comparison output is {}".format(get_cmp))



