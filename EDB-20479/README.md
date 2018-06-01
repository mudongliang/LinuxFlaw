# CVE/EDB ID

## Experiment Environment

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-20479/pure-ftpd-1.0.21.tar.gz
tar -xvf pure-ftpd-1.0.21.tar.gz
cd pure-ftpd-1.0.21
./configure
make
sudo make install
```

## Problems in Installation & Configuration


## How to trigger vulnerability

Server:

```
sudo /usr/local/sbin/pure-ftpd 
```

Client:

```
perl poc.pl
```

## PoCs

[Pure-FTPd 1.0.21 (CentOS 6.2 / Ubuntu 8.04) - Null Pointer Dereference Crash (PoC)](https://www.exploit-db.com/exploits/20479/)

## Vulnerability Details & Patch

### Root Cause

### Stack Trace

### Patch

## References
