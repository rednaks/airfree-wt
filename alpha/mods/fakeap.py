from autoDeauth import sc
import re
import os



print 'Cleaning Mon interfaces'
sc.CleanMon()
print 'Scanning APs'
sc.Scan_APs()
f = open('res_scan.txt','r')

line = ' '
while line:
  line = re.sub('\n','',f.readline())
  BSSID = line
  line = re.sub('\n','',f.readline())
  channel = line
  line = re.sub('\n','',f.readline())
  essid = line
  line = f.readline()

f.close()
#os.remove('res_scan.txt')



print 'BSSID %s Channel %s ESSID %s' %(BSSID, channel, essid)
