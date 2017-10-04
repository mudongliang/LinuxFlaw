# EDB-23523

## Experiment Environment
Ubuntu 14.04 LTS

## INSTALL & Configuration
```
wget https://ftp.gnu.org/gnu/gdb/gdb-7.5.1.tar.gz
tar xvf gdb-7.5.1.tar.gz
cd gdb-7.5.1
CFLAGS="-g -O0" CXXFLAGS="-g -O0" .configure
make -j
```

## Problems in Installation & Configuration

cannnot allocate virtual memory, virtual memory exhausted

Solution: use `make -j4` instead of `make -j` to constrain number of threads for compilation

linux-nat.h:63:18: error: field 'siginfo' has incomplete type

Reason: Glibc removes `struct siginfo` from \<bits\/siginfo.h\> and replaces it with POSIX-defined `siginfo_t`

Solution: [patch](https://gist.github.com/arachsys/3060032)

## How to trigger vulnerability
```
wget https://github.com/IOActive/FileFormatFuzzing/raw/master/ELFAntiDebuggingTools/gdb_751_elf_shield.c

gcc -Wall gdb_751_elf_shield.c -o gdb_751_elf_shield 
```
write a simple but normal c program by yourself, say evil.c
```
gcc -g evil.c -o evil
.gdb_751_elf_shield ./evil
```
change to build/gdb/bin
```
./gdb/gdb ../../../trigger/evil
```

## PoCs
[edb](https://www.exploit-db.com/exploits/23523/)

## Vulnerability Details & Patch

### Root Cause

### Stack Trace

## References
[analysis](http://blog.ioactive.com/2012/12/striking-back-gdb-and-ida-debuggers.html)
