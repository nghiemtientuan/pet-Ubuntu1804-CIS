import subprocess, os, re

# 4 Logging and Auditing
# 4.1 Configure System Accounting (auditd)
# 4.1.1 Configure Data Retention
# 4.1.1.1 Ensure audit log storage size is configured

# 4.1.2 Ensure auditd service is enabled
def task_4_1_2(fixbug=False):
	check = os.popen("systemctl is-enabled auditd").read()

	if (check == 'enabled'):
		return True
	if(fixbug == True): fix_4_1_2()			
	return False

def fix_4_1_2():
	# check install
	os.popen("systemctl enable auditd")

# 4.1.3 Ensure auditing for processes that start prior to auditd is enabled
def task_4_1_3(fixbug=False):
	check = os.popen('grep "^\s*linux" /boot/grub/grub.cfg').read()

	if (re.search("audit=1", check)):
		return True
	if (fixbug == True): fix_4_1_3()
	return False

def fix_4_1_3():
	# Edit /etc/default/grub and add audit=1 to GRUB_CMDLINE_LINUX:
	os.popen("update-grub")

# 4.2 Configure Logging
# 4.2.1 Configure rsyslog
# 4.2.1.1 Ensure rsyslog Service is enabled
def task_4_2_1_1(fixbug=False):
	check = os.popen("systemctl is-enabled rsyslog").read()

	if (check == 'enabled'):
		return True
	if(fixbug == True): fix_4_2_1_1()			
	return False

def fix_4_2_1_1():
	#check install
	os.popen("systemctl enable rsyslog")

# 4.2.2 Configure syslog-ng
# 4.2.2.1 Ensure syslog-ng service is enabled
def task_4_2_2_2(fixbug=False):
	check = os.popen("systemctl is-enabled syslog-ng").read()

	if (check == 'enabled'):
		return True
	if(fixbug == True): fix_4_2_2_2()			
	return False

def fix_4_2_2_2():
	#check install
	os.popen("update-rc.d syslog-ng enable")

# 4.2.3 Ensure rsyslog or syslog-ng is installed
def task_4_2_3(fixbug=False):
	dpkg_rsyslog = os.popen("dpkg -s rsyslog").read()
	dpkg_syslog = os.popen("dpkg -s syslog-ng").read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg_rsyslog) and re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg_syslog)):
		return True
	if (fixbug == True): fix_4_2_3()
	return False

def fix_4_2_3():
	os.popen("apt-get install rsyslog -y")
	os.popen("apt-get install syslog-ng -y")