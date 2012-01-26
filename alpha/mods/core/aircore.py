import sys,os
import time
import re



RES_FILE = '.res_scan.txt'
MON_INTF = '.mi.txt'
MYMACADD = '.mymcadd.txt'

# Clean All Mon interfaces:

def CleanMon():
  os.system('iwconfig | grep -i mon | cut --delimiter=" " -f1 > %s' % MON_INTF)
  fp = open(MON_INTF,'r')
  line= ' '
  while(line):
    line = fp.readline()
    interface = re.sub('\n','',line)
    if(line):
      os.system('airmon-ng stop %s' % interface)
  fp.close()
  os.remove(MON_INTF)


#Change Channel
def Change_Channel(Channel):
  os.system('ifconfig mon0 down')
  os.system('iwconfig mon0 channel '+Channel)
  os.system('ifconfig mon0 up')

#Get My MAC-ADD

def Get_MyMac():
	os.system('ifconfig wlan0 | grep -i hwaddr | cut --delimiter=r -f2- | cut --delimiter=r -f2 > %s' % MYMACADD)
	f = open(MYMACADD,'r')
	mac_add = re.sub(' ','',f.readline())
	f.close()
	os.remove(MYMACADD)
	return mac_add


def SetOnMon():
  os.system('airmon-ng start wlan0 -1')

def SetOffMon():
  os.system('airmon-ng stop mon0')
  
  
def Scan_APs():
  os.system('iwlist wlan0 scanning | egrep "\\bAddress\\b|\\bChannel\\b|\\bESSID\\b" | grep -v Frequency |cut -d: -f2- > %s' % RES_FILE)
  #os.system('iwlist wlan0 scanning | grep  -i address  -A 1 > res_scan.txt')
  fp = open(RES_FILE,'r')
  line = ' '
  info_list = []
  while line:
	tmp = []
	line = fp.readline()
	tmp.append(re.sub('\n','',line))
	line = fp.readline()
	tmp.append(re.sub('\n','',line))
	line = fp.readline()
	tmp.append(re.sub('\n','',line))
	info_list.append(tmp)
  os.remove(RES_FILE)
  return info_list[:len(info_list)-1]





#Exit Airfree-Wt
def ExitAir():
   print 'Thank you for using AirFree-WT\n'
   sys.exit(0)


def GetVersion():
   return '0.2'

def updateAir():
   #print '\nupdating AirFree-WT ...'
   print '\n Not Yet implemented !'
   time.sleep(1)

def affiche_menu(liste):
   i = 1
   for men in liste:
     print '\n [%d] %s' %(i,men)
     i += 1
