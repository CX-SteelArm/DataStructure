#!/usr/bin/env python
#coding: utf-8

import random
random.seed()

MAX_PRIORITY = 1000000

class Node:
  def __init__(self, data, key):
    self.data = data
    self.key = key
    self.priority = random.randint(1, MAX_PRIORITY)
    # as a BST
    self.left = None
    self.right = None

class Treap:
  def __init__(self):
    self.head = None

  def leftRotate(self, node):
    ptmp = node.right
    lptmp = ptmp.left
    ptmp.left = node
    node.right = lptmp
  
  def rightRotate(self, node):
    ptmp = node.left
    rptmp = ptmp.right
    ptmp.right = node
    node.left = rptmp

  def add(self, root, key, data):
    if (~root):
      return Node(data, key)
    
    if (key <= root.key):
      root.left = self.add(root.left, key, data)
      # right rotate
      if (root.left.priority > root.priority):
        self.rightRotate(root)
    else:
      root.right = self.add(root.right, key, data)
      # left rotate
      if (root.right.priority < root.priority):
        self.leftRotate(root)
  
  def search(self, root, key):
    if (~root or root.key == key):
      return root
    if (root.key < key):
      self.search(root.left, key)
    else:
      self.search(root.right, key)

  def delete(self, node):
    pass

if (__name__ == '__main__'):
  node = Node({}, 'node1')
  print(node, node.data, node.key, node.priority)
