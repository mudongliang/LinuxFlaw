# EDB-24981

## Experiment Environment

Ubuntu 14.04 LTS

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-24981/jpegtoavi-1.5.tar.gz

tar -xvf jpegtoavi-1.5.tar.gz
cd jpegtoavi-1.5

make
```

## Problems in Installation & Configuration

## How to trigger vulnerability

./jpegtoavi-1.5/jpegtoavi -f 1 640 480 < 10.list

## PoCs

[JPegToAvi 1.5 - File List Buffer Overflow](https://www.exploit-db.com/exploits/24981/)

[securityfocus](http://www.securityfocus.com/bid/11976/info)

## Vulnerability Details & Patch

### Root Cause

```
jpegtoavi.c:126

	strcpy(tmp->name, fn);
```

### Stack Trace

```
(gdb) info stack
#0  0xbfffe780 in ?? ()
#1  0xbfffe780 in ?? ()
#2  0xbfffe780 in ?? ()
```

## References
