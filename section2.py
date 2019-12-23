import subprocess, os, re, sys
test_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(test_path)

import helper as helper

# 2 Services
# 2.1 inetd Services
# 2.1.1 Ensure chargen services are not enabled
def task_2_1_1(fixbug=False):
	grep = os.popen('grep -R "^chargen" /etc/xinetd.*').read()

	if (grep == '' and helper.checkDisableServiceInFolder('/etc/xinetd.d', 'chargen')):
		return True
	if (fixbug == True): fix_2_1_1()
	return False

def fix_2_1_1():
	helper.disableServiceInFolder('/etc/xinetd.d', 'chargen')

# 2.1.2 Ensure daytime services are not enabled
def task_2_1_2(fixbug=False):
	grep = os.popen('grep -R "^daytime" /etc/xinetd.*').read()

	if (grep == '' and helper.checkDisableServiceInFolder('/etc/xinetd.d', 'daytime')):
		return True
	if (fixbug == True): fix_2_1_2()
	return False

def fix_2_1_2():
	helper.disableServiceInFolder('/etc/xinetd.d', 'daytime')

# 2.1.3 Ensure discard services are not enabled
def task_2_1_3(fixbug=False):
	grep = os.popen('grep -R "^discard" /etc/xinetd.*').read()

	if (grep == '' and helper.checkDisableServiceInFolder('/etc/xinetd.d', 'discard')):
		return True
	if (fixbug == True): fix_2_1_3()
	return False

def fix_2_1_3():
	helper.disableServiceInFolder('/etc/xinetd.d', 'discard')

# 2.1.4 Ensure echo services are not enabled
def task_2_1_4(fixbug=False):
	grep = os.popen('grep -R "^echo" /etc/xinetd.*').read()

	if (grep == '' and helper.checkDisableServiceInFolder('/etc/xinetd.d', 'echo')):
		return True
	if (fixbug == True): fix_2_1_4()
	return False

def fix_2_1_4():
	helper.disableServiceInFolder('/etc/xinetd.d', 'echo')

# 2.1.5 Ensure time services are not enabled
def task_2_1_5(fixbug=False):
	grep = os.popen('grep -R "^time" /etc/xinetd.*').read()

	if (grep == '' and helper.checkDisableServiceInFolder('/etc/xinetd.d', 'time')):
		return True
	if (fixbug == True): fix_2_1_5()
	return False

def fix_2_1_5():
	helper.disableServiceInFolder('/etc/xinetd.d', 'time')

# 2.1.6 Ensure rsh server is not enabled
def task_2_1_6(fixbug=False):
	grep = os.popen('grep -R "^shell" /etc/xinetd.*').read()
	grep2 = os.popen('grep -R "^login" /etc/xinetd.*').read()
	grep3 = os.popen('grep -R "^exec" /etc/xinetd.*').read()

	if (grep == '' and grep2 =='' and grep3 =='' and helper.checkDisableServiceInFolder('/etc/xinetd.d', 'rsh') and helper.checkDisableServiceInFolder('/etc/xinetd.d', 'rlogin') and helper.checkDisableServiceInFolder('/etc/xinetd.d', 'rexec')):
		return True
	if (fixbug == True): fix_2_1_6()
	return False

def fix_2_1_6():
	helper.disableServiceInFolder('/etc/xinetd.d', 'rsh')
	helper.disableServiceInFolder('/etc/xinetd.d', 'rlogin')
	helper.disableServiceInFolder('/etc/xinetd.d', 'rexec')

# 2.1.7 Ensure talk server is not enabled
def task_2_1_7(fixbug=False):
	grep = os.popen('grep -R "^talk" /etc/xinetd.*').read()
	grep2 = os.popen('grep -R "^ntalk" /etc/xinetd.*').read()

	if (grep == '' and grep2 == '' and helper.checkDisableServiceInFolder('/etc/xinetd.d', 'talk')):
		return True
	if (fixbug == True): fix_2_1_7()
	return False

def fix_2_1_7():
	helper.disableServiceInFolder('/etc/xinetd.d', 'talk')

# 2.1.8 Ensure telnet server is not enabled
def task_2_1_8(fixbug=False):
	grep = os.popen('grep -R "^telnet" /etc/xinetd.*').read()

	if (grep == '' and helper.checkDisableServiceInFolder('/etc/xinetd.d', 'telnet')):
		return True
	if (fixbug == True): fix_2_1_8()
	return False

