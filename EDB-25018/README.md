# EDB-25018

## Experiment Environment

Ubuntu 14.04 LTS

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-25018/abc2mtex1.6.1.tar.gz

tar -xvf abc2mtex1.6.1.tar.gz
cd abc2mtex1.6.1

make 
```

## Problems in Installation & Configuration

## How to trigger vulnerability

```
./abc2mtex 79.abc
```

## PoCs

[ABC2MTEX 1.6.1 - Process ABC Key Field Buffer Overflow](https://www.exploit-db.com/exploits/25018/)

## Vulnerability Details & Patch

### Root Cause

```
abc.c:1663

        (void) strcat(key,entry->KEY);
```

### Stack Trace

```
(gdb) info stack
#0  0x0804e251 in process_abc (title=0xe3d0bfbf, titles=-335757377, entry=0xebfcbfbf, 
    key_comment=0xebfcbfbf <Address 0xebfcbfbf out of bounds>, bars=0xec5abfbf <Address 0xec5abfbf out of bounds>, 
    tune=0xe25abfbf <Address 0xe25abfbf out of bounds>, input=0xe28cbfbf <Address 0xe28cbfbf out of bounds>, 
    output_type=-335757377, nbars=-335757377, force=-335757377, hash_array=0xebfcbfbf) at abc.c:1670
#1  0xe3d0bfbf in ?? ()
#2  0xe3d0bfbf in ?? ()
#3  0xebfcbfbf in ?? ()
```

## References
