# EDB-39406

## Experiment Environment

Ubuntu 14.04

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-39406/ytree-1.94.tar.gz
tar -xvf ytree-1.94.tar.gz
cd ytree-1.94

make
```

## Problems in Installation & Configuration

## How to trigger vulnerability

At first, put the PoC file into the root directory of ytree;

Then, `python 39406.py`

## PoCs

[yTree 1.94-1.1 - Local Buffer Overflow](https://www.exploit-db.com/exploits/39406/)

## Vulnerability Patch

### Root Cause

### Stack Trace

## References
