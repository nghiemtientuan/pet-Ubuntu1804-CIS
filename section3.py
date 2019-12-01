import subprocess, os, re, sys
test_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(test_path)

import helper as helper

# 3 Network Configuration
# 3.1 Network Parameters (Host Only)
# 3.1.1 Ensure IP forwarding is disabled
def task_3_1_1(fixbug=False):
	check = os.popen('sysctl net.ipv4.ip_forward').read()
	check2 = os.popen('grep "net\.ipv4\.ip_forward" /etc/sysctl.conf /etc/sysctl.d/*').read()

	if (check == 'net.ipv4.ip_forward = 0' and re.search("net.ipv4.ip_forward = 0", check2)):
		return True
	if (fixbug == True): fix_3_1_1()
	return False

def fix_3_1_1():
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv4\.ip_forward', 'net.ipv4.ip_forward = 0')
	os.popen("sysctl -w net.ipv4.ip_forward=0")
	os.popen("sysctl -w net.ipv4.route.flush=1")

# 3.1.2 Ensure packet redirect sending is disabled
def task_3_1_2(fixbug=False):
	check = os.popen('sysctl net.ipv4.conf.all.send_redirects').read()
	check2 = os.popen('sysctl net.ipv4.conf.default.send_redirects').read()
	check3 = os.popen('grep "net\.ipv4\.conf\.all\.send_redirects" /etc/sysctl.conf/etc/sysctl.d/*').read()
	check4 = os.popen('grep "net\.ipv4\.conf\.default\.send_redirects" /etc/sysctl.conf/etc/sysctl.d/*').read()

	if (check == 'net.ipv4.conf.all.send_redirects = 0' and check2 == 'net.ipv4.conf.default.send_redirects = 0' and check3 == 'net.ipv4.conf.all.send_redirects = 0' and check4 == 'net.ipv4.conf.default.send_redirects = 0'):
		return True
	if (fixbug == True): fix_3_1_2()
	return False

def fix_3_1_2():
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv4\.conf\.all\.send_redirects', 'net.ipv4.conf.all.send_redirects = 0')
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv4\.conf\.default\.send_redirects', 'net.ipv4.conf.default.send_redirects = 0')
	os.popen("sysctl -w net.ipv4.conf.all.send_redirects=0")
	os.popen("sysctl -w net.ipv4.conf.default.send_redirects=0")
	os.popen("sysctl -w net.ipv4.route.flush=1")

# 3.2 Network Parameters
# 3.2.1 Ensure source routed packets are not accepted
def task_3_2_1(fixbug=False):
	check = os.popen('sysctl net.ipv4.conf.all.accept_source_route').read()
	check2 = os.popen('sysctl net.ipv4.conf.default.accept_source_route').read()
	check3 = os.popen('grep "net\.ipv4\.conf\.all\.accept_source_route" /etc/sysctl.conf/etc/sysctl.d/*').read()
	check4 = os.popen('grep "net\.ipv4\.conf\.default\.accept_source_route" /etc/sysctl.conf/etc/sysctl.d/*').read()

	if (check == 'net.ipv4.conf.all.accept_source_route = 0' and check2 == 'net.ipv4.conf.default.accept_source_route = 0' and check3 == 'net.ipv4.conf.all.accept_source_route = 0' and check4 == 'net.ipv4.conf.default.accept_source_route = 0'):
		return True
	if (fixbug == True): fix_3_2_1()
	return False

def fix_3_2_1():
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv4\.conf\.all\.accept_source_route', 'net.ipv4.conf.all.accept_source_route = 0')
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv4\.conf\.default\.accept_source_route', 'net.ipv4.conf.default.accept_source_route = 0')
	os.popen("sysctl -w net.ipv4.conf.all.accept_source_route=0")
	os.popen("sysctl -w net.ipv4.conf.default.accept_source_route=0")
	os.popen("sysctl -w net.ipv4.route.flush=1")

# 3.2.2 Ensure ICMP redirects are not accepted
def task_3_2_2(fixbug=False):
	check = os.popen('sysctl net.ipv4.conf.all.accept_redirects').read()
	check2 = os.popen('sysctl net.ipv4.conf.default.accept_redirects').read()
	check3 = os.popen('grep "net\.ipv4\.conf\.all\.accept_redirects" /etc/sysctl.conf/etc/sysctl.d/*').read()
	check4 = os.popen('grep "net\.ipv4\.conf\.default\.accept_redirects" /etc/sysctl.conf/etc/sysctl.d/*').read()

	if (check == 'net.ipv4.conf.all.accept_redirects = 0' and check2 == 'net.ipv4.conf.default.accept_redirects = 0' and check3 == 'net.ipv4.conf.all.accept_redirects = 0' and check4 == 'net.ipv4.conf.default.accept_redirects = 0'):
		return True
	if (fixbug == True): fix_3_2_2()
	return False

