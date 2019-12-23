import subprocess, os, re, sys, stat
test_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(test_path)

import helper as helper

# 4 Logging and Auditing
# 4.1 Configure System Accounting (auditd)
# 4.1.1 Configure Data Retention
# 4.1.1.1 Ensure audit log storage size is configured
def task_4_1_1_1(fixbug=False):
	check = os.popen('max_log_file =').read()

	if (re.search('max_log_file =', check)):
		return True
	# show guide
	return False

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
	uuid, after = os.popen('findmnt / -o UUID -n').read().split('\n')
	check_grep = subprocess.Popen('grep "^\s*linux" /boot/grub/grub.cfg', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	for line in check_grep.stdout.readlines():
		if (uuid in line and not re.search("audit=1", line)):
			if (fixbug == True): fix_4_1_3()

			return False

	return True

def fix_4_1_3():
	helper.replaceLine('/etc/default/grub', '"^\s*linux"', 'GRUB_CMDLINE_LINUX="audit=1"')
	os.popen("update-grub")

# 4.1.4 Ensure events that modify date and time information are collected
def task_4_1_4(fixbug=False):
	ubuntu, after = os.popen('getconf LONG_BIT').read().split('\n')
	check = os.popen('grep time-change /etc/audit/audit.rules').read()
	check2 = os.popen('auditctl -l | grep time-change').read()
	filePath = '/etc/audit/audit.rules'

	check_32_line_1 = '-a always,exit -F arch=b32 -S adjtimex -S settimeofday -S stime -k time-change'
	check_32_line_2 = '-a always,exit -F arch=b32 -S clock_settime -k time-change'

	check_64_line_1 = '-a always,exit -F arch=b64 -S adjtimex -S settimeofday -k time-change'
	check_64_line_2 = '-a always,exit -F arch=b32 -S adjtimex -S settimeofday -S stime -k time-change'
	check_64_line_3 = '-a always,exit -F arch=b64 -S clock_settime -k time-change'
	check_64_line_4 = '-a always,exit -F arch=b32 -S clock_settime -k time-change'
	check_line = '-w /etc/localtime -p wa -k time-change'

	if (ubuntu == '32'):
		if (re.search(check_32_line_1, check) and re.search(check_32_line_2, check) and re.search(check_line, check) and re.search(check_32_line_1, check2) and re.search(check_32_line_2, check2) and re.search(check_line, check2)):
			return True
		else: 
			if (fixbug == True):
				helper.replaceLine(filePath, check_32_line_1, check_32_line_1)
				helper.replaceLine(filePath, check_32_line_2, check_32_line_2)
				helper.replaceLine(filePath, check_line, check_line)
				os.popen("systemctl reload auditd")

			return False
	elif (ubuntu == '64'):
		if (re.search(check_64_line_1, check) and re.search(check_64_line_2, check) and re.search(check_64_line_3, check) and re.search(check_64_line_4, check) and re.search(check_line, check) and re.search(check_64_line_1, check2) and re.search(check_64_line_2, check2) and re.search(check_64_line_3, check2) and re.search(check_64_line_4, check2) and re.search(check_line, check2)):
			return True
		else: 
			if (fixbug == True):
				helper.replaceLine(filePath, check_64_line_1, check_64_line_1)
				helper.replaceLine(filePath, check_64_line_2, check_64_line_2)
				helper.replaceLine(filePath, check_64_line_3, check_64_line_3)
				helper.replaceLine(filePath, check_64_line_4, check_64_line_4)
				helper.replaceLine(filePath, check_line, check_line)
				os.popen("systemctl reload auditd")

			return False

# 4.1.5 Ensure events that modify user/group information are collected
def task_4_1_5(fixbug=False):
	check = os.popen('grep identity /etc/audit/audit.rules').read()
	check2 = os.popen('auditctl -l | grep identity').read()
	line_1 = '-w /etc/group -p wa -k identity'
	line_2 = '-w /etc/passwd -p wa -k identity'
	line_3 = '-w /etc/gshadow -p wa -k identity'
	line_4 = '-w /etc/shadow -p wa -k identity'
	line_5 = '-w /etc/security/opasswd -p wa -k identity'
	filePath = '/etc/audit/audit.rules'

	if (re.search(line_1, check) and re.search(line_2, check) and re.search(line_3, check) and re.search(line_4, check) and re.search(line_5, check) and re.search(line_1, check2) and re.search(line_2, check2) and re.search(line_3, check2) and re.search(line_4, check2) and re.search(line_5, check2)):
		return True
	else:
		if (fixbug == True):
			helper.replaceLine(filePath, line_1, line_1)
			helper.replaceLine(filePath, line_2, line_2)
			helper.replaceLine(filePath, line_3, line_3)
			helper.replaceLine(filePath, line_4, line_4)
			helper.replaceLine(filePath, line_5, line_5)
			os.popen("systemctl reload auditd")

		return False

# 4.1.6 Ensure events that modify the system's network environment are collected
def task_4_1_6(fixbug=False):
	ubuntu, after = os.popen('getconf LONG_BIT').read().split('\n')
	check = os.popen('grep system-locale /etc/audit/audit.rules').read()
	check2 = os.popen('auditctl -l | grep system-locale').read()
	filePath = '/etc/audit/audit.rules'

	check_32_line = '-a always,exit -F arch=b32 -S sethostname -S setdomainname -k system-locale'
	check_64_line = '-a always,exit -F arch=b64 -S sethostname -S setdomainname -k system-locale'
	check_line_1 = '-w /etc/issue -p wa -k system-locale'
	check_line_2 = '-w /etc/issue.net -p wa -k system-locale'
	check_line_3 = '-w /etc/hosts -p wa -k system-locale'
	check_line_4 = '-w /etc/network -p wa -k system-locale'

	if (ubuntu == '32'):
		if (re.search(check_32_line, check) and re.search(check_line_1, check) and re.search(check_line_2, check) and re.search(check_line_3, check) and re.search(check_line_4, check) and re.search(check_32_line, check2) and re.search(check_line_1, check2) and re.search(check_line_2, check2) and re.search(check_line_3, check2) and re.search(check_line_4, check2)):
			return True
		else:
			if (fixbug == True):
				helper.replaceLine(filePath, check_32_line, check_32_line)
				helper.replaceLine(filePath, check_line_1, check_line_1)
				helper.replaceLine(filePath, check_line_2, check_line_2)
				helper.replaceLine(filePath, check_line_3, check_line_3)
				helper.replaceLine(filePath, check_line_4, check_line_4)
				os.popen("systemctl reload auditd")

			return False
	elif (ubuntu == '64'):
		if (re.search(check_32_line, check) and re.search(check_64_line, check) and re.search(check_line_1, check) and re.search(check_line_2, check) and re.search(check_line_3, check) and re.search(check_line_4, check) and re.search(check_32_line, check2) and re.search(check_64_line, check2) and re.search(check_line_1, check2) and re.search(check_line_2, check2) and re.search(check_line_3, check2) and re.search(check_line_4, check2)):
			return True
		else:
			if (fixbug == True):
				helper.replaceLine(filePath, check_32_line, check_32_line)
				helper.replaceLine(filePath, check_64_line, check_64_line)
				helper.replaceLine(filePath, check_line_1, check_line_1)
				helper.replaceLine(filePath, check_line_2, check_line_2)
				helper.replaceLine(filePath, check_line_3, check_line_3)
				helper.replaceLine(filePath, check_line_4, check_line_4)
				os.popen("systemctl reload auditd")

			return False

	return True

# 4.1.7 Ensure events that modify the system's Mandatory Access Controls are collected
def task_4_1_7(fixbug=False):
	dpkg_apparmor = os.popen("dpkg -s apparmor").read()

	check = os.popen('grep MAC-policy /etc/audit/audit.rules').read()
	check2 = os.popen('auditctl -l | grep MAC-policy').read()

	check_apparmor_1 = '-w /etc/apparmor/ -p wa -k MAC-policy'
	check_apparmor_2 = '-w /etc/apparmor.d/ -p wa -k MAC-policy'

	check_selinux_1 = '-w /etc/selinux/ -p wa -k MAC-policy'
	check_selinux_2 = '-w /usr/share/selinux/ -p wa -k MAC-policy'
	filePath = '/etc/audit/audit.rules'

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg_apparmor)):
		if (re.search(check_apparmor_1, check) and re.search(check_apparmor_2, check) and re.search(check_apparmor_1, check2) and re.search(check_apparmor_2, check2)):
			return True
		else:
			if (fixbug == True):
				helper.replaceLine(filePath, check_apparmor_1, check_apparmor_1)
				helper.replaceLine(filePath, check_apparmor_2, check_apparmor_2)
				os.popen("systemctl reload auditd")

			return False
	else:
		dpkg_selinux = os.popen("dpkg -s selinux").read()

		if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg_selinux)):
			if (re.search(check_selinux_1, check) and re.search(check_selinux_2, check) and re.search(check_selinux_1, check2) and re.search(check_selinux_2, check2)):
				return True
			else:
				if (fixbug == True):
					helper.replaceLine(filePath, check_selinux_1, check_selinux_1)
					helper.replaceLine(filePath, check_selinux_2, check_selinux_2)
					os.popen("systemctl reload auditd")

				return False

	return True

