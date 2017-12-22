# EDB-24984

## Experiment Environment

CentOS 6.5

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-24984/2fax304.tgz
tar -xvf 2fax304.tgz
cd 2fax-3.04/
gcc -o 2fax 2fax.c
```

## Problems in Installation & Configuration

## How to trigger vulnerability

```
./2fax 13.txt 13.tiff
```

## PoCs

[2Fax 3.0 Tab Expansion - Buffer Overflow](https://www.exploit-db.com/exploits/24984/)

## Vulnerability Details & Patch

### Root Cause

### Stack Trace

## References

[](http://securesoftware.list.cr.yp.to/archive/0/21)
