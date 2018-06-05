# EDB-19987

## Experiment Environment

CentOS 6.5

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/blob/master/EDB-19987/PingTunnel-0.72.tar.gz
tar -xvf PingTunnel-0.72.tar.gz
cd PingTunnel
make
```

## Problems in Installation & Configuration

## How to trigger vulnerability

Server:

```
sudo ./ptunnel -c lo
```

Client:

```
sudo ./ptunnel-dos.py 127.0.0.1
```


## PoCs

[ptunnel 0.72 - Remote Denial of Service](https://www.exploit-db.com/exploits/19987/)

## Vulnerability Details & Patch

### Root Cause

### Stack Trace

### Patch

## References
