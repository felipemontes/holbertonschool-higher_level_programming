#!/usr/bin/python3
class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def __str__(self):
        strr = []
        tmp = self.__head
        while (tmp):
            strr.append(str(tmp.data))
            tmp = tmp.next_node
        strr.sort(key=int)
        return ('\n'.join(strr))

    def sorted_insert(self, value):
        if self.__head is None:
            newnode = Node(value)
            newnode.data = value
            newnode.next_node = self.__head
            self.__head = newnode
        else:
            newnode = Node(value, None)
            newnode.data = value
            newnode.next_node = self.__head
            self.__head = newnode
