# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

import sys
from logutil import LogUtil
from importenv import ImportEnvKeyEnum
import importenv as setting

from fork import Fork
from pipesample import PipeSample
from sharedctypes import Sharedctypes
from process_pool import ProcessPool
from multi_args import MultiArgs

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(PYTHON_APP_HOME + '/config/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

if __name__ == '__main__':
  # 起動引数の取得
  # args = sys.argv
  # args[0]はpythonのファイル名。
  # 実際の引数はargs[1]から。

  args = sys.argv
  
  if args[1] == 'fork':
    Fork.main()
  elif args[1] == 'pipe':
    PipeSample.main()
  elif args[1] == 'sharedctypes':
    Sharedctypes.main()
  elif args[1] == 'process_pool':
    process_pool = ProcessPool(int(args[2]))
    process_pool.main()
  elif args[1] == 'multi_args':
    MultiArgs.run()
  else:
    ValueError('{} is not defined.'.format(args[1]))