# 4.1.8 Ensure login and logout events are collected
def task_4_1_8(fixbug=False):
	check = os.popen('grep logins /etc/audit/audit.rules').read()
	check2 = os.popen('auditctl -l | grep logins').read()

	line_1 = '-w /var/log/faillog -p wa -k logins'
	line_2 = '-w /var/log/lastlog -p wa -k logins'
	line_3 = '-w /var/log/tallylog -p wa -k logins'
	filePath = '/etc/audit/audit.rules'

	if (re.search(line_1, check) and re.search(line_2, check) and re.search(line_3, check) and re.search(line_1, check2) and re.search(line_2, check2) and re.search(line_3, check2)):
		return True
	else:
		if (fixbug == True):
			helper.replaceLine(filePath, line_1, line_1)
			helper.replaceLine(filePath, line_2, line_2)
			helper.replaceLine(filePath, line_3, line_3)
			os.popen("systemctl reload auditd")

		return False

# 4.1.9 Ensure session initiation information is collected
def task_4_1_9(fixbug=False):
	check = os.popen('grep session /etc/audit/audit.rules').read()
	check2 = os.popen('auditctl -l | grep session').read()

	line_session = '-w /var/run/utmp -p wa -k session'
	filePath = '/etc/audit/audit.rules'

	check3 = os.popen('grep logins /etc/audit/audit.rules').read()
	check4 = os.popen('auditctl -l | grep logins').read()

	line_login_1 = '-w /var/log/wtmp -p wa -k logins'
	line_login_2 = '-w /var/log/btmp -p wa -k logins'

	if (re.search(line_session, check) and re.search(line_session, check2) and re.search(line_login_1, check3) and re.search(line_login_2, check3) and re.search(line_login_1, check4) and re.search(line_login_2, check4)):
		return True
	else:
		if (fixbug == True):
			helper.replaceLine(filePath, line_session, line_session)
			helper.replaceLine(filePath, line_login_1, line_login_1)
			helper.replaceLine(filePath, line_login_2, line_login_2)
			os.popen("systemctl reload auditd")

		return False

