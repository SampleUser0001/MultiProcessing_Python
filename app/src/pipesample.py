# -*- coding: utf-8 -*-
from multiprocessing import Process, Pipe

class PipeSample():
  @staticmethod
  def main():
    parent_conn, child_conn = Pipe()

    # カンマは必要。
    child = Process(target=PipeSample.work, args=(child_conn,))
    
    for item in (
      42,
      'some string',
      {'one':1},
      ['hogehoge','piyopiyo','fugafuga'],
      CustomClass(),
      None
      ):
      print("親：送信：{}".format(item))
      parent_conn.send(item)
      
    child.start()
    child.join()

  @staticmethod
  def work(connection):
    while True:
      instance = connection.recv()

      if instance:
        print("子：受信：{}".format(instance))
      else:
        return

class CustomClass():
  """ 転送用クラス """
  pass;
