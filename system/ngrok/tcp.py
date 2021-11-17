import os
x = input ("input port tcp : ")
os.system ("./ngrok tcp %s" % (x))
