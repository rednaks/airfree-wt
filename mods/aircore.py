import sys
import time

def ExitAir():
   print 'Thank you for using AirFree-WT\n'
   sys.exit(0)

def GetVersion():
   return 'alpha'

def updateAir():
   #print '\nupdating AirFree-WT ...'
   print '\n Not Yet implemented !'
   time.sleep(1)

def affiche_menu(liste):
   i = 1
   for men in liste:
     print '\n [%d] %s' %(i,men)
     i += 1