# 4.1.10 Ensure discretionary access control permission modification events are collected
def task_4_1_10(fixbug=False):
	ubuntu, after = os.popen('getconf LONG_BIT').read().split('\n')
	filePath = '/etc/audit/audit.rules'

	check = os.popen('grep perm_mod /etc/audit/audit.rules').read()
	check2 = os.popen('auditctl -l | grep perm_mod').read()

	check_32_line_1 = '-a always,exit -F arch=b32 -S chmod -S fchmod -S fchmodat -F auid>=1000 -F auid!=4294967295 -k perm_mod'
	check_32_line_2 = '-a always,exit -F arch=b32 -S chown -S fchown -S fchownat -S lchown -F auid>=1000 -F auid!=4294967295 -k perm_mod'
	check_32_line_3 = '-a always,exit -F arch=b32 -S setxattr -S lsetxattr -S fsetxattr -S removexattr -S lremovexattr -S fremovexattr -F auid>=1000 -F auid!=4294967295 -k perm_mod'

	check_64_line_1 = '-a always,exit -F arch=b64 -S chmod -S fchmod -S fchmodat -F auid>=1000 -F auid!=4294967295 -k perm_mod'
	check_64_line_2 = '-a always,exit -F arch=b64 -S chown -S fchown -S fchownat -S lchown -F auid>=1000 -F auid!=4294967295 -k perm_mod'
	check_64_line_3 = '-a always,exit -F arch=b64 -S setxattr -S lsetxattr -S fsetxattr -S removexattr -S lremovexattr -S fremovexattr -F auid>=1000 -F auid!=4294967295 -k perm_mod'

	if (ubuntu == '32'):
		if (re.search(check_32_line_1, check) and re.search(check_32_line_2, check) and re.search(check_32_line_3, check) and re.search(check_32_line_1, check2) and re.search(check_32_line_2, check2) and re.search(check_32_line_3, check2)):
			return True
		else:
			if (fixbug == True):
				helper.replaceLine(filePath, check_32_line_1, check_32_line_1)
				helper.replaceLine(filePath, check_32_line_2, check_32_line_2)
				helper.replaceLine(filePath, check_32_line_3, check_32_line_3)
				os.popen("systemctl reload auditd")

			return False
	elif (ubuntu == '64'):
		if (re.search(check_32_line_1, check) and re.search(check_32_line_2, check) and re.search(check_32_line_3, check) and re.search(check_32_line_1, check2) and re.search(check_32_line_2, check2) and re.search(check_32_line_3, check2) and re.search(check_64_line_1, check) and re.search(check_64_line_2, check) and re.search(check_64_line_3, check) and re.search(check_64_line_1, check2) and re.search(check_64_line_2, check2) and re.search(check_64_line_3, check2)):
			return True
		else:
			if (fixbug == True):
				helper.replaceLine(filePath, check_32_line_1, check_32_line_1)
				helper.replaceLine(filePath, check_32_line_2, check_32_line_2)
				helper.replaceLine(filePath, check_32_line_3, check_32_line_3)
				helper.replaceLine(filePath, check_64_line_1, check_64_line_1)
				helper.replaceLine(filePath, check_64_line_2, check_64_line_2)
				helper.replaceLine(filePath, check_64_line_3, check_64_line_3)
				os.popen("systemctl reload auditd")

			return False

	return True

