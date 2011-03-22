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

#print "The total number of lines is ",sentinel1 ," And the number of smtpfilter lines is ",sentinel2;

udata.close();
#def get_id(line):
#On each line get the servernaem and the smtpfilter id, the 4th and 5th Column
#We need to create a hash where these unique identifier can be stored.
#Once that is done store them on the hash and for each new one check the hash so 
#we don't store any duplicates. This will give us the total emails check on all the
#sys_spam hosts.
#matchObj = re.match(r'       







