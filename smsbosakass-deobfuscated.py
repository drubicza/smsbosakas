#TERIMA KASIH TELAH MEMAKAI SCRIPT KAMI THANKS TO ALLAH SWT
#GUNAKANLAH SEBAIK MUNGKIN YA SAYANG...
#SUPPORT TO ME : MRTAMFANX CYBER TEAM
#CONTACT : Prakasa_Jr64

from requests import Session
import re, sys
s = Session()

try:
     print("║██████████╚╗        ╔══════╗╦    ╦╔══════╗╔══════╗")
     print("║██╔══╗█╔═╗█║        ║ ╔══╗ ║║    ║║ ╔══╗ ║║      ║")
     print("║██║╬╔╝█╚╗║█║        ║ ║  ║ ║║    ║║ ║  ║ ║║      ║")
     print("║██╚═╝█║█╚╝█║        ║ ╚══╝ ║║ ╔══╝║ ╚══╝ ║║")
     print("╚╗█████████═╝        ╠══════╣╠═╣   ╠══════╣╚══════╗")
     print(" ╚╗║╠╩╩╩╩╩╝          ║ ╔══╗ ║║ ╚══╗║ ╔══╗ ║       ║")
     print(" ║║┈┈┈█▐█████▒.｡oO   ║ ║  ║ ║║    ║║ ║  ║ ║║      ║ ╔═══╗╦  ╦")
     print(" ║██╠╦╦╦╗            ║ ║  ║ ║║    ║║ ║  ║ ║║      ║ ╠═══╗╚══╣")
     print(" ╚╗██████:           ╩ ╩  ╩ ╩╩    ╩╩ ╩  ╩ ╩╚══════╝ ╚═══╝   ╩")
     print("▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂")
     print(" MASUKIN NOMERNYA PAKAI 62 JANGAN PAKAI 0 YA SAYANGKU CINTAKU")
     print("     AUTHOR : PRAKASA _JR64 WHATSAPP : +62 857-7951-5200")
     print("   SUPPORT TO ME : MRTAMFANX CYBER TEAM  IG : Prakasa_Jr64\n")

     no = int(input("[ROOT@PRAKASA_JR64]MASUKAN NOMER KORBAN SAYANG=•> "))
     msg = input("[ROOT@PRAKASA_JR64]ISI PESANNYA SAYANG=•> ")
except:
	print("[ROOT@PRAKASA_JR64]MASUKIN NOMERNYA YANG BENER DONG NGENTOD...")
	sys.exit()

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
    'Referer': 'http://sms.payuterus.biz/alpha/'
}

bypass = s.get("http://sms.payuterus.biz/alpha/?a=keluar", headers=headers).text
key = re.findall(r'value="(\d+)"', bypass)[0]
jml = re.findall(r'<span>(.*?) = </span>', bypass)[0]
captcha = eval(jml.replace("x", "*").replace(":", "/"))

data = {
	'nohp':no,
	'pesan':msg,
	'captcha':captcha,
	'key':key
}

send = s.post("http://sms.payuterus.biz/alpha/send.php", headers=headers, data=data).text

if '[ROOT@PRAKASA_JR64]SMS TELAH DIKIRIM OLEH BOSS PRAKASA_JR64' in send:
	print(f"\n[ROOT@PRAKASA_JR64]PESAN TELAH MASUK [✓]\n  [ {no} : {msg} ]\n")
elif '[ROOT@PRAKASA_JR64]IM SORRY SIR/MIS' in send:
     print("\n[+]MOHON DI TUNGGU YA NGENTOD SABAR...\n")
else:
	print("\n[ROOT@PRAKASA_JR64]PENGIRIMAN SMS GAGAL BOS PRAKASA_JR64[-]\n")
