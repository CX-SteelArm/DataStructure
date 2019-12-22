#!/usr/bin/env python
#coding: utf-8

def _del(node, key):
  if (not node): return None
  if (node.key == key): return node.next
  node.next = _del(node.next, key)
  return node

def _reverse(pre, cur):
  if (not cur): return pre
  # edge case: at the beginning of recursive: a double linked loop
  if (cur and pre.next == cur): pre.next = None
  tmp = cur.next
  cur.next = pre
  return _reverse(cur, tmp)

class Node:
  def __init__(self, key=None):
    self.key = key
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = Node()

  def add(self, key):
    nextElm = self.head.next
    newElm = Node(key)
    newElm.next = nextElm
    self.head.next = newElm

  def delete(self, key):
    self.head = _del(self.head, key)

  def reverse(self):
    fe = self.head.next
    if (not fe): return 
    se = fe.next if fe else None
    self.head.next = _reverse(fe, se)

  def print(self):
    elements = []
    head = self.head
    while (head):
      elements.append(head.key)
      head = head.next
    print(elements)

if (__name__ == '__main__'):
  ll = LinkedList()
  print('begin')
  ll.add(34)
  ll.add(45)
  ll.add(32)
  ll.add(8)
  ll.add(14)
  ll.add(92)
  ll.add(65)
  ll.add(101)
  ll.add(67)
  ll.add(18)
  ll.print()
  ll.delete(45)
  print('after delete')
  ll.print()
  ll.reverse()
  print('after reverse')
  ll.print()
  print('end')
