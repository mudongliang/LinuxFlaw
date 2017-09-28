# EDB-38616

## Experiment Environment

Ubuntu 14.04 LTS

## INSTALL & Configuration

```
wget https://github.com/mudongliang/source-packages/raw/master/EDB-38616/Python-2.7.tgz

tar -xvf Python-2.7.tgz
cd Python-2.7

./configure
make
```

## Problems in Installation & Configuration

## How to trigger vulnerability

```
./python exploit.py/minimal.py
```

## PoCs

[Python 2.7 array.fromstring Method - Use-After-Free](https://www.exploit-db.com/exploits/38616/)


## Vulnerability Details & Patch

### Root Cause

```
Modules/arraymodule.c
array_fromstring(PyObject *args) {
	char *str;
	Py_ssize_t n;
	PyArg_ParseTuple(args, &str, &n); // pass args to str and n, if the str is itself 
	PyMem_RESIZE(item, char, (Py_SIZE(self) + n) * itemsize); // when preserved memory space is not enough, resize will realloc a new memory region and delete the original one, str will point to a freed memory
	memcpy(item+(Py_SIZE(self)-n)*itemsize, str, itemsize*n); // SIGSEGV here

}

```

### Stack Trace

```
(gdb) info stack
#0  __memcpy_ssse3_rep () at ../sysdeps/i386/i686/multiarch/memcpy-ssse3-rep.S:462
#1  0xb7710a84 in array_fromstring (self=0xb7435ac0, args=0xb742c2ec)
    at /home/core/workspace/program/Python-2.7/Modules/arraymodule.c:1397
#2  0x081400e2 in PyCFunction_Call (func=0xb7435f0c, arg=0xb742c2ec, kw=0x0) at Objects/methodobject.c:81
#3  0x080d9a5f in call_function (pp_stack=0xbf89c47c, oparg=1) at Python/ceval.c:4012
#4  0x080d6aa9 in PyEval_EvalFrameEx (f=0x9568e54, throwflag=0) at Python/ceval.c:2665
#5  0x080d9d0d in fast_function (func=0xb7432a3c, pp_stack=0xbf89c64c, n=0, na=0, nk=0) at Python/ceval.c:4098
#6  0x080d9b56 in call_function (pp_stack=0xbf89c64c, oparg=0) at Python/ceval.c:4033
#7  0x080d6aa9 in PyEval_EvalFrameEx (f=0x9516b0c, throwflag=0) at Python/ceval.c:2665
#8  0x080d81d9 in PyEval_EvalCodeEx (co=0xb748c530, globals=0xb74cd35c, locals=0xb74cd35c, args=0x0, argcount=0, 
    kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:3252
#9  0x080d250f in PyEval_EvalCode (co=0xb748c530, globals=0xb74cd35c, locals=0xb74cd35c) at Python/ceval.c:666
#10 0x080fc35e in run_mod (mod=0x956da58, filename=0xbf89e7e9 "exploit.py", globals=0xb74cd35c, locals=0xb74cd35c, 
    flags=0xbf89c918, arena=0x955ef60) at Python/pythonrun.c:1346
#11 0x080fc2fc in PyRun_FileExFlags (fp=0x9516b00, filename=0xbf89e7e9 "exploit.py", start=257, globals=0xb74cd35c, 
    locals=0xb74cd35c, closeit=1, flags=0xbf89c918) at Python/pythonrun.c:1332
#12 0x080fb2bc in PyRun_SimpleFileExFlags (fp=0x9516b00, filename=0xbf89e7e9 "exploit.py", closeit=1, 
    flags=0xbf89c918) at Python/pythonrun.c:936
#13 0x080fac00 in PyRun_AnyFileExFlags (fp=0x9516b00, filename=0xbf89e7e9 "exploit.py", closeit=1, flags=0xbf89c918)
    at Python/pythonrun.c:740
#14 0x08059559 in Py_Main (argc=2, argv=0xbf89ca84) at Modules/main.c:599
#15 0x080584f8 in main (argc=2, argv=0xbf89ca84) at ./Modules/python.c:23
```

## References
