#!/usr/bin/env python
#coding: utf-8

import random
import math
random.seed()

MAX_PRIORITY = 100

def leftRotate(node):
  ptmp = node.right
  lptmp = ptmp.left
  ptmp.left = node
  node.right = lptmp
  return ptmp

def rightRotate(node):
  ptmp = node.left
  rptmp = ptmp.right
  ptmp.right = node
  node.left = rptmp
  return ptmp

def _add(root, key, data):
  if (not root):
    return Node(data, key)
  
  if (key <= root.key):
    root.left = _add(root.left, key, data)
    # right rotate
    if (root.left and root.left.priority > root.priority):
      root = rightRotate(root)
  else:
    root.right = _add(root.right, key, data)
    # left rotate
    if (root.right and root.right.priority > root.priority):
      root = leftRotate(root)

  return root

def _delete(root, key):
  success = False
  if (not root): return root, success

  if (root.key < key):
    root.right, success = _delete(root.right, key)
  elif (root.key > key):
    root.left, success = _delete(root.left, key)
  elif (not root.left and not root.right):
    return None, True
  elif (root.left and root.right):
    method = rightRotate if (root.left.priority > root.right.priority) else leftRotate
    node = method(root)
    return _delete(node, key)
  else:
    return root.left or root.right, True
  
  return root, success

def _search(root, key):
  if (not root or root.key == key):
    return root
  if (root.key < key):
    _search(root.left, key)
  else:
    _search(root.right, key)

def _flatten(node, id=0, layer=0, result=[]):
  if (node):
    if (not result[layer]): result[layer] = []
    result[layer].append({ "id": id, "key": node.key, "priority": node.priority })
    _flatten(node.left, 2*id+1, layer+1, result)
    _flatten(node.right, 2*id+2, layer+1, result)
  return result

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
    self.root = None
    self.size = 0

  def add(self, key, data):
    node = _add(self.root, key, data)
    # if (not self.root):
    self.root = node
    self.size += 1
  
  def search(self, key):
    _search(self.root, key)

  def print(self):
    flattenedListSize = self.size
    result = _flatten(self.root, result=[None]*flattenedListSize)
    for l in result:
      if (l):
        l.sort(key=lambda x: x['id'])
        print(l)

  def delete(self, key):
    self.root, success = _delete(self.root, key)
    if (success):
      self.size -= 1

if (__name__ == '__main__'):
  print('begin')
  treap = Treap()
  treap.add(15, {'a': 'b'})
  treap.add(23, 3)
  treap.add(14, (1, 4))
  treap.add(27, 'abcdefg')
  treap.add(66, None)
  treap.add(72, [1,2])
  treap.add(57, [[1,2], [0,1]])
  treap.add(32, 'abcde')
  treap.add(38, 'abcdefgh')
  treap.print()
  print('length of treap: {0}'.format(treap.size))
  print('begin delete')
  treap.delete(66)
  treap.print()
  print('length of treap after delete: {0}'.format(treap.size))
  print('end')
