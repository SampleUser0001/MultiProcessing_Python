# -*- coding: utf-8 -*-
from multiprocessing import Pool
import random
import time

class ProcessPool:
  """ 乱数を生成して、重複している値の件数をカウントする。
      重複している数が最も多い値のみを出力する。
  """

  RANDOM_COUNT = 10000
  MAX_INT = 100
  
  def __init__(self, pool_size):
    self.pool_size = pool_size
    self.sliced_random_list = []
    self.random_list = []

    # 乱数の生成
    for i in range(0, ProcessPool.RANDOM_COUNT):
      self.random_list.append(random.randint(1, ProcessPool.MAX_INT))

    # Poolによるマルチプロセスは配列を引数に取る。
    # 生成した乱数の配列をプロセス数個の配列に分割する。
    # random_listをこの件数ごとに区切る。
    len_unit = int(len(self.random_list) / self.pool_size)
    for i in range(0, int(ProcessPool.RANDOM_COUNT/len_unit)):
      if i == int(ProcessPool.RANDOM_COUNT/len_unit) - 1:
        # プロセス数が引数のときに余りが出ないようにする
        self.sliced_random_list.append(self.random_list[i*len_unit:])
      else:
        self.sliced_random_list.append(self.random_list[i*len_unit:(i+1)*len_unit])

  def fetch(self, args):
    """ 重複チェック本体。マルチプロセス処理する。
    """
    double_dict = {}
    for i in self.random_list:
      for j in args:
        if i == j:
          key = str(i)
          if key not in double_dict.keys():
            double_dict[key] = 0
          double_dict[key] += 1
    return double_dict

  def main(self):
    """ 重複チェック開始 """

    start = time.time()
    print('start : {}'.format(start))

    result_list = []
    slice_index = 0
    with Pool(self.pool_size) as pool:
      result_list = pool.map(self.fetch, self.sliced_random_list)

    # マルチプロセスで取得した結果をマージする。
    double_dict = {}
    for result in result_list:
      for value in result.keys():
        if value not in double_dict.keys():
          double_dict[value] = 0
        double_dict[value] += result[value]

    max_value = None
    max_count = 0
    for value in double_dict.keys():
      if max_count < double_dict[value]:
        max_count = double_dict[value]
        max_value = value
        
    print('value : {} , count : {}'.format(max_value, max_count))
    print('finish : {}'.format(time.time() - start))
