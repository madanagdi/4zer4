#!/usr/bin/env python3
import threading
import requests
import time 
from requests.exceptions import HTTPError
from colorama import init ,Fore, Back, Style
from colorama.ansi import Fore
import requests
import time 
from requests.exceptions import HTTPError
from io import open_code
import os 
import colorama
from colorama import init , Fore 
from termcolor import colored
import logging
import time
init()





def url_001():
    with open(path,encoding="ISO-8859-1") as newfile:

        url=[]
        for x in newfile:
            xx= ("https://"+str(x[:-1]))
            url.append(xx)
    return url  



def call_ing():
    
    F_F=[]
    Two_100=[]


    for link in url_001():
        
            try:
                r = requests.get(link)
                
                a = str(r)
                
                
                if a == "<Response [404]>":
                    print(Fore.BLUE , link)
                    F_F.append(link)

                elif a == "<Response [200]>":
                    print(Fore.GREEN , link)
                    
                    os.system("echo {} >>200.txt".format(link))
                else:
                    pass

            except:
                pass
    return F_F



def fof():
        
    file404=[]

    for x in call_ing(): 

        print(Fore.RED, x)

        dig=os.system(Fore.GREEN," dig {}".format(x))
        
        ns=os.system(Fore.YELLOW," nslookup {}".format(x))
        
        host=os.system(Back.RED,"host {}".format(x))

        file404.append(dig,ns,host)
    
 
if __name__ == '__main__':

    title="NIGO MADE THIS "

    for l in title:
        print(Fore.RED,l,end="")
        time.sleep(.1)



    print(Fore.BLUE , "Blue SubDomain = 200" , Fore.GREEN , "Green  SubDomain = 404")

    try: 
        path = input("Enter Filename contains subdomains : ")  # path to the url list file
    except:
        print("enter correct file name")

    fof()