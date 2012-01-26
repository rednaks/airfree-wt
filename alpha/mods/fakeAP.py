from audcore import audc
from core import aircore
import os



print 'cleaning mon ...'
aircore.CleanMon()

print 'Scanning APs ...\n'
liste = aircore.Scan_APs()

aircore.SetOnMon()

while 1:
    i = 0
    print '            BSSID         Channel         ESSID'
    for elt in liste:
        i+=1
        print '*[%d] %s      %s        %s' %(i,elt[0],elt[1],elt[2])
    print '\n[99] To exit'
    print 'Choose the one u want "clone"'
    choix = raw_input('air> ')
    #print len(liste)
    print type(int(choix))
    print int(choix)<=len(liste)
    print choix> 0
    print choix <= len(liste) and choix > 0
    if(int(choix)<=len(liste) and int(choix) > 0):
        os.system('airbase-ng -c %s -e %s mon0' %(liste[int(choix)-1][1],liste[int(choix)-1][2]))
    if (choix == '99' or choix == 'quit' or choix == 'exit'):
        break


aircore.SetOffMon()
