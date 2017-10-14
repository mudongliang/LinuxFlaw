# EDB-9264

## Experiment Environment

Opensuse 11.1
Ubuntu 14.04

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-9264/stftp-1.1.0.tar.gz

cd stftp-1.1.0
make
```

## Problems in Installation & Configuration
```
tty.c:25:20: fatal error: curses.h: No such file or directory
```
Solution: sudo apt-get install libncurse5-dev

## How to trigger vulnerability

```
sudo python 9264.py/other_test.py/password.py

./stftp localhost
```

## PoCs

[stftp 1.10 - (PWD Response) Remote Stack Overflow (PoC)](https://www.exploit-db.com/exploits/9264/)

## Vulnerability Detail & Patch

### Root Cause

```
main.c:381

	parse_pwd(output,dir);
```

### Stack Trace

```
(gdb) info stack
#0  0x00007fa45ba70560 in strlen () from /lib64/libc.so.6
#1  0x00007fa45ba3b266 in vfprintf () from /lib64/libc.so.6
#2  0x00007fa45ba5b439 in vsprintf () from /lib64/libc.so.6
#3  0x00007fa45ba416c8 in asprintf () from /lib64/libc.so.6
#4  0x00000000004052f9 in p_header (host=0x6867666564636261 <Address 0x6867666564636261 out of bounds>, 
    dir=0x7fff641b00f0 'x' <repeats 144 times>, "abcdefghi") at misc.c:130
#5  0x000000000040240c in main (argc=2, argv=0x7fff641b0298) at main.c:382
```

## References