def fix_2_1_8():
	helper.disableServiceInFolder('/etc/xinetd.d', 'telnet')

# 2.1.9 Ensure tftp server is not enabled
def task_2_1_9(fixbug=False):
	grep = os.popen('grep -R "^tftp" /etc/xinetd.*').read()

	if (grep == '' and helper.checkDisableServiceInFolder('/etc/xinetd.d', 'tftp')):
		return True
	if (fixbug == True): fix_2_1_9()
	return False

def fix_2_1_9():
	helper.disableServiceInFolder('/etc/xinetd.d', 'tftp')

# 2.1.10 Ensure xinetd is not enabled
def task_2_1_10(fixbug=False):
	check = os.popen('systemctl is-enabled xinetd').read()

	if (check == 'disabled'):
		return True
	if (fixbug == True): fix_2_1_10()
	return False

def fix_2_1_10():
	os.popen("systemctl disable xinetd")

# 2.1.11 Ensure openbsd-inetd is not installed
def task_2_1_11(fixbug=False):
	dpkg_openbsd = os.popen("dpkg -s openbsd-inetd").read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg_openbsd)):
		if (fixbug == True): fix_2_1_11()
		return False
	return True

def fix_2_1_11():
	os.popen("apt-get remove openbsd-inetd -y")

# 2.2 Special Purpose Services
# 2.2.1 Time Synchronization
# 2.2.1.1 Ensure time synchronization is in use
def task_2_2_1_1(fixbug=False):
	dpkg_ntp = os.popen("dpkg -s ntp").read()
	dpkg_chrony = os.popen("dpkg -s chrony").read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg_ntp) or re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg_chrony)):
		return True
	if (fixbug == True): fix_2_2_1_1()
	return False

def fix_2_2_1_1():
	os.popen("apt-get install chrony -y")

def check_install_ntp():
	dpkg_ntp = os.popen("dpkg -s ntp").read()
	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg_ntp)):
		return True
	return False

def check_install_chrony():
	dpkg_chrony = os.popen("dpkg -s chrony").read()
	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg_chrony)):
		return True
	return False

# 2.2.1.2 Ensure ntp is configured
def task_2_2_1_2(fixbug=False):
	if (check_install_ntp()):
		check = os.popen('grep "^restrict" /etc/ntp.conf').read()
		check_egrep = os.popen('egrep "^(server|pool)" /etc/ntp.conf').read()
		check_grep = os.popen('grep "RUNASUSER=ntp" /etc/init.d/ntp').read()

		if (re.search("restrict -4 default kod nomodify notrap nopeer noquery", check) and re.search("restrict -6 default kod nomodify notrap nopeer noquery", check) and re.search("RUNASUSER=ntp", check_grep) and not (check_egrep == '')):
			return True
		if (fixbug == True): fix_2_2_1_2()
		return False
	return True

def fix_2_2_1_2():
	helper.replaceLine('/etc/ntp.conf', '^restrict -4', 'restrict -4 default kod nomodify notrap nopeer noquery')
	helper.replaceLine('/etc/ntp.conf', '^restrict -6', 'restrict -6 default kod nomodify notrap nopeer noquery')
	helper.replaceLine('/etc/init.d/ntp', 'RUNASUSER=', 'RUNASUSER=ntp')

	check_egrep = os.popen('egrep "^(server|pool)" /etc/ntp.conf').read()
	if (check_egrep == ''):
		with open('/etc/ntp.conf', 'a+') as file:
			file.writelines('\npool 0.ubuntu.pool.ntp.org iburst')
			file.writelines('\npool 1.ubuntu.pool.ntp.org iburst')
			file.writelines('\npool 2.ubuntu.pool.ntp.org iburst')
			file.writelines('\npool 3.ubuntu.pool.ntp.org iburst')
			file.writelines('\npool ntp.ubuntu.com')

# 2.2.1.3 Ensure chrony is configured
def task_2_2_1_3(fixbug=False):
	if (check_install_chrony()):
		check_grep = os.popen('grep "^(server|pool)" /etc/chrony/chrony.conf').read()

		if (not (check_grep == '')):
			return True
		if (fixbug == True): fix_2_2_1_3()

		return False

	return True

