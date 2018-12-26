# LinuxFlaw

This repo records all the vulnerabilities of linux software I have reproduced in my local workspace.

If the vulnerability has both CVE-ID and EDB-ID, CVE-ID is preferred as its directory name. All the vulnerable source code packages are stored in [source-packages](https://github.com/mudongliang/source-packages)

## Vmware Workstation Images
Image Name|username|password
----------|--------|--------
[Ubuntu 8.10](https://psu.box.com/s/yzy7l5okh77xa7bwzilk90jwf1it0bs1) | exploit | exploit
[Ubuntu 10.04LTS](https://psu.box.com/s/g7pvmwsvi0a4o85j0clthkn64iuplzzl) | exploit | exploit
[CentOS 6.5](https://psu.box.com/s/afzod6ewo0sdsz86wpw5f3ynwv7mz6uv) | core | core
[CentOS 5.5](https://psu.box.com/s/rvqv9yxeywvq5rhzp212u1q8799w263s) | core | core
[Ubuntu 11.04](https://psu.box.com/s/l1xjsuue2lfibtwr9osr5d00ddnqy19y) | dzm77 | dzm77
[Ubuntu 12.04](https://psu.box.com/s/m55ncbvgmmcaua57ofhf606zhpstu4ch) | ubuntu | ubuntu
[Fedora](https://psu.box.com/s/rfxl4zw1tkv84jxc6el3fqyo8clf77je) | fedora | fedora
[OpenSUSE](https://psu.box.com/s/q940eadlnx9cwez0w0ru61he3vyhj7eu) | core | core
[Ubuntu 14.04_core](https://psu.box.com/s/uag1v3u9eboce4nylrgwc0cbcdghxu5n) | core | core
[Kali](https://psu.box.com/s/4r3zacu2uq4ni1eb8lyxh9bk6r4kkvo6) | root | kali
[Ubuntu_14.04_alex](https://psu.box.com/s/ui1kr4bgczlzb6f731xn66onc3ek799k) | research-cve | toortoor
[Ubuntu_14.04_pt](https://psu.box.com/s/tah44vnuaqj4y2ml7740ma8o9we3gy3e) | pt | pt

For details of vulnerabilities(in which virtual machine, what is the reproduction workspace, etc.), please refer to [virtualmachine.csv](./virtualmachine.csv)

If you encounter problems with keyword "Failed to lock files", you could try to delete any `.lck` or `.lock` files or folders in the directory of the problematic VM.

## CVE-ID List

- [ ] CVE-2001-0144
- [ ] CVE-2001-0550
- [x] CVE-2002-0656
- [x] CVE-2002-1496
- [x] CVE-2002-1896
- [ ] CVE-2003-0577 (Fail to reproduce)
- [x] CVE-2004-0238
- [x] CVE-2004-0270
- [x] CVE-2004-0557
- [x] CVE-2004-0597
- [x] CVE-2004-0990
- [x] CVE-2004-1120
- [x] CVE-2004-1255
- [ ] CVE-2004-1256 (Fail to reproduce)
- [x] CVE-2004-1257
- [ ] CVE-2004-1258 (Fail to reproduce)
- [ ] CVE-2004-1259 (Fail to reproduce)
- [ ] CVE-2004-1260 (Fail to reproduce)
- [x] CVE-2004-1261
- [x] CVE-2004-1262
- [x] CVE-2004-1265
- [ ] CVE-2004-1266 (Fail to reproduce)
- [x] CVE-2004-1271
- [ ] CVE-2004-1272 (Fail to reproduce)
- [x] CVE-2004-1275
- [x] CVE-2004-1278
- [x] CVE-2004-1279
- [ ] CVE-2004-1283 (Fail to reproduce)
- [x] CVE-2004-1287
- [x] CVE-2004-1288
- [x] CVE-2004-1289
- [x] CVE-2004-1290
- [x] CVE-2004-1292
- [x] CVE-2004-1293
- [x] CVE-2004-1297
- [x] CVE-2004-1298
- [x] CVE-2004-1299
- [ ] CVE-2004-1455 (Fail to reproduce)
- [x] CVE-2004-2093
- [x] CVE-2004-2167
- [x] CVE-2005-0101
- [x] CVE-2005-0199
- [x] CVE-2005-1275
- [x] CVE-2005-3120
- [x] CVE-2005-3252
- [x] CVE-2005-3862
- [x] CVE-2005-4667
- [x] CVE-2005-4807
- [x] CVE-2006-0539
- [x] CVE-2006-1148
- [x] CVE-2006-1542
- [x] CVE-2006-2025
- [x] CVE-2006-2362
- [x] CVE-2006-2465
- [x] CVE-2006-2656
- [x] CVE-2006-2971
- [x] CVE-2006-3082
- [x] CVE-2006-3124
- [x] CVE-2006-3581
- [x] CVE-2006-3582
- [x] CVE-2006-3746
- [x] CVE-2006-4018
- [x] CVE-2006-4089
- [x] CVE-2006-4144
- [x] CVE-2006-4182
- [x] CVE-2006-4812
- [x] CVE-2006-5276
- [x] CVE-2006-5295
- [x] CVE-2006-5465
- [x] CVE-2006-5815
- [x] CVE-2006-6563
- [x] CVE-2007-0368
- [x] CVE-2007-1001
- [x] CVE-2007-1286
- [x] CVE-2007-1371
- [x] CVE-2007-1383
- [x] CVE-2007-1465
- [x] CVE-2007-1777
- [x] CVE-2007-1825
- [x] CVE-2007-2052
- [x] CVE-2007-2446
- [x] CVE-2007-2683
- [x] CVE-2007-2872
- [x] CVE-2007-3473
- [x] CVE-2007-3947
- [x] CVE-2007-4060
- [x] CVE-2007-4965
- [x] CVE-2007-5301
- [x] CVE-2007-5759 
- [x] CVE-2007-6015
- [x] CVE-2007-6454
- [x] CVE-2007-6697
- [x] CVE-2007-6731
- [x] CVE-2008-1721
- [x] CVE-2008-1767
- [x] CVE-2008-1801
- [x] CVE-2008-1802
- [x] CVE-2008-1887
- [ ] CVE-2008-2292 (Fail to reproduce)
- [x] CVE-2008-2315
- [ ] CVE-2008-2316 (Fail to reproduce)
- [x] CVE-2008-2950
- [x] CVE-2008-3142
- [x] CVE-2008-3143
- [ ] CVE-2008-3144 (Fail to reproduce)
- [x] CVE-2008-4864
- [x] CVE-2008-5031
- [x] CVE-2008-5314
- [x] CVE-2008-5904
- [x] CVE-2009-1759
- [x] CVE-2009-1886
- [x] CVE-2009-2285
- [x] CVE-2009-2286
- [x] CVE-2009-3050
- [x] CVE-2009-3586
- [x] CVE-2009-4134
- [x] CVE-2009-4880
- [x] CVE-2009-4881
- [x] CVE-2009-5018
- [x] CVE-2010-1147
- [x] CVE-2010-1159
- [x] CVE-2010-1449
- [x] CVE-2010-1450
- [x] CVE-2010-1634
- [x] CVE-2010-1866
- [x] CVE-2010-2089
- [x] CVE-2010-2481
- [x] CVE-2010-2482
- [x] CVE-2010-2810
- [x] CVE-2010-2891
- [x] CVE-2010-2959
- [x] CVE-2010-4221
- [x] CVE-2010-4259
- [x] CVE-2010-4409
- [x] CVE-2011-0420
- [x] CVE-2011-0708
- [x] CVE-2011-0761
- [x] CVE-2011-1071
- [x] CVE-2011-1092
- [x] CVE-2011-1137
- [x] CVE-2011-1938
- [ ] CVE-2011-5033
- [x] CVE-2012-0809
- [x] CVE-2012-2386
- [x] CVE-2012-3480
- [x] CVE-2012-4409
- [x] CVE-2012-4412
- [x] CVE-2012-4424
- [ ] CVE-2012-5612
- [x] CVE-2012-5667
- [x] CVE-2012-5867
- [x] CVE-2013-0221
- [x] CVE-2013-0222
- [x] CVE-2013-0223
- [x] CVE-2013-0722
- [x] CVE-2013-2028
- [x] CVE-2013-2131
- [x] CVE-2013-3724
- [x] CVE-2013-4123
- [x] CVE-2013-4243
- [x] CVE-2013-4473
- [x] CVE-2013-4474
- [x] CVE-2013-4788
- [x] CVE-2013-7226
- [x] CVE-2013-7446
- [ ] CVE-2014-0226
- [x] CVE-2014-0749
- [x] CVE-2014-1912
- [x] CVE-2014-2851
- [x] CVE-2014-4616
- [x] CVE-2014-6277
- [x] CVE-2014-7185
- [x] CVE-2014-8322
- [x] CVE-2014-8768
- [x] CVE-2014-9295
- [x] CVE-2015-0235
- [x] CVE-2015-0252
- [x] CVE-2015-1265
- [x] CVE-2015-3205
- [x] CVE-2015-3890
- [x] CVE-2015-5895
- [x] CVE-2015-7547
- [x] CVE-2015-7805
- [x] CVE-2015-8396
- [x] CVE-2015-8617
- [x] CVE-2015-8668
- [x] CVE-2016-0728
- [x] CVE-2016-10092
- [x] CVE-2016-10093
- [x] CVE-2016-10094
- [x] CVE-2016-10095
- [x] CVE-2016-10251
- [x] CVE-2016-10268
- [x] CVE-2016-10269
- [x] CVE-2016-10270
- [x] CVE-2016-10271
- [x] CVE-2016-10272
- [x] CVE-2016-2233
- [x] CVE-2016-2563
- [x] CVE-2016-4557
- [x] CVE-2016-5636
- [x] CVE-2016-6187
- [x] CVE-2016-6516
- [ ] CVE-2016-6832 (Fail to reproduce) 
- [ ] CVE-2016-7393 (Fail to reproduce)
- [x] CVE-2016-7445
- [ ] CVE-2016-7477 (Fail to reproduce)
- [ ] CVE-2016-8655
- [ ] CVE-2016-8676
- [ ] CVE-2016-8678
- [ ] CVE-2016-8883
- [x] CVE-2016-8887 (***PoC not found***)
- [x] CVE-2016-9560
- [ ] CVE-2016-9819
- [ ] CVE-2016-9820
- [ ] CVE-2016-9821
- [ ] CVE-2017-10688
- [x] CVE-2017-11403
- [x] CVE-2017-12858
- [ ] CVE-2017-12936
- [ ] CVE-2017-12937
- [ ] CVE-2017-14103
- [x] CVE-2017-14638
- [x] CVE-2017-14639
- [x] CVE-2017-14640
- [x] CVE-2017-14641
- [x] CVE-2017-14642
- [x] CVE-2017-14643
- [x] CVE-2017-14644
- [x] CVE-2017-14645
- [x] CVE-2017-14646
- [x] CVE-2017-15020
- [x] CVE-2017-15938
- [x] CVE-2017-15939
- [x] CVE-2017-5502
- [x] CVE-2017-5852
- [x] CVE-2017-5853
- [x] CVE-2017-5854
- [x] CVE-2017-5855
- [x] CVE-2017-5886
- [x] CVE-2017-5974
- [x] CVE-2017-5975
- [x] CVE-2017-5976
- [x] CVE-2017-5977
- [x] CVE-2017-5978
- [x] CVE-2017-5980
- [x] CVE-2017-6840
- [x] CVE-2017-6842
- [x] CVE-2017-6843
- [x] CVE-2017-6847
- [x] CVE-2017-6848
- [x] CVE-2017-6850
- [x] CVE-2017-6852
- [x] CVE-2017-7184
- [x] CVE-2017-7308
- [x] CVE-2017-7378
- [x] CVE-2017-7379
- [x] CVE-2017-7380
- [x] CVE-2017-7381
- [x] CVE-2017-7382
- [x] CVE-2017-7383
- [x] CVE-2017-7533
- [x] CVE-2017-7596
- [x] CVE-2017-7597
- [x] CVE-2017-7598
- [x] CVE-2017-7599
- [x] CVE-2017-7600
- [x] CVE-2017-7601
- [x] CVE-2017-7602
- [x] CVE-2017-7606
- [x] CVE-2017-8890
- [x] CVE-2017-9038
- [ ] CVE-2017-9147
- [x] CVE-2017-9154
- [x] CVE-2017-9160
- [x] CVE-2017-9162
- [x] CVE-2017-9163
- [x] CVE-2017-9164
- [x] CVE-2017-9165
- [x] CVE-2017-9166
- [x] CVE-2017-9167
- [x] CVE-2017-9168
- [x] CVE-2017-9169
- [x] CVE-2017-9170
- [x] CVE-2017-9171
- [x] CVE-2017-9172
- [x] CVE-2017-9173
- [x] CVE-2017-9174
- [x] CVE-2017-9177
- [x] CVE-2017-9180
- [x] CVE-2017-9182
- [x] CVE-2017-9183
- [x] CVE-2017-9184
- [x] CVE-2017-9186
- [x] CVE-2017-9189
- [x] CVE-2017-9190
- [x] CVE-2017-9191
- [x] CVE-2017-9192
- [x] CVE-2017-9193
- [x] CVE-2017-9194
- [x] CVE-2017-9195
- [x] CVE-2017-9196
- [x] CVE-2017-9204
- [x] CVE-2017-9205
- [x] CVE-2017-9206
- [x] CVE-2017-9207
- [x] CVE-2018-9138


## EDB-ID List

- [x] EDB-10334
- [x] EDB-10617
- [x] EDB-10634
- [x] EDB-11644
- [x] EDB-14083
- [x] EDB-14452
- [x] EDB-14904
- [x] EDB-15054
- [x] EDB-15062
- [x] EDB-15705
- [x] EDB-17611
- [x] EDB-17806
- [x] EDB-19987
- [x] EDB-20479
- [x] EDB-23523
- [ ] EDB-25411
- [ ] EDB-26915
- [ ] EDB-28679
- [ ] EDB-30142
- [ ] EDB-30648
- [ ] EDB-31761
- [ ] EDB-31915
- [ ] EDB-33251
- [ ] EDB-33949
- [x] EDB-34164
- [ ] EDB-35450
- [ ] EDB-36024
- [ ] EDB-36229
- [ ] EDB-36388
- [ ] EDB-36881
- [ ] EDB-37546
- [ ] EDB-37743
- [ ] EDB-37777
- [ ] EDB-37975
- [ ] EDB-37987
- [ ] EDB-37988
- [ ] EDB-38597
- [x] EDB-38616
- [ ] EDB-38617
- [ ] EDB-38681
- [ ] EDB-38685
- [ ] EDB-38857
- [ ] EDB-39285
- [ ] EDB-39406
- [ ] EDB-39502
- [ ] EDB-39673
- [ ] EDB-39692
- [ ] EDB-39733
- [ ] EDB-39734
- [ ] EDB-39747
- [ ] EDB-39764
- [ ] EDB-39800
- [ ] EDB-39810
- [ ] EDB-39842
- [ ] EDB-39875
- [ ] EDB-40023
- [ ] EDB-40025
- [x] EDB-8205
- [x] EDB-890
- [x] EDB-9264

## Other-ID list

- [x] Gentoo-Bug-70090
- [x] Sourceware-Bug-21877
- [x] Sourceware-Bug-21878
- [x] Sourceware-Bug-21880

- Some vulnerabilities without CVE ID listed in Gentoo Security Blog

## Classification

### Stack Overflow

### Heap Overflow

### BSS/Data Overflow

### Use-After-Free

### Double Free

### Invalid Free

### Null Pointer

- [EDB-23523](https://github.com/mudongliang/LinuxFlaw/tree/master/EDB-23523)

### Uninitialized Memory

- [CVE-2009-2950](https://github.com/mudongliang/LinuxFlaw/tree/master/CVE-2009-2950)

### Stack exhaustion

- [CVE-2008-5314](https://github.com/mudongliang/LinuxFlaw/tree/master/CVE-2008-5314)

### Heap exhaustion

### Memory Leak

- [Sourceware-Bug-21877](https://github.com/mudongliang/LinuxFlaw/tree/master/Sourceware-Bug-21877)
- [Sourceware-Bug-21878](https://github.com/mudongliang/LinuxFlaw/tree/master/Sourceware-Bug-21878)
- [Sourceware-Bug-21880](https://github.com/mudongliang/LinuxFlaw/tree/master/Sourceware-Bug-21880)

## Note

### Enable/Disable Security mitigations

Please refer to [Traditional Mitigation](https://github.com/hardenedlinux/TraditionalMitigation) Repository to check security mitigations and how to enable/disable them.
