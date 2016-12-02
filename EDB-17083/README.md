# EDB-17083

## 实验环境

Ubuntu 14.04 LTS

## 安装（源码,...）

下载 HT-Editor 源码，解压，编译，

```sh
$ ./configure
$ make
```

### 安装过程中的Problems

## 软件启动

```sh
$ ht file-to-be-edited
```

## 漏洞测试

### Simple Test

```sh
$ ./ht $(perl -e 'print "A"x5000')

```

### Try to exploit

1. 首先，将库中的poc - 17803.pl 拷贝到对应的软件根目录下
2. 然后，执行这个 perl 文件

```sh
$ perl 17083.pl

```

## 漏洞 Patch

## References

[1] [HT-Editor Source Code](https://www.exploit-db.com/apps/ce7698b80035bce297374b338045dadd-ht-2.0.18.tar.gz)
