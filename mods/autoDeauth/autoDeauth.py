import sc
import re
import os


print 'Cleaning Mon Interfaces ...'
sc.CleanMon()
print 'Clean !'
print 'Scanning AccessPoints ...'
sc.Scan_APs()
print 'Fineshed !'
print 'Set Monitor Mode On ...'
sc.SetOnMon()
print 'Set !'

print 'Processing ...'
f = open('res_scan.txt','r')

line = ' '
current_ch = '-1'

while(line):
  line = f.readline()
  bssid = re.sub('\n','',line)
  line = f.readline()
  sc.GetOut(re.sub('\n','',line),current_ch,bssid)
  current_ch = re.sub('\n','',line)
  
  line = f.readline()  
  
sc.SetOffMon()
f.close()
os.remove('res_scan.txt')
