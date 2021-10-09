# MultiProcessing Python

Pythonのマルチプロセスを使ってみる。

## 実行

### fork

Javaで言うThreadやRunnableインスタンスを明示的に生成する方法。

``` sh
docker-compose run python fork
```

### Pipe

Pythonのマルチプロセスはプロセス間でメモリ共有がされない。
Javaで言うQueue？  

``` sh
docker-compose run python pipe
```

### sharedctypes

マルチプロセス間で共通のメモリ空間を使用する。  
基本データ型のみ設定可能。

``` sh
docker-compose run python sharedctypes
```

## 参考

- [【Python】マルチプロセスについて:Qiita](https://qiita.com/y518gaku/items/db3b0ced6d62b616f961)