# 4.1.11 Ensure unsuccessful unauthorized file access attempts are collected
def task_4_1_11(fixbug=False):
	ubuntu, after = os.popen('getconf LONG_BIT').read().split('\n')
	filePath = '/etc/audit/audit.rules'

	check = os.popen('grep access /etc/audit/audit.rules').read()
	check2 = os.popen('auditctl -l | grep access').read()

	check_32_line_1 = '-a always,exit -F arch=b32 -S creat -S open -S openat -S truncate -S ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access'
	check_32_line_2 = '-a always,exit -F arch=b32 -S creat -S open -S openat -S truncate -S ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access'

	check_64_line_1 = '-a always,exit -F arch=b64 -S creat -S open -S openat -S truncate -S ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access'
	check_64_line_2 = '-a always,exit -F arch=b64 -S creat -S open -S openat -S truncate -S ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access'

	if (ubuntu == '32'):
		if (re.search(check_32_line_1, check) and re.search(check_32_line_2, check) and re.search(check_32_line_1, check2) and re.search(check_32_line_2, check2)):
			return True
		else:
			if (fixbug == True):
				helper.replaceLine(filePath, check_32_line_1, check_32_line_1)
				helper.replaceLine(filePath, check_32_line_2, check_32_line_2)
				os.popen("systemctl reload auditd")

			return False
	elif (ubuntu == '64'):
		if (re.search(check_32_line_1, check) and re.search(check_32_line_2, check) and re.search(check_32_line_1, check2) and re.search(check_32_line_2, check2) and re.search(check_64_line_1, check) and re.search(check_64_line_2, check) and re.search(check_64_line_1, check2) and re.search(check_64_line_2, check2)):
			return True
		else:
			if (fixbug == True):
				helper.replaceLine(filePath, check_32_line_1, check_32_line_1)
				helper.replaceLine(filePath, check_32_line_2, check_32_line_2)
				helper.replaceLine(filePath, check_64_line_1, check_64_line_1)
				helper.replaceLine(filePath, check_64_line_2, check_64_line_2)
				os.popen("systemctl reload auditd")

			return False

	return True

