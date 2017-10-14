# EDB-25030

## Experiment Environment

CentOS 6.4

Ubuntu 14.04

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-25030/unrtf-0.19.3.tar.gz

tar -xvf unrtf-0.19.3.tar.gz
cd unrtf-0.19.3

make
```

## Problems in Installation & Configuration

## How to trigger vulnerability

```
./unrtf-0.19.3/unrtf 81.rtf
```

## PoCs

[GNU UnRTF 0.19.3 - Font Table Conversion Buffer Overflow](https://www.exploit-db.com/exploits/25030/)

[securityfocus(http://www.securityfocus.com/bid/12030/info)

## Vulnerability Details & Patch

### Root Cause

```
convert.c:344

		strcat(name,tmp);
```

### Stack Trace

`nfo stack
#0  0x08048de0 in process_font_table (w=0x925dc48) at convert.c:346
#1  0x0804acd2 in cmd_fonttbl (w=0x925dc18, align=0, has_param=0 '\000', param=0) at convert.c:1774
#2  0x0804bc78 in word_print_core (w=0x925dc18) at convert.c:2792
#3  0x0804bd9a in word_print_core (w=0x925dbf8) at convert.c:2842
#4  0x0804bd9a in word_print_core (w=0x925dba8) at convert.c:2842
#5  0x0804befa in word_print (w=0x925dba8) at convert.c:2901
#6  0x0804ca08 in main (argc=2, argv=0xbfe33344) at main.c:206``
```

## References
