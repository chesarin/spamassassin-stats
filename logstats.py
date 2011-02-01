#!/usr/bin/env python
import bz2

udata = bz2.BZ2File("spamlog.20101222.bz2",'r')
sentinel=0;

for line in udata:
    sentinel += 1

print "The total number of lines is ",sentinel
udata.close()