# 4.1.12 Ensure use of privileged commands is collected

# 4.1.13 Ensure successful file system mounts are collected
def task_4_1_13(fixbug=False):
	ubuntu, after = os.popen('getconf LONG_BIT').read().split('\n')
	filePath = '/etc/audit/audit.rules'

	check = os.popen('grep mounts /etc/audit/audit.rules').read()
	check2 = os.popen('auditctl -l | grep mounts').read()

	check_32_line_1 = '-a always,exit -F arch=b32 -S mount -F auid>=1000 -F auid!=4294967295 -k mounts'

	check_64_line_1 = '-a always,exit -F arch=b64 -S mount -F auid>=1000 -F auid!=4294967295 -k mounts'

	if (ubuntu == '32'):
		if (re.search(check_32_line_1, check) and re.search(check_32_line_1, check2)):
			return True
		else:
			if (fixbug == True):
				helper.replaceLine(filePath, check_32_line_1, check_32_line_1)
				os.popen("systemctl reload auditd")

			return False
	elif (ubuntu == '64'):
		if (re.search(check_32_line_1, check) and re.search(check_32_line_1, check2) and re.search(check_64_line_1, check) and re.search(check_64_line_1, check2)):
			return True
		else:
			if (fixbug == True):
				helper.replaceLine(filePath, check_32_line_1, check_32_line_1)
				helper.replaceLine(filePath, check_64_line_1, check_64_line_1)
				os.popen("systemctl reload auditd")

			return False
	return True

# 4.1.14 Ensure file deletion events by users are collected
def task_4_1_14(fixbug=False):
	ubuntu, after = os.popen('getconf LONG_BIT').read().split('\n')
	filePath = '/etc/audit/audit.rules'

	check = os.popen('grep delete /etc/audit/audit.rules').read()
	check2 = os.popen('auditctl -l | grep delete').read()

	check_32_line_1 = '-a always,exit -F arch=b32 -S unlink -S unlinkat -S rename -S renameat -F auid>=1000 -F auid!=4294967295 -k delete'

	check_64_line_1 = '-a always,exit -F arch=b64 -S unlink -S unlinkat -S rename -S renameat -F auid>=1000 -F auid!=4294967295 -k delete'

	if (ubuntu == '32'):
		if (re.search(check_32_line_1, check) and re.search(check_32_line_1, check2)):
			return True
		else:
			if (fixbug == True):
				helper.replaceLine(filePath, check_32_line_1, check_32_line_1)
				os.popen("systemctl reload auditd")

			return False
	elif (ubuntu == '64'):
		if (re.search(check_32_line_1, check) and re.search(check_32_line_1, check2) and re.search(check_64_line_1, check) and re.search(check_64_line_1, check2)):
			return True
		else:
			if (fixbug == True):
				helper.replaceLine(filePath, check_32_line_1, check_32_line_1)
				helper.replaceLine(filePath, check_64_line_1, check_64_line_1)
				os.popen("systemctl reload auditd")

			return False
	return True

