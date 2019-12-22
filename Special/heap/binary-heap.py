#!/usr/bin/env python
#coding: utf-8

import math

def _buildHeap(base, l, index):
  if (index >= l): return
  left = index * 2 + 1
  right = left + 1
  _buildHeap(base, l, left)
  _buildHeap(base, l, right)
  _3rebuild(base, l, index, left, right)

def _3rebuild(base, l, index, left, right):
  rebuildLeft, rebuildRight = False, False
  if (left < l and base[left] < base[index]):
    rebuildLeft = True
  if (right < l and base[right] < base[index]):
    rebuildRight = True
  if (rebuildLeft and rebuildRight and base[left] <= base[right]):
    rebuildRight = False
  if (rebuildLeft):
    swap(base, left, index)
    _3rebuild(base, l, left, left * 2 + 1, left * 2 + 2)
  if (rebuildRight):
    swap(base, right, index)
    _3rebuild(base, l, right, right * 2 + 1, right * 2 + 2)

def swap(base, l, r):
  tmp = base[l]
  base[l] = base[r]
  base[r] = tmp

class BinaryHeap:
  def __init__(self, base=[]):
    self.base = base
    # build heap in O(n)
    _buildHeap(self.base, len(base), 0)

  def add(self, key):
    self.base.append(key)
    base = self.base
    l = len(base) - 1
    m = math.floor((l - 1) / 2)
    while m >= 0:
      if (base[m] > base[l]):
        swap(base, m, l)
        l = m
        m = math.floor((l - 1) / 2)
      else:
        break
  
  def delMin(self):
    base = self.base
    last = base.pop()
    if (len(base) > 0):
      base[0] = last
      _3rebuild(base, len(base), 0, 1, 2)

  def decreaseKey(self, key):
    pass

  def increaseKey(self, key):
    pass

  def print(self):
    print(self.base)

if (__name__ == '__main__'):
  ll = BinaryHeap([34, 45, 32, 8, 14, 92, 65, 101, 67, 18])
  print('begin')
  ll.print()
  ll.add(23)
  ll.add(12)
  ll.add(64)
  print('after add')
  ll.print()
  ll.delMin()
  print('after delMin')
  ll.print()
  print('end')
