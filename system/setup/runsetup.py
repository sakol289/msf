import os
os.system ("clear")
print('''\033[1;33;40m     
********************************
*                              *
*      1 setup ubuntu          *
*      2 setup kali linux      *
*      3 setup termux          *
*     00 exit                  *
*                              *
********************************
''')
x=int(input("1 setup ubuntu 2 setup kali linux 00 exit = "))
if x == 1:
    os.system ("clear")
    os.system ("cd /$HOME/msf/system;python3 progressbar.py")
    os.system ("clear")
    os.system ("cd /$HOME/msf/setup;bash setupubuntu.sh")
    ##bash setupubuntu.sh
    ##os.system ("python3 msf.py")
elif x == 2:
    os.system ("clear")
    os.system ("cd /$HOME/msf/system;python3 progressbar.py")
    os.system ("clear")
    os.system ("cd /$HOME/msf/setup;bash setupkalilinux.sh")
elif x == 3:
    os.system ("clear")
    os.system ("cd /$HOME/msf/system;python3 progressbar.py")
    os.system ("clear")
    os.system ("cd /$HOME/msf/setup;bash setuptermux.sh")
elif x == 0:
    os.system ("exit")
else:
        print ("vkg0 ld] Tkouiy9oN")