# 4.1.15 Ensure changes to system administration scope (sudoers) is collected
def task_4_1_15(fixbug=False):
	check = os.popen('grep scope /etc/audit/audit.rules').read()
	check2 = os.popen('auditctl -l | grep scope').read()

	line_1 = '-w /etc/sudoers -p wa -k scope'
	line_2 = '-w /etc/sudoers.d/ -p wa -k scope'
	filePath = '/etc/audit/audit.rules'

	if (re.search(line_1, check) and re.search(line_2, check) and re.search(line_1, check2) and re.search(line_2, check2)):
		return True
	else:
		if (fixbug == True):
			helper.replaceLine(filePath, line_1, line_1)
			helper.replaceLine(filePath, line_2, line_2)
			os.popen("systemctl reload auditd")

		return False

# 4.1.16 Ensure system administrator actions (sudolog) are collected
def task_4_1_16(fixbug=False):
	check = os.popen('grep actions /etc/audit/audit.rules').read()
	check2 = os.popen('auditctl -l | grep actions').read()

	line_1 = '-w /var/log/sudo.log -p wa -k actions'
	filePath = '/etc/audit/audit.rules'

	if (re.search(line_1, check) and re.search(line_1, check2)):
		return True
	else:
		if (fixbug == True):
			helper.replaceLine(filePath, line_1, line_1)
			os.popen("systemctl reload auditd")

		return False

# 4.1.17 Ensure kernel module loading and unloading is collected
def task_4_1_17(fixbug=False):
	ubuntu, after = os.popen('getconf LONG_BIT').read().split('\n')
	filePath = '/etc/audit/audit.rules'

	check = os.popen('grep modules /etc/audit/audit.rules').read()
	check2 = os.popen('auditctl -l | grep modules').read()

	check_line_1 ='-w /sbin/insmod -p x -k modules'
	check_line_2 ='-w /sbin/rmmod -p x -k modules'
	check_line_3 ='-w /sbin/modprobe -p x -k modules'

	check_32_line = '-a always,exit -F arch=b32 -S init_module -S delete_module -k modules'
	check_64_line = '-a always,exit -F arch=b64 -S init_module -S delete_module -k modules'

	if (ubuntu == '32'):
		if (re.search(check_line_1, check) and re.search(check_line_2, check) and re.search(check_line_3, check) and re.search(check_line_1, check2) and re.search(check_line_2, check2) and re.search(check_line_3, check2) and re.search(check_32_line, check) and re.search(check_32_line, check2)):
			return True
		else:
			if (fixbug == True):
				helper.replaceLine(filePath, check_line_1, check_line_1)
				helper.replaceLine(filePath, check_line_2, check_line_2)
				helper.replaceLine(filePath, check_line_3, check_line_3)
				helper.replaceLine(filePath, check_32_line, check_32_line)
				os.popen("systemctl reload auditd")

			return False
	elif (ubuntu == '64'):
		if (re.search(check_line_1, check) and re.search(check_line_2, check) and re.search(check_line_3, check) and re.search(check_line_1, check2) and re.search(check_line_2, check2) and re.search(check_line_3, check2) and re.search(check_64_line, check) and re.search(check_64_line, check2)):
			return True
		else:
			if (fixbug == True):
				helper.replaceLine(filePath, check_line_1, check_line_1)
				helper.replaceLine(filePath, check_line_2, check_line_2)
				helper.replaceLine(filePath, check_line_3, check_line_3)
				helper.replaceLine(filePath, check_64_line, check_64_line)
				os.popen("systemctl reload auditd")

			return False
	return True

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
def check_install_rsyslog():
	dpkg = os.popen("dpkg -s rsyslog").read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg)):
		return True
	return False

# 4.2.1.1 Ensure rsyslog Service is enabled
def task_4_2_1_1(fixbug=False):
	if (check_install_rsyslog()):
		check = os.popen("systemctl is-enabled rsyslog").read()

		if (check == 'enabled'):
			return True
		if(fixbug == True): fix_4_2_1_1()			
		return False
	return True

