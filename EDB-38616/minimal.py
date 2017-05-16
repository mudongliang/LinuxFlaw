import array
a = array.array("B")
a.fromstring(b'x'*0x10000)
a.fromstring(a)
a.fromstring(a)
