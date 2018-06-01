# EDB-14904

## Experiment Environment

Ubuntu 10.04

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-14904/fcrackzip-1.0.tar.gz
tar -xvf fcrackzip-1.0.tar.gz
cd fcrackzip-1.0
./configure
make
```

## Problems in Installation & Configuration


## How to trigger vulnerability

```
./fcrackzip -p $(python -c 'print "A"*440') file.zip
```

## PoCs

[FCrackZip 1.0 - Local Buffer Overflow (PoC)](https://www.exploit-db.com/exploits/14904/)

## Vulnerability Patch

### Root Cause

### Stack Trace

### Patch

## References
