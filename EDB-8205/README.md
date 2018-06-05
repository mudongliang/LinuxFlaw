# EDB-8205

## Experiment Environment

Ubuntu 11.04

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-8205/jdkchat-1.5.tar.gz
tar -xvf jdkchat-1.5.tar.gz
cd jdkchat-1.5
make
```

## Problems in Installation & Configuration


## How to trigger vulnerability

Server:

```
./jdkchat 7777
```

Client:

```
perl 8205.pl
```

## PoCs

[JDKChat 1.5 - Remote Integer Overflow (PoC)](https://www.exploit-db.com/exploits/8205/)

## Vulnerability Details & Patch

### Root Cause

### Stack Trace

### Patch

## References
