# -*- coding: utf-8 -*-
import multiprocessing
from multiprocessing import Pool
import os

class MultiArgs:
  @staticmethod
  def func(arg1, arg2):
    for arg in arg2:
      print("{} * {} = {}".format(arg1, arg, arg1*arg))
  
  @staticmethod
  def wrapper(args):
    # print("{}, args : {}".format(os.getpid(), args) )
    # print("{}, args[0] : {}".format(os.getpid(), args[0]))
    # print("{}, args[1] : {}".format(os.getpid(), args[1]))
    MultiArgs.func(args[0],args[1])
  
  @staticmethod
  def sample(arg):
    print(arg)
  
  @staticmethod
  def run():
    arg1 = [1,2,3,4]
    arg2 = [5,6,7,8]
    
    args = []
    for i in range(len(arg1)):
      args.append((arg1[i],arg2))
    with Pool(multiprocessing.cpu_count()) as pool:
      pool.map(MultiArgs.wrapper, args)
    