def fix_3_2_2():
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv4\.conf\.all\.accept_redirects', 'net.ipv4.conf.all.accept_redirects = 0')
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv4\.conf\.default\.accept_redirects', 'net.ipv4.conf.default.accept_redirects = 0')
	os.popen("sysctl -w net.ipv4.conf.all.accept_redirects=0")
	os.popen("sysctl -w net.ipv4.conf.default.accept_redirects=0")
	os.popen("sysctl -w net.ipv4.route.flush=1")

# 3.2.3 Ensure secure ICMP redirects are not accepted
def task_3_2_3(fixbug=False):
	check = os.popen('sysctl net.ipv4.conf.all.secure_redirects').read()
	check2 = os.popen('sysctl net.ipv4.conf.default.secure_redirects').read()
	check3 = os.popen('grep "net\.ipv4\.conf\.all\.secure_redirects" /etc/sysctl.conf/etc/sysctl.d/*').read()
	check4 = os.popen('grep "net\.ipv4\.conf\.default\.secure_redirects" /etc/sysctl.conf/etc/sysctl.d/*').read()

	if (check == 'net.ipv4.conf.all.secure_redirects = 0' and check2 == 'net.ipv4.conf.default.secure_redirects = 0' and check3 == 'net.ipv4.conf.all.secure_redirects = 0' and check4 == 'net.ipv4.conf.default.secure_redirects = 0'):
		return True
	if (fixbug == True): fix_3_2_3()
	return False

def fix_3_2_3():
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv4\.conf\.all\.secure_redirects', 'net.ipv4.conf.all.secure_redirects = 0')
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv4\.conf\.default\.secure_redirects', 'net.ipv4.conf.default.secure_redirects = 0')
	os.popen("sysctl -w net.ipv4.conf.all.secure_redirects=0")
	os.popen("sysctl -w net.ipv4.conf.default.secure_redirects=0")
	os.popen("sysctl -w net.ipv4.route.flush=1")

# 3.2.4 Ensure suspicious packets are logged
def task_3_2_4(fixbug=False):
	check = os.popen('sysctl net.ipv4.conf.all.log_martians').read()
	check2 = os.popen('sysctl net.ipv4.conf.default.log_martians').read()
	check3 = os.popen('grep "net\.ipv4\.conf\.all\.log_martians" /etc/sysctl.conf /etc/sysctl.d/*').read()
	check4 = os.popen('grep "net\.ipv4\.conf\.default\.log_martians" /etc/sysctl.conf/etc/sysctl.d/*').read()

	if (check == 'net.ipv4.conf.all.log_martians = 1' and check2 == 'net.ipv4.conf.default.log_martians = 1' and check3 == 'net.ipv4.conf.all.log_martians = 1' and check4 == 'net.ipv4.conf.default.log_martians = 1'):
		return True
	if (fixbug == True): fix_3_2_4()
	return False

def fix_3_2_4():
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv4\.conf\.all\.log_martians', 'net.ipv4.conf.all.log_martians = 1')
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv4\.conf\.default\.log_martians', 'net.ipv4.conf.default.log_martians = 1')
	os.popen("sysctl -w net.ipv4.conf.all.log_martians=1")
	os.popen("sysctl -w net.ipv4.conf.default.log_martians=1")
	os.popen("sysctl -w net.ipv4.route.flush=1")

# 3.2.5 Ensure broadcast ICMP requests are ignored
def task_3_2_5(fixbug=False):
	check = os.popen('sysctl net.ipv4.icmp_echo_ignore_broadcasts').read()
	check2 = os.popen('grep "net\.ipv4\.icmp_echo_ignore_broadcasts" /etc/sysctl.conf/etc/sysctl.d/*').read()

	if (check == 'net.ipv4.icmp_echo_ignore_broadcasts = 1' and check2 == 'net.ipv4.icmp_echo_ignore_broadcasts = 1'):
		return True
	if (fixbug == True): fix_3_2_5()
	return False

def fix_3_2_5():
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv4\.icmp_echo_ignore_broadcasts', 'net.ipv4.icmp_echo_ignore_broadcasts = 1')
	os.popen("sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=1")
	os.popen("sysctl -w net.ipv4.route.flush=1")

# 3.2.6 Ensure bogus ICMP responses are ignored
def task_3_2_6(fixbug=False):
	check = os.popen('sysctl net.ipv4.icmp_ignore_bogus_error_responses').read()
	check2 = os.popen('grep "net\.ipv4\.icmp_ignore_bogus_error_responses" /etc/sysctl.conf/etc/sysctl.d/*').read()

	if (check == 'net.ipv4.icmp_ignore_bogus_error_responses = 1' and check2 == 'net.ipv4.icmp_ignore_bogus_error_responses = 1'):
		return True
	if (fixbug == True): fix_3_2_6()
	return False

def fix_3_2_6():
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv4\.icmp_ignore_bogus_error_responses', 'net.ipv4.icmp_ignore_bogus_error_responses = 1')
	os.popen("sysctl -w net.ipv4.route.flush=1")

