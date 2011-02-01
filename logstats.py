#!/usr/bin/env python
import bz2;

udata = bz2.BZ2File("spamlog.20101222.bz2",'r');
sentinel=0;

for line in udata:
    sentinel += 1;
    if sentinel == 1:
        line1 = line;
    elif sentinel == 2:
        line2 = line;

#print line1;
#print line2;

#print "The total number of lines is ",sentinel;
udata.close();








