import random as RR
import threading
from threading import Thread as TT
import os
import requests
from requests import post as P, get as G
try:
    from user_agent import generate_user_agent as AA
except:
    os.system('pip install user_agent')
    from user_agent import generate_user_agent as AA
    
F = '\033[1;32m'
Z = '\033[1;31m'  

def ProxyHttp():
    while True:
        ip = ".".join(str(RR.randint(0, 255)) for _ in range(4))
        pl = [19, 20, 21, 22, 23, 24, 25, 80, 53, 111, 110, 443, 8080, 139, 445, 512, 513, 514, 4444, 2049, 1524, 3306, 5900]
        port = RR.choice(pl)
        proxy = ip + ":" + str(port)
        try:
            req = G('https://www.google.com', headers={"User-Agent": AA()}, proxies={'http': proxy})
            if req.status_code == 200:
                print(f'{F}GOOD PROXY : {proxy}')
                with open('http_proxy.txt', 'a') as f:
                    f.write(proxy + "\n")
            else:
                print(f'{Z}BAD PROXY : {proxy}')
        except requests.RequestException as e:
            print(f'{Z}ERROR OCCURRED WITH PROXY : {proxy}')

def ProxySocks4():
    while True:
        ip = ".".join(str(RR.randint(0, 255)) for _ in range(4))
        pl = [19, 20, 21, 22, 23, 24, 25, 80, 53, 111, 110, 443, 8080, 139, 445, 512, 513, 514, 4444, 2049, 1524, 3306, 5900]
        port = RR.choice(pl)
        proxy = ip + ":" + str(port)
        try:
            req = G('https://www.google.com', headers={"User-Agent": AA()}, proxies= {'http': 'socks4://'+proxy})
            if req.status_code == 200:
                print(f'{F}GOOD SOCKS4 : {proxy}')
                with open('good_Socks4.txt', 'a') as f:
                    f.write(proxy + "\n")
            else:
                print(f'{Z}BAD SOCKS4 : {proxy}')
        except requests.RequestException as e:
            print(f'{Z}ERROR OCCURRED WITH PROXY : {proxy}')

def ProxySocks5():
    while True:
        ip = ".".join(str(RR.randint(0, 255)) for _ in range(4))
        pl = [19, 20, 21, 22, 23, 24, 25, 80, 53, 111, 110, 443, 8080, 139, 445, 512, 513, 514, 4444, 2049, 1524, 3306, 5900]
        port = RR.choice(pl)
        proxy = ip + ":" + str(port)
        try:
            req = G('https://www.google.com', headers={"User-Agent": AA()}, proxies= {'http': 'socks5://'+proxy})
            if req.status_code == 200:
                print(f'{F}GOOD SOCKS5 : {proxy}')
                with open('good_Socks5.txt', 'a') as f:
                    f.write(proxy + "\n")
            else:
                print(f'{Z}BAD SOCKS5 : {proxy}')
        except requests.RequestException as e:
            print(f'{Z}ERROR OCCURRED WITH PROXY : {proxy}')

Threads = []
for _ in range(100):
    t_http = TT(target=ProxyHttp)
    t_http.start()
    Threads.append(t_http)

    t_socks4 = TT(target=ProxySocks4)
    t_socks4.start()
    Threads.append(t_socks4)

    t_socks5 = TT(target=ProxySocks5)
    t_socks5.start()
    Threads.append(t_socks5)

for thread in Threads:
    thread.join()