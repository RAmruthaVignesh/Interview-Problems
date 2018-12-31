'''
This file creates a singly-linked linked list
'''

class linkedlistnode(object):
    def __init__(self,value, next_node=None):
        self.value = value
        self.nextnode = next_node

#Traversing linkedlist given head
class ll_operations(object):
    def __init__(self):
        pass

    def traverse(self, node):
        '''
        This function takes in the head node and traverses through the entire linked list
        :param node: Head node of the linked list
        '''
        self.node = node
        print(node.value)
        if node.next_node != None:
            self.traverse(node.next_node)

    def insert_node_at_end(self, head, new_value):
        '''
        This has complexity O(n)
        :param head: head node of the linked list
        :param new_value: value to be inserted
        '''
        print("Before inserting new node at the end, the linked list looks like")
        self.traverse(head)
        new_node = linkedlistnode(new_value)
        new_node.next_node = None
        self.node.next_node = new_node
        print("After inserting new node at the end, the linked list looks like")
        self.traverse(head)

    def insert_node_sorted(self, head, val_to_ins):
        '''
        Given a sorted linked list and a value to insert, write a function to insert the value in sorted way.
        :param head: head node
        :param val_to_ins: new value to insert
        :return:
        Complexity O(n)
        '''
        curr_node = head
        new_node = linkedlistnode(val_to_ins)
        if curr_node != None:
            print("Before inserting new node, the linked list looks like")
            self.traverse(head)
            while curr_node.value < val_to_ins:
                prev_node = curr_node
                curr_node = curr_node.next_node
                if curr_node == None:
                    break
            prev_node.next_node=new_node
        else:
            head= new_node
        new_node.next_node = curr_node
        print("After inserting new node, the linked list looks like")
        self.traverse(head)


    def delete_node(self, head, val_to_del):
        print("Before deleting a new node, the linked list looks like")
        self.traverse(head)
        curr_node = head
        while curr_node.value != val_to_del:
            prev_node = curr_node
            curr_node = curr_node.next_node
        prev_node.next_node = curr_node.next_node
        print("After deleting a new node, the linked list looks like")
        self.traverse(head)

if __name__ == '__main__':
    #Creating nodes and assigning values
    node1 = linkedlistnode(3)
    node2 = linkedlistnode(5)
    node3 = linkedlistnode(10)

    #connecting the nodes
    node1.next_node = node2
    node2.next_node = node3
    node3.next_node = None

    #Traversing linkedlist given head
    linked_list = ll_operations()
    linked_list.insert_node_at_end(node1, 15)

    #deleting a given node
    linked_list.delete_node(node1, 5)
    linked_list.delete_node(node1, 15)

    linked_list.insert_node_sorted(node1, 15)
    linked_list.insert_node_sorted(node1, 12)
    linked_list.insert_node_sorted(None, 12)




