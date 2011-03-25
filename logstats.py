#!/usr/bin/env python
import bz2;
import re;

def get_id(line):
#On each line get the servernaem and the smtpfilter id, the 4th and 5th Column
#We need to create a hash where these unique identifier can be stored.
#Once that is done store them on the hash and for each new one check the hash so 
#we don't store any duplicates. This will give us the total emails check on all the
#sys_spam hosts.
    matchObj = re.match(r'.*(\b\w+\-spam\b) (smtpfilter\[\d+\]).*',line);
    email_id = '';
    if matchObj:
#        print "It matched";
#        print "host > ",matchObj.group(1), " and id ",matchObj.group(2); 
        server_name = matchObj.group(1);
        proc_id = matchObj.group(2);
        email_id = server_name + proc_id;
        insert_id(email_id);
#        insert_id(server_name+prc_id);
#        email_id += matchObj.group(1);
#        email_id += matchObj.group(2);
#        insert_id(email_id);
#        print "email id >", email_id;
#        email_id += matchObj.group(1);
#        email_id += matchObj.group(2);
#        print "Potential id >",matchObj.group(1) += matchObj.group(2);
    else:
        print "Sorry no matched";
#matchObj = re.match(r'       
def insert_id(email_id):
    if not email_id in email_list:
        email_list.append(email_id);

udata = bz2.BZ2File("spamlog.20101222.bz2",'r');
sentinel1=0;
sentinel2=0;

email_list = [];
email_idPattern = re.compile(r'.*(\b\w+\-spam\b) (smtpfilter\[\d+\]).*');
for line in udata:
    sentinel1 += 1;
    if email_idPattern.match(line):
#        email_idPattern.groups
#    if re.match(r'.*(\b\w+\-spam\b) (smtpfilter\[\d+\]).*',line).groups():
#    if re.search('smtpfilter',line):
        sentinel2 += 1;
#        servername = email_idPattern.group(1) + email_idPattern.group(2);
#        email_server = 
#        get_id(line);
#        sentinel2 += 1;
#        if sentinel2 == 1:
#            line1 = line;
#        elif sentinel2 == 2:
#            line2 = line;

#print line1;
#print line2;
udata.close();
#print "The total number of lines is ",sentinel1 ," And the number of smtpfilter lines is ",sentinel2;

print "Total lines on file:> ",sentinel1;
print "Total lines related with unique smtpfilter is:> ",sentinel2;
#print "Total email scanned by smtpfilter:> ",len(email_list);