def fix_4_2_1_1():
	os.popen("systemctl enable rsyslog")

# 4.2.1.3 Ensure rsyslog default file permissions configured
def task_4_2_1_3(fixbug=False):
	if (check_install_rsyslog()):
		check = os.popen("grep ^\$FileCreateMode /etc/rsyslog.conf /etc/rsyslog.d/*.conf").read()

		if (re.search('\$FileCreateMode 0640', check)):
			return True
		if(fixbug == True): fix_4_2_1_3()			
		return False
	return True

def fix_4_2_1_3():
	helper.replaceLine('/etc/rsyslog.conf', '^\$FileCreateMode', '$FileCreateMode 0640')

# 4.2.1.4 Ensure rsyslog is configured to send logs to a remote log host
def task_4_2_1_4(fixbug=False):
	if (check_install_rsyslog()):
		check = os.popen('grep "^*.*[^I][^I]*@" /etc/rsyslog.conf /etc/rsyslog.d/*.conf').read()

		if (check != ''):
			return True
		# show guide
		return False
	return True

# 4.2.1.5 Ensure remote rsyslog messages are only accepted on designated log hosts
def task_4_2_1_5(fixbug=False):
	if (check_install_rsyslog()):
		check = os.popen("grep '$ModLoad imtcp' /etc/rsyslog.conf /etc/rsyslog.d/*.conf").read()
		check2 = os.popen("grep '$InputTCPServerRun' /etc/rsyslog.conf /etc/rsyslog.d/*.conf").read()

		if (check == '$ModLoad imtcp' and check2 == '$InputTCPServerRun 514'):
			return True
		# show guide
		return False
	return True

# 4.2.2 Configure syslog-ng
def check_install_syslogng():
	dpkg = os.popen("dpkg -s syslog-ng").read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg)):
		return True
	return False

# 4.2.2.1 Ensure syslog-ng service is enabled
def task_4_2_2_1(fixbug=False):
	if (check_install_syslogng()):
		check = os.popen("systemctl is-enabled syslog-ng").read()

		if (check == 'enabled'):
			return True
		if(fixbug == True): fix_4_2_2_1()			
		return False
	return True

def fix_4_2_2_1():
	os.popen("update-rc.d syslog-ng enable")

# 4.2.2.3 Ensure syslog-ng default file permissions configured
def task_4_2_2_3(fixbug=False):
	if (check_install_syslogng()):
		check = os.popen("grep ^options /etc/syslog-ng/syslog-ng.conf").read()

		if (check == 'options { chain_hostnames(off); flush_lines(0); perm(0640); stats_freq(3600); hreaded(yes); };'):
			return True
		if(fixbug == True): fix_4_2_2_3()			
		return False
	return True

def fix_4_2_2_3():
	helper.replaceLine('/etc/rsyslog.conf', '^options', 'options { chain_hostnames(off); flush_lines(0); perm(0640); stats_freq(3600); threaded(yes); };')

# 4.2.3 Ensure rsyslog or syslog-ng is installed
def task_4_2_3(fixbug=False):
	dpkg_rsyslog = os.popen("dpkg -s rsyslog").read()
	dpkg_syslog = os.popen("dpkg -s syslog-ng").read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg_rsyslog) or re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg_syslog)):
		return True
	if (fixbug == True): fix_4_2_3()
	return False

def fix_4_2_3():
	os.popen("apt-get install rsyslog -y")

# 4.2.4 Ensure permissions on all logfiles are configured
def task_4_2_4(fixbug=False):
	permissions = subprocess.Popen('find /var/log -type f -ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in permissions.stdout.readlines():
		line, after = line.split('\n')
		permission = re.split('([rwx-]+)', line)[1]
		if (permission[4 : None] != 'r-----'):
			if (fixbug == True): fix_4_2_4()

			return False

	return True

def fix_4_2_4():
	os.popen("chmod -R g-wx,o-rwx /var/log/*")

# 4.3 Ensure logrotate is configured