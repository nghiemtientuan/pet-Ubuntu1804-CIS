import subprocess, os, re
test_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(test_path)

import helper as helper

# 4 Logging and Auditing
# 4.1 Configure System Accounting (auditd)
# 4.1.1 Configure Data Retention
# 4.1.1.1 Ensure audit log storage size is configured
# 4.1.1.2 Ensure system is disabled when audit logs are full
def task_4_1_1_2(fixbug=False):
	check = os.popen('grep space_left_action /etc/audit/auditd.conf').read()
	check2 = os.popen('grep action_mail_acct /etc/audit/auditd.conf').read()
	check3 = os.popen('grep admin_space_left_action /etc/audit/auditd.conf').read()

	if (check == 'space_left_action = email' and check2 == 'action_mail_acct = root' and check3 == 'admin_space_left_action = halt'):
		return True
	if (fixbug == True): fix_4_1_1_2()
	return False

def fix_4_1_1_2():
	helper.replaceLine('/etc/audit/auditd.conf', 'space_left_action', 'space_left_action = email')
	helper.replaceLine('/etc/audit/auditd.conf', 'action_mail_acct', 'action_mail_acct = root')
	helper.replaceLine('/etc/audit/auditd.conf', 'admin_space_left_action', 'admin_space_left_action = halt')

# 4.1.1.3 Ensure audit logs are not automatically deleted
def task_4_1_1_3(fixbug=False):
	check = os.popen('grep max_log_file_action /etc/audit/auditd.conf').read()

	if (check == 'max_log_file_action = keep_logs'):
		return True
	if (fixbug == True): fix_4_1_1_3()
	return False

def fix_4_1_1_3():
	helper.replaceLine('/etc/audit/auditd.conf', 'max_log_file_action', 'max_log_file_action = keep_logs')

# 4.1.2 Ensure auditd service is enabled
def task_4_1_2(fixbug=False):
	check = os.popen("systemctl is-enabled auditd").read()

	if (check == 'enabled'):
		return True
	if(fixbug == True): fix_4_1_2()			
	return False

def fix_4_1_2():
	os.popen("systemctl enable auditd")

# 4.1.3 Ensure auditing for processes that start prior to auditd is enabled
def task_4_1_3(fixbug=False):
	check = os.popen('grep "^\s*linux" /boot/grub/grub.cfg').read()

	if (re.search("audit=1", check)):
		return True
	if (fixbug == True): fix_4_1_3()
	return False

def fix_4_1_3():
	helper.replaceLine('/etc/default/grub', '"^\s*linux"', 'GRUB_CMDLINE_LINUX="audit=1"')
	os.popen("update-grub")

# 4.1.18 Ensure the audit configuration is immutable
def task_4_1_18(fixbug=False):
	check = os.popen('grep "^\s*[^#]" /etc/audit/audit.rules | tail -1').read()

	if (check == '-e 2'):
		return True
	if (fixbug == True): fix_4_1_18()
	return False

def fix_4_1_18():
	helper.replaceLine('/etc/audit/audit.rules', '"^\s*[^#]"', '-e 2')

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
	os.popen("systemctl enable rsyslog")

# 4.2.1.5 Ensure remote rsyslog messages are only accepted on designated log hosts
def task_4_2_1_5(fixbug=False):
	check = os.popen("grep '$ModLoad imtcp' /etc/rsyslog.conf /etc/rsyslog.d/*.conf").read()
	check2 = os.popen("grep '$InputTCPServerRun' /etc/rsyslog.conf /etc/rsyslog.d/*.conf").read()

	if (check == '$ModLoad imtcp' and check2 == '$InputTCPServerRun 514'):
		return True
	if(fixbug == True): fix_4_2_1_5()			
	return False

def fix_4_2_1_5():
	helper.replaceLine('/etc/rsyslog.conf', '$ModLoad', '$ModLoad imtcp')
	helper.replaceLine('/etc/rsyslog.conf', '$InputTCPServerRun', '$InputTCPServerRun 514')
	# fix
	os.popen("pkill -HUP rsyslogd")

# 4.2.2 Configure syslog-ng
# 4.2.2.1 Ensure syslog-ng service is enabled
def task_4_2_2_1(fixbug=False):
	check = os.popen("systemctl is-enabled syslog-ng").read()

	if (check == 'enabled'):
		return True
	if(fixbug == True): fix_4_2_2_1()			
	return False

def fix_4_2_2_1():
	os.popen("update-rc.d syslog-ng enable")

# 4.2.2.3 Ensure syslog-ng default file permissions configured
def task_4_2_2_3(fixbug=False):
	check = os.popen("grep ^options /etc/syslog-ng/syslog-ng.conf").read()

	if (check == 'options { chain_hostnames(off); flush_lines(0); perm(0640); stats_freq(3600); hreaded(yes); };'):
		return True
	if(fixbug == True): fix_4_2_2_3()			
	return False

def fix_4_2_2_3():
	helper.replaceLine('/etc/rsyslog.conf', '^options', 'options { chain_hostnames(off); flush_lines(0); perm(0640); stats_freq(3600); threaded(yes); };')

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

# 4.2.4 Ensure permissions on all logfiles are configured
def task_4_2_4(fixbug=False):
	check = os.popen("find /var/log -type f -ls").read()

def fix_4_2_4():
	os.popen("chmod -R g-wx,o-rwx /var/log/*")