#!/usr/bin/python3
class Node:
    '''Represents a node'''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''Get value from __data field attribute'''
        return self.__data

    @data.setter
    def data(self, value):
        '''Set value for __data field attribute'''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        '''Get value from __next_node field'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''Set value for __next_node field'''
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        '''Represent a singly linked list'''
        self.__head = None

    def sorted_insert(self, value):
        '''Create a new instance of Node and add it to the linked list'''
        new = Node(value)
        if self.__head is None:
            self.__head = new
        else:
            tmp = self.__head
            if tmp.data > value:
                new.next_node = self.__head
                self.__head = new
            else:
                while (tmp.next_node is not None and
                        tmp.next_node.data < value):
                    tmp = tmp.next_node
                new.next_node = tmp.next_node
                tmp.next_node = new

    def __str__(self):
        '''Assign data __data field values into a string'''
        result = " "
        tmp = self.__head
        while (tmp.next_node is not None):
            result += str(tmp.data) + "\n"
            tmp = tmp.next_node
        result += str(tmp.data)
        return result
