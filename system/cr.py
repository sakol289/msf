import os ,sys
import time
from time import sleep

def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0/90)

os.system("clear")
semut=('''\033[0;32m
╦═╗ ╦╦ ╦╔═╗╔═╗╦╔═╦ ╦╔═╗╦ ╦
╠╦╝ ║╠═╣╠═╣║  ╠╩╗╚╦╝║ ║║ ║
╩╚═╚╝╩ ╩╩ ╩╚═╝╩ ╩ ╩ ╚═╝╚═╝ o
=================================
Project จัดทำโดย Sakol Thaneerat ทำเพื่อเป็น Tool ในการใช่ metasploit ได้ง่ายขึ้น ได้ดัดเเปลง tool มาจาก apt 47 เเละปรึกษา การทำ project นี้ คือ พี่ หมิ่ง พี่ ปาร์ค พี่ น้ำ พี่ เวียร์ ฯลฯ
''')
xr=("________________________________________________________")

slowprints(semut)
slowprints(xr)

input('\nPress enter to continue...:')
os.system("python3 $HOME/msf/run.py")
'''
g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
c = "\033[0m"
p = "\033[37;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
a = "\033[30;1m"

W = "\x1b[0m"
R = "\x1b[31m"
G = "\x1b[1;32m"
O = "\x1b[33m"
B = "\x1b[34m"
P = "\x1b[35m"
C = "\x1b[36m"
GR = "\x1b[37m"
'''
