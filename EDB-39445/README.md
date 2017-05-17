# EDB-39445

## Experiment Environment

Ubuntu 14.04 LTS

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-39445/ntp-4.2.6p5.tar.gz

tar -xvf ntp-4.2.6p5.tar.gz
cd ntp-4.2.6p5/

./configure
make
sudo make install
```

## Problems in Installation & Configuration

## How to trigger vulnerability

```
sudo cp ntp.conf /etc/ntp.conf
sudo cp ntp.keys /etc/ntp.keys

gcc -o exploit 39445.c

sudo /usr/local/bin/ntpd -d

./exploit
```

## PoCs

[NTPd ntp-4.2.6p5 - ctl_putdata() Buffer Overflow](https://www.exploit-db.com/exploits/39445/)

## Vulnerability Details & Patch

### Root Cause

```
ntpd/ntp_control.c:1027

        memmove((char *)datapt, dp, (unsigned)dlen);
```

### Stack Trace

```
(gdb) info stack
#0  read_variables (rbufp=0x811efa8, restrict_mask=0) at ntp_control.c:2294
#1  0x08066cd7 in receive (rbufp=0x811efa8) at ntp_proto.c:372
#2  0x08059be5 in ntpdmain (argc=0, argc@entry=2, argv=0xbffff85c, argv@entry=0xbffff854) at ntpd.c:1150
#3  0x0804adcb in main (argc=2, argv=0xbffff854) at ntpd.c:356
```

## References

[1] [Project Zero](https://googleprojectzero.blogspot.com/2015/01/finding-and-exploiting-ntpd.html)