# 3.2.7 Ensure Reverse Path Filtering is enabled
def task_3_2_7(fixbug=False):
	check = os.popen('sysctl net.ipv4.conf.all.rp_filter').read()
	check2 = os.popen('sysctl net.ipv4.conf.default.rp_filter').read()
	check3 = os.popen('grep "net\.ipv4\.conf\.all\.rp_filter" /etc/sysctl.conf /etc/sysctl.d/*').read()
	check4 = os.popen('grep "net\.ipv4\.conf\.default\.rp_filter" /etc/sysctl.conf /etc/sysctl.d/*').read()

	if (check == 'net.ipv4.conf.all.rp_filter = 1' and check2 == 'net.ipv4.conf.default.rp_filter = 1' and check3 == 'net.ipv4.conf.all.rp_filter = 1' and check4 == 'net.ipv4.conf.default.rp_filter = 1'):
		return True
	if (fixbug == True): fix_3_2_7()
	return False

def fix_3_2_7():
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv4\.conf\.all\.rp_filter', 'net.ipv4.conf.all.rp_filter = 1')
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv4\.conf\.default\.rp_filter', 'net.ipv4.conf.default.rp_filter = 1')
	os.popen("sysctl -w net.ipv4.conf.all.rp_filter=1")
	os.popen("sysctl -w net.ipv4.conf.default.rp_filter=1")
	os.popen("sysctl -w net.ipv4.route.flush=1")

# 3.2.8 Ensure TCP SYN Cookies is enabled
def task_3_2_8(fixbug=False):
	check = os.popen('sysctl net.ipv4.tcp_syncookies').read()
	check = os.popen('grep "net\.ipv4\.tcp_syncookies" /etc/sysctl.conf /etc/sysctl.d/*').read()

	if (check == 'net.ipv4.tcp_syncookies = 1' and check2 == 'net.ipv4.tcp_syncookies = 1'):
		return True
	if (fixbug == True): fix_3_2_8()
	return False

def fix_3_2_8():
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv4\.tcp_syncookies', 'net.ipv4.tcp_syncookies = 1')
	os.popen("sysctl -w net.ipv4.tcp_syncookies=1")
	os.popen("sysctl -w net.ipv4.route.flush=1")

# 3.3 IPv6
# 3.3.1 Ensure IPv6 router advertisements are not accepted
def task_3_3_1(fixbug=False):
	check = os.popen('sysctl net.ipv6.conf.all.accept_ra').read()
	check2 = os.popen('sysctl net.ipv6.conf.default.accept_ra').read()
	check3 = os.popen('grep "net\.ipv6\.conf\.all\.accept_ra" /etc/sysctl.conf /etc/sysctl.d/*').read()
	check4 = os.popen('grep "net\.ipv6\.conf\.default\.accept_ra" /etc/sysctl.conf /etc/sysctl.d/*').read()

	if (check == 'net.ipv6.conf.all.accept_ra = 0' and check2 == 'net.ipv6.conf.default.accept_ra = 0' and check3 == 'net.ipv6.conf.all.accept_ra = 0' and check4 == 'net.ipv6.conf.default.accept_ra = 0'):
		return True
	if (fixbug == True): fix_3_3_1()
	return False

def fix_3_3_1():
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv6\.conf\.all\.accept_ra', 'net.ipv6.conf.all.accept_ra = 0')
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv6\.conf\.default\.accept_ra', 'net.ipv6.conf.default.accept_ra = 0')
	os.popen("sysctl -w net.ipv6.conf.all.accept_ra=0")
	os.popen("sysctl -w net.ipv6.conf.default.accept_ra=0")
	os.popen("sysctl -w net.ipv6.route.flush=1")

# 3.3.2 Ensure IPv6 redirects are not accepted
def task_3_3_2(fixbug=False):
	check = os.popen('sysctl net.ipv6.conf.all.accept_redirects').read()
	check2 = os.popen('sysctl net.ipv6.conf.default.accept_redirects').read()
	check3 = os.popen('grep "net\.ipv6\.conf\.all\.accept_redirect" /etc/sysctl.conf/etc/sysctl.d/*').read()
	check4 = os.popen('grep "net\.ipv6\.conf\.default\.accept_redirect" /etc/sysctl.conf/etc/sysctl.d/*').read()

	if (check == 'net.ipv6.conf.all.accept_redirect = 0' and check2 == 'net.ipv6.conf.default.accept_redirect = 0' and check3 == 'net.ipv6.conf.all.accept_redirect = 0' and check4 == 'net.ipv6.conf.default.accept_redirect = 0'):
		return True
	if (fixbug == True): fix_3_3_2()
	return False

def fix_3_3_2():
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv6\.conf\.all\.accept_redirect', 'net.ipv6.conf.all.accept_redirects = 0')
	helper.replaceLine('/etc/sysctl.conf', 'net\.ipv6\.conf\.default\.accept_redirect', 'net.ipv6.conf.default.accept_redirects = 0')
	os.popen("sysctl -w net.ipv6.conf.all.accept_redirects=0")
	os.popen("sysctl -w net.ipv6.conf.default.accept_redirects=0")
	os.popen("sysctl -w net.ipv6.route.flush=1")

# 3.3.3 Ensure IPv6 is disabled

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