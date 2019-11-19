import subprocess, os, re

# 3 Network Configuration
# 3.1 Network Parameters (Host Only)
# 3.1.1 Ensure IP forwarding is disabled
def task_3_1_1(fixbug=False):
	check = os.popen('sysctl net.ipv4.ip_forward').read()
	check2 = os.popen('grep "net\.ipv4\.ip_forward" /etc/sysctl.conf /etc/sysctl.d/*').read()

	if (check == 'net.ipv4.ip_forward[\s]+=[\s]+0' and re.search("net.ipv4.ip_forward[\s]+=[\s]+0", check2)):
		return True
	if (fixbug == True): fix_3_1_1()
	return False

def fix_3_1_1():
	# Set the following parameter in /etc/sysctl.conf or a /etc/sysctl.d/* file:
	os.popen("sysctl -w net.ipv4.ip_forward=0")
	os.popen("sysctl -w net.ipv4.route.flush=1")

# 3.4 TCP Wrappers
# 3.4.1 Ensure TCP Wrappers is installed
def task_3_4_1(fixbug=False):
	dpkg = os.popen("dpkg -s tcpd").read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg)):
		return True
	if (fixbug == True): fix_3_4_1()
	return False

def fix_3_4_1():
	os.popen("apt-get install tcpd -y")

# 3.4.2 Ensure /etc/hosts.allow is configured
def task_3_4_2(fixbug=False):
	check = os.popen("cat /etc/hosts.allow").read()

	if (check == ''):
		if (fixbug == True): fix_3_4_2()
		return False
	return True

def fix_3_4_2():
	os.popen('echo "ALL: 192.168.1.0/255.255.255.0" >/etc/hosts.allow')

# 3.4.3 Ensure /etc/hosts.deny is configured
def task_3_4_3(fixbug=False):
	dpkg = os.popen("cat /etc/hosts.deny").read()

	if (re.search("[^a-zA-Z0-9#]ALL: ALL", dpkg)):
		return True
	if (fixbug == True): fix_3_4_3()
	return False

def fix_3_4_3():
	os.popen('echo "ALL: ALL" >> /etc/hosts.deny')

# 3.4.4 Ensure permissions on /etc/hosts.allow are configured
def task_3_4_4(fixbug=False):
	stat = os.popen('stat /etc/hosts.allow').read()

	if (re.search("Access:[\s]+\(0644/-rw-r--r--\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat)):
		return True
	if (fixbug == True): fix_3_4_4()
	return False

def fix_3_4_4():
	os.popen("chown root:root /etc/hosts.allow")
	os.popen("chmod 644 /etc/hosts.allow")

# 3.4.5 Ensure permissions on /etc/hosts.deny are configured
def task_3_4_5(fixbug=False):
	stat = os.popen('stat /etc/hosts.deny').read()

	if (re.search("Access:[\s]+\(0644/-rw-r--r--\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat)):
		return True
	if (fixbug == True): fix_3_4_5()
	return False

def fix_3_4_5():
	os.popen("chown root:root /etc/hosts.deny")
	os.popen("chmod 644 /etc/hosts.deny")

# 3.5 Uncommon Network Protocols
# 3.5.1 Ensure DCCP is disabled
def task_3_5_1(fixbug=False):
	check = os.popen('modprobe -n -v dccp').read()
	check2 = os.popen('lsmod | grep dccp').read()

	if (re.search("install[a-zA-Z\s]+/bin/true", check2) and check2 == ''):
		return True
	if (fixbug == True): fix_3_5_1()
	return False

def fix_3_5_1():
	with open('/etc/modprobe.d/dccp.conf', 'a+') as file:
		file.write('install dccp /bin/true')

# 3.5.2 Ensure SCTP is disabled
def task_3_5_2(fixbug=False):
	check = os.popen('modprobe -n -v sctp').read()
	check2 = os.popen('lsmod | grep sctp').read()

	if (re.search("install[a-zA-Z\s]+/bin/true", check2) and check2 == ''):
		return True
	if (fixbug == True): fix_3_5_2()
	return False

def fix_3_5_2():
	with open('/etc/modprobe.d/sctp.conf', 'a+') as file:
		file.write('install sctp /bin/true')

# 3.5.3 Ensure RDS is disabled
def task_3_5_3(fixbug=False):
	check = os.popen('modprobe -n -v rds').read()
	check2 = os.popen('lsmod | grep rds').read()

	if (re.search("install[a-zA-Z\s]+/bin/true", check2) and check2 == ''):
		return True
	if (fixbug == True): fix_3_5_3()
	return False

def fix_3_5_3():
	with open('/etc/modprobe.d/rds.conf', 'a+') as file:
		file.write('install rds /bin/true')

# 3.5.4 Ensure TIPC is disabled
def task_3_5_4(fixbug=False):
	check = os.popen('modprobe -n -v tipc').read()
	check2 = os.popen('lsmod | grep tipc').read()

	if (re.search("install[a-zA-Z\s]+/bin/true", check2) and check2 == ''):
		return True
	if (fixbug == True): fix_3_5_4()
	return False

def fix_3_5_4():
	with open('/etc/modprobe.d/tipc.conf', 'a+') as file:
		file.write('install tipc /bin/true')

# 3.6 Firewall Configuration
# 3.6.1 Ensure iptables is installed
def task_3_6_1(fixbug=False):
	dpkg = os.popen("dpkg -s iptables").read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg)):
		return True
	if (fixbug == True): fix_3_6_1()
	return False

def fix_3_6_1():
	os.popen("apt-get install iptables -y")

# 3.6.2 Ensure default deny firewall policy
def task_3_6_2(fixbug=False):
	check = os.popen('iptables -L').read()

	if (re.search("Chain INPUT (policy DROP)", check) and re.search("Chain FORWARD (policy DROP)", check) and re.search("Chain OUTPUT (policy DROP)", check)):
		return True
	if (fixbug == True): fix_3_6_2()
	return False

def fix_3_6_2():
	os.popen("iptables -P INPUT DROP")
	os.popen("iptables -P OUTPUT DROP")
	os.popen("iptables -P FORWARD DROP")

# 3.6.3 Ensure loopback traffic is configured