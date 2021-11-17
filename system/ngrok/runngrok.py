import os 

x = int(input("1 ngrok tcp 2 token ngrok : ")) 
if x == 1: 
   os.system ("cd /$HOME/msf/system/ngrok;python3 tcp.py")
elif x == 2:
   os.system ("cd /$HOME/msf/system/ngrok;python3 tokenngrok.py")

