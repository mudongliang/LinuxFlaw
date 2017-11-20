# EDB-38685

## Experiment Environment

Ubuntu 14.04 LTS

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-38685/tack-1.07-1.tar.gz
tar -xvf tack-1.07-1.tar.gz

LIBS="-ltic" ./configure
make
```

## Problems in Installation & Configuration

**1. undefined reference to `_nc_tic_expand`**

>linking tack ...    
>../tack-test/edit.o: In function `show_changed':    
>/home/core/tack/tack-test/edit.c:476: undefined reference to `_nc_tic_expand'    
>/home/core/tack/tack-test/edit.c:477: undefined reference to `_nc_tic_expand'

>../tack-test/edit.o: In function `build_change_menu':

>/home/core/tack/tack-test/edit.c:971: undefined reference to `_nc_tic_expand'

>../tack-test/edit.o: In function `show_value':

>/home/core/tack/tack-test/edit.c:351: undefined reference to `_nc_reset_input'

>/home/core/tack/tack-test/edit.c:352: undefined reference to `_nc_trans_string'

>../tack-test/edit.o: In function `change_one_entry':

>/home/core/tack/tack-test/edit.c:891: undefined reference to `_nc_tic_expand'

>/home/core/tack/tack-test/edit.c:881: undefined reference to `_nc_reset_input'

>/home/core/tack/tack-test/edit.c:882: undefined reference to `_nc_trans_string'

>../tack-test/edit.o: In function `save_info':

>/home/core/tack/tack-test/edit.c:250: undefined reference to `_nc_tic_expand'

>collect2: error: ld returned 1 exit status

>make: *** [tack] Error 1

**Solution:**

    LIBS="-ltic" ./configure

Details in [tack's configure script doesn't find separate tic library](https://lists.gnu.org/archive/html/bug-ncurses/2012-02/msg00009.html)

## How to trigger vulnerability

At first, put the PoC file into the root directory of tack;

Then, `python 38685.py`

## PoCs

[TACK 1.07 - Local Stack Based Buffer Overflow](https://www.exploit-db.com/exploits/38685/)


## Vulnerability Details & Patch

### Root Cause

### Stack Trace

# References