def fix_2_2_1_3():
	with open('/etc/chrony/chrony.conf', 'a+') as file:
		file.writelines('\npool 0.ubuntu.pool.ntp.org iburst')
		file.writelines('\npool 1.ubuntu.pool.ntp.org iburst')
		file.writelines('\npool 2.ubuntu.pool.ntp.org iburst')
		file.writelines('\npool 3.ubuntu.pool.ntp.org iburst')
		file.writelines('\npool ntp.ubuntu.com')

# 2.2.2 Ensure X Window System is not installed
def task_2_2_2(fixbug=False):
	dpkg_xserver = os.popen("dpkg -l xserver-xorg*").read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg_xserver)):
		if (fixbug == True): fix_2_2_2()
		return False
	return True

def fix_2_2_2():
	os.popen("apt-get remove xserver-xorg* -y")

# 2.2.3 Ensure Avahi Server is not enabled
def task_2_2_3(fixbug=False):
	check = os.popen("systemctl is-enabled avahi-daemon").read()

	if (not re.search("enabled", check)):
		return True
	if (fixbug == True): fix_2_2_3()
	return False

def fix_2_2_3():
	os.popen("systemctl disable avahi-daemon")

# 2.2.4 Ensure CUPS is not enabled
def task_2_2_4(fixbug=False):
	check = os.popen("systemctl is-enabled cups").read()

	if (not re.search("enabled", check)):
		return True
	if (fixbug == True): fix_2_2_4()
	return False

def fix_2_2_4():
	os.popen("systemctl disable cups")

# 2.2.5 Ensure DHCP Server is not enabled
def task_2_2_5(fixbug=False):
	check_server = os.popen("systemctl is-enabled isc-dhcp-server").read()
	check_server6 = os.popen("systemctl is-enabled isc-dhcp-server6").read()

	if (not re.search("enabled", check_server) and not re.search("enabled", check_server6)):
		return True
	if (fixbug == True): fix_2_2_5()
	return False

def fix_2_2_5():
	os.popen("systemctl disable isc-dhcp-server")
	os.popen("systemctl disable isc-dhcp-server6")

# 2.2.6 Ensure LDAP server is not enabled
def task_2_2_6(fixbug=False):
	check = os.popen("systemctl is-enabled slapd").read()

	if (not re.search("enabled", check)):
		return True
	if (fixbug == True): fix_2_2_6()
	return False

def fix_2_2_6():
	os.popen("systemctl disable slapd")

# 2.2.7 Ensure NFS and RPC are not enabled
def task_2_2_7(fixbug=False):
	check_server = os.popen("systemctl is-enabled nfs-server").read()
	check_rpcbind = os.popen("systemctl is-enabled rpcbind").read()

	if (not re.search("enabled", check_server) and not re.search("enabled", check_rpcbind)):
		return True
	if (fixbug == True): fix_2_2_7()
	return False

def fix_2_2_7():
	os.popen("systemctl disable nfs-server")
	os.popen("systemctl disable rpcbind")

# 2.2.8 Ensure DNS Server is not enabled
def task_2_2_8(fixbug=False):
	check = os.popen("systemctl is-enabled bind9").read()

	if (not re.search("enabled", check)):
		return True
	if (fixbug == True): fix_2_2_8()
	return False

def fix_2_2_8():
	os.popen("systemctl disable bind9")

# 2.2.9 Ensure FTP Server is not enabled
def task_2_2_9(fixbug=False):
	check = os.popen("systemctl is-enabled vsftpd").read()

	if (not re.search("enabled", check)):
		return True
	if (fixbug == True): fix_2_2_9()
	return False

def fix_2_2_9():
	os.popen("systemctl disable vsftpd")

# 2.2.10 Ensure HTTP server is not enabled
def task_2_2_10(fixbug=False):
	check = os.popen("systemctl is-enabled apache2").read()

	if (not re.search("enabled", check)):
		return True
	if (fixbug == True): fix_2_2_10()
	return False

def fix_2_2_10():
	os.popen("systemctl disable apache2")

# 2.2.11 Ensure IMAP and POP3 server is not enabled
def task_2_2_11(fixbug=False):
	check = os.popen("systemctl is-enabled dovecot").read()

	if (not re.search("enabled", check)):
		return True
	if (fixbug == True): fix_2_2_11()
	return False

