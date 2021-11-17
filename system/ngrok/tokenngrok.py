import os
x = input ("token ngrok : ")
os.system ("./ngrok authtoken %s" % (x))
