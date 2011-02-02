#!/usr/bin/env python
import bz2;
import re;

udata = bz2.BZ2File("spamlog.20101222.bz2",'r');
sentinel1=0;
sentinel2=0;

for line in udata:
    sentinel1 += 1;
    if re.search('smtpfilter',line):
        sentinel2 += 1;
        if sentinel2 == 1:
            line1 = line;
        elif sentinel2 == 2:
            line2 = line;

#print line1;
#print line2;

print "The total number of lines is ",sentinel1 ," And the number of smtpfilter lines is ",sentinel2;

udata.close();