def fix_2_2_11():
	os.popen("systemctl disable dovecot")

# 2.2.12 Ensure Samba is not enabled
def task_2_2_12(fixbug=False):
	check = os.popen("systemctl is-enabled smbd").read()

	if (not re.search("enabled", check)):
		return True
	if (fixbug == True): fix_2_2_12()
	return False

def fix_2_2_12():
	os.popen("systemctl disable smbd")

# 2.2.13 Ensure HTTP Proxy Server is not enabled
def task_2_2_13(fixbug=False):
	check = os.popen("systemctl is-enabled squid").read()

	if (not re.search("enabled", check)):
		return True
	if (fixbug == True): fix_2_2_13()
	return False

def fix_2_2_13():
	os.popen("systemctl disable squid")

# 2.2.14 Ensure SNMP Server is not enabled
def task_2_2_14(fixbug=False):
	check = os.popen("systemctl is-enabled snmpd").read()

	if (not re.search("enabled", check)):
		return True
	if (fixbug == True): fix_2_2_14()
	return False

def fix_2_2_14():
	os.popen("systemctl disable snmpd")

# 2.2.15 Ensure mail transfer agent is configured for local-only mode
def task_2_2_15(fixbug=False):
	netstat = subprocess.Popen('netstat -an | grep LIST | grep ":25[[:space:]]"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	for line in netstat.stdout.readlines():
		listString = line.split(' ')
		for string in listString:
			if (re.search(":25", string) and (string != '127.0.0.1:25' and string != '::1:25')):
				if (fixbug == True): fix_2_2_15()

				return False

	return True

def fix_2_2_15():
	helper.replaceLine('/etc/postfix/main.cf', 'inet_interfaces', 'inet_interfaces = loopback-only')
	os.popen("systemctl restart postfix")

# 2.2.16 Ensure rsync service is not enabled
def task_2_2_16(fixbug=False):
	check = os.popen("systemctl is-enabled rsync").read()

	if (not re.search("enabled", check)):
		return True
	if (fixbug == True): fix_2_2_16()
	return False

def fix_2_2_16():
	os.popen("systemctl disable rsync")

# 2.2.17 Ensure NIS Server is not enabled
def task_2_2_17(fixbug=False):
	check = os.popen("systemctl is-enabled nis").read()

	if (not re.search("enabled", check)):
		return True
	if (fixbug == True): fix_2_2_17()
	return False

def fix_2_2_17():
	os.popen("systemctl disable nis")

# 2.3 Service Clients
# 2.3.1 Ensure NIS Client is not installed
def task_2_3_1(fixbug=False):
	dpkg = os.popen("dpkg -s nis").read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg)):
		if (fixbug == True): fix_2_3_1()
		return False
	return True

def fix_2_3_1():
	os.popen("apt-get remove nis -y")

# 2.3.2 Ensure rsh client is not installed
def task_2_3_2(fixbug=False):
	dpkg = os.popen("dpkg -s rsh-client").read()
	dpkg2 = os.popen("dpkg -s rsh-redone-client").read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg) or re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg2)):
		if (fixbug == True): fix_2_3_2()
		return False
	return True

def fix_2_3_2():
	os.popen("apt-get remove rsh-client rsh-redone-client -y")

# 2.3.3 Ensure talk client is not installed
def task_2_3_3(fixbug=False):
	dpkg = os.popen("dpkg -s talk").read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg)):
		if (fixbug == True): fix_2_3_3()
		return False
	return True

def fix_2_3_3():
	os.popen("apt-get remove talk -y")

# 2.3.4 Ensure telnet client is not installed
def task_2_3_4(fixbug=False):
	dpkg = os.popen("dpkg -s telnet").read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg)):
		if (fixbug == True): fix_2_3_4()
		return False
	return True

def fix_2_3_4():
	os.popen("apt-get remove telnet -y")

# 2.3.5 Ensure LDAP client is not installed
def task_2_3_5(fixbug=False):
	dpkg = os.popen("dpkg -s ldap-utils").read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg)):
		if (fixbug == True): fix_2_3_5()
		return False
	return True

def fix_2_3_5():
	os.popen("apt-get remove ldap-utils -y")