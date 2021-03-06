from audcore import audc
import os
from core import aircore

print 'Cleaning Mon Interfaces ...'
aircore.CleanMon()
print 'Clean !'
print 'Scanning AccessPoints ...'
ap_list = aircore.Scan_APs()
my_mac = aircore.Get_MyMac()
#print ap_list
print 'Fineshed !'
print 'Set Monitor Mode On ...'
aircore.SetOnMon()
print 'Set !'

print 'Processing ...'

current_ch = '-1'

for elt in ap_list:
	audc.GetOut(elt[1],current_ch,elt[0],my_mac)
	current_ch = elt[1]
  
aircore.SetOffMon()
