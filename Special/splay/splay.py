#!/usr/bin/env python
#coding: utf-8

class Node:
  def __init__(self, key, data):
    self.key = key
    self.data = data
    self.left = None
    self.right = None

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

def _splay(root, key):
  if (not root or root.key == key):
    return root
  if (root.key > key):
    # move left
    left = root.left
    if (not left): return root
    else:
      if (left.key > key):
        # zig-zig
        left.left = _splay(left.left, key)
        if (left.left):
          root.left = rightRotate(root.left)
      elif (left.key < key):
        # zig-zag
        left.right = _splay(left.right, key)
        if (left.right):
          root.left = leftRotate(root.left)
      else:
        # already find the target, we needn't do the rotation any more
        pass

      return rightRotate(root) if root.left else root
  else:
    # move right
    right = root.right
    if (not right): return root
    else:
      if (right.key < key):
        # zig-zig right to left
        right.right = _splay(right.right, key)
        if (right.right):
          root.right = leftRotate(root.right)
      elif (right.key > key):
        # zig-zag right
        right.left = _splay(right.left, key)
        if (right.left):
          root.right = rightRotate(root.right)

      return leftRotate(root) if root.right else root 

def _add(node, key, data):
  if (not node):
    return Node(key, data)
  if (node.key > key):
    node.left = _add(node.left, key, data)
  elif (node.key < key):
    node.right = _add(node.right, key, data)
  else:
    node.data = data
  return node

def _findBiggestInRight(node):
  if (not node.right):
    return node.left, node
  node.right, biggest = _findBiggestInRight(node.right)
  return node, biggest

def _flatten(node, id=0, layer=0, result=[]):
  if (node):
    if (not result[layer]): result[layer] = []
    result[layer].append({ "id": id, "key": node.key, "data": node.data })
    _flatten(node.left, 2*id+1, layer+1, result)
    _flatten(node.right, 2*id+2, layer+1, result)
  return result

class Splay:
  def __init__(self):
    self.root = None
    self.size = 0

  def add(self, key, data):
    self.root = _add(self.root, key, data)
    self.size += 1

  def delete(self, key):
    self.search(key)
    root = self.root
    if (root.key == key):
      if (not root.left):
        # first, root doesn't have left child
        self.root = root.right
      elif (not root.left.right):
        # second, root.left has no right child
        root.left.right = root.right
        self.root = root.left
      else:
        # the last one, find the biggest one in the right branch and take it as new root
        root.left.right, biggestNode = _findBiggestInRight(root.left.right)
        biggestNode.left = root.left
        biggestNode.right = root.right
        self.root = biggestNode

  def search(self, key):
    self.root = _splay(self.root, key)

  def print(self):
    flattenedListSize = self.size
    result = _flatten(self.root, result=[None]*flattenedListSize)
    for l in result:
      if (l):
        l.sort(key=lambda x: x['id'])
        print(l)

if (__name__ == '__main__'):
  print('begin')
  splay = Splay()
  splay.add(15, {'a': 'b'})
  splay.add(23, 3)
  splay.add(14, (1, 4))
  splay.add(27, 'abcdefg')
  splay.add(66, None)
  splay.add(72, [1,2])
  splay.add(57, [[1,2], [0,1]])
  splay.add(32, 'abcde')
  splay.add(38, 'abcdefgh')
  splay.print()
  splay.search(32)
  print('after search a')
  splay.print()
  # splay.search(32)
  # print('after search b')
  splay.delete(32)
  print('after deleta a')
  splay.print()
  print('end')
