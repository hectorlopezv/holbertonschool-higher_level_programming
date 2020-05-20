#!/usr/bin/python3
"""Nonde python implementation"""


class Node:
    """Node Class
    """
    def __init__(self, data, next_node=None):
        """init of node class

        Arguments:
            data {int} -- integer value for constructor

        Keyword Arguments:
            next_node {Node} -- Node object for the next Node (default: {None})
        """
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """data

        Returns:
            data -- return the integer that the node is storing
        """
        return self.__data

    @data.setter
    def data(self, value):
        """data

        Arguments:
            value {int} -- integer value

        Raises:
            TypeError: data is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        """next node

        Returns:
            node -- node that is going to be the next
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next node

        Arguments:
            value {Node} -- the next node

        Raises:
            TypeError: when is not a Node and its != None
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Single linke list implementation
    """
    def __init__(self):
        """contructor for single linke list class
        """
        self.__head = None
        self.temp = self.__head

    def __str__(self):
        """string representation of class

        Returns:
            print the linked list  -- going to print 
        """
        temp_node = self.__head
        resu = ""
        while temp_node is not None:
            resu += str(temp_node.data) + "\n"
            temp_node = temp_node.next_node 
        return resu[:-1]
    
    def __iter__(self):
        """iterator 

        Returns:
            self -- when the object its already a iterator return self
        """
        return self
    
    def __next__(self):
        """next

        Raises:
            StopIteration: stop iteration when all the  conditions are meet

        Returns:
            return a node -- move the iterator 1 position
        """
        if self.temp is None:
            raise StopIteration
        else:
            temp = self.temp
            self.temp = self.temp.next_node
            return temp

    def sorted_insert(self, value):
        """[summary]

        Arguments:
            value {[type]} -- [description]
        """
        if self.__head is None:
            self.__head = Node(value)
            return
        temp_node = self.__head
        prev = None
        while temp_node is not None:

            if value < temp_node.data and prev is None:
                self.__head = Node(value, temp_node)
                self.temp = self.__head
                prev = self.__head 
                return
            if value < temp_node.data and prev is not None:
                prev.next_node = Node(value, temp_node)
                return
            prev = temp_node
            temp_node = temp_node.next_node
        prev.next_node = Node(value)
        return



