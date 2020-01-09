#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 19:26:21 2019

@author: vikasmittal
"""

class Node:
    
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def push(self,new_data):
        new_node = Node(new_data)
        #new_node.next = self.head
        if(self.head is None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node
            
    def printlist(self,llist):
        temp = llist.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
    def removeNode(self,delete2):
        count = 1
        #check if ll doesn't exists
        if(self.head is None):
            print("Linked list does not exists")
            return None
        else:
            if delete2 == 1:
                self.head = self.head.next
                return
            prev = self.head
            temp = prev
            while(delete2 != count): 
                prev = temp
                temp = temp.next
                count = count + 1
                if temp is None:
                    print("Node {} does not exist".format(delete2))
                    return
            prev.next = temp.next
            
    def removeNodebyval(self,val):
        if(self.head is None):
            print("Linked list does not exists")
            return None
        else:
            prev = self.head
            temp = prev
            if(temp.data == val):
                self.head = temp.next
            while(temp):
                if(temp.data == val):
                    prev.next = temp.next
                    return # remove return to remove all occurences of val
                prev = temp
                temp = temp.next
            self.push(val)
    
    def insertNodeatPos(self,pos,val):
        if(self.head is None):
            return
        else:
            curr = self.head
            node = Node(val)
            count = 1
            if(pos ==1):
                tempVar = curr
                self.head = node
                node.next = tempVar
            while(curr):
                if(count+1 == pos):
                    tempVar = curr.next
                    curr.next = node
                    node.next = tempVar
                    return
                curr = curr.next
                count = count+1
                
    def sortLinkedList(self):
        curr = self.head
        while(curr.next):
            next_node = curr.next
            if(curr.data > next_node.data):
                temp = next_node.next
                if(curr == self.head):
                    self.head = curr.next
                next_node.next = curr
                curr.next = temp   
            curr = curr.next        
                    
                 
        
if __name__ == "__main__":
    llist = LinkedList()
    llist.push(10)
    llist.push(20)
    llist.push(3)
    llist.push(4)
    llist.push(2)
    #llist.removeNode(1)
    #llist.push(1)
    llist.removeNodebyval(5)
    llist.insertNodeatPos(1,17)
    llist.printlist(llist)
    print("----------------")
    llist.sortLinkedList()
    llist.printlist(llist)