# -*- coding: utf-8 -*-
from multiprocessing import Process, Value, Array

class Sharedctypes:
  @staticmethod
  def f(n,a):
    n.value = 3.141592
    for i in range(len(a)):
      a[i] = -a[i]
  
  @staticmethod
  def main():
    num = Value('d', 0.0)
    arr = Array('i', range(10))
    
    p = Process(target=Sharedctypes.f, args=(num, arr))
    p.start()
    p.join()
    
    print(num.value)
    print(arr[:])