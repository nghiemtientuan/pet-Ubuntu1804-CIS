import subprocess, os, re
test_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(test_path)

import helper as helper

# 5 Access, Authentication and Authorization
# 5.1 Configure cron
# 5.1.1 Ensure cron daemon is enabled
def task_5_1_1(fixbug=False):
	check = os.popen("systemctl is-enabled cron").read()

	if (check == 'enabled'):
		return True
	if(fixbug == True): fix_5_1_1()			
	return False

def fix_5_1_1():
	os.popen("systemctl enable cron")

# 5.1.2 Ensure permissions on /etc/crontab are configured
def task_5_1_2(fixbug=False):
	stat = os.popen("stat /etc/crontab").read()

	if (re.search("Access:[\s]+\(0600/-rw-------\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat)):
		return True
	if(fixbug == True): fix_5_1_2()
	return False

def fix_5_1_2():
	os.popen("chown root:root /etc/crontab")
	os.popen("chmod og-rwx /etc/crontab")

# 5.1.3 Ensure permissions on /etc/cron.hourly are configured
def task_5_1_3(fixbug=False):
	stat = os.popen("stat /etc/cron.hourly").read()

	if (re.search("Access:[\s]+\(0700/drwx------\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat)):
		return True
	if(fixbug == True): fix_5_1_3()
	return False

def fix_5_1_3():
	os.popen("chown root:root /etc/cron.hourly")
	os.popen("chmod og-rwx /etc/cron.hourly")

# 5.1.4 Ensure permissions on /etc/cron.daily are configured
def task_5_1_4(fixbug=False):
	stat = os.popen("stat /etc/cron.daily").read()

	if (re.search("Access:[\s]+\(0700/drwx------\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat)):
		return True
	if(fixbug == True): fix_5_1_4()
	return False

def fix_5_1_4():
	os.popen("chown root:root /etc/cron.daily")
	os.popen("chmod og-rwx /etc/cron.daily")

# 5.1.5 Ensure permissions on /etc/cron.weekly are configured
def task_5_1_5(fixbug=False):
	stat = os.popen("stat /etc/cron.weekly").read()

	if (re.search("Access:[\s]+\(0700/drwx------\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat)):
		return True
	if(fixbug == True): fix_5_1_5()
	return False

def fix_5_1_5():
	os.popen("chown root:root /etc/cron.weekly")
	os.popen("chmod og-rwx /etc/cron.weekly")

# 5.1.6 Ensure permissions on /etc/cron.monthly are configured
def task_5_1_6(fixbug=False):
	stat = os.popen("stat /etc/cron.monthly").read()

	if (re.search("Access:[\s]+\(0700/drwx------\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat)):
		return True
	if(fixbug == True): fix_5_1_6()
	return False

def fix_5_1_6():
	os.popen("chown root:root /etc/cron.monthly")
	os.popen("chmod og-rwx /etc/cron.monthly")

# 5.1.7 Ensure permissions on /etc/cron.d are configured
def task_5_1_7(fixbug=False):
	stat = os.popen("stat /etc/cron.d").read()

	if (re.search("Access:[\s]+\(0700/drwx------\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat)):
		return True
	if(fixbug == True): fix_5_1_7()
	return False

def fix_5_1_7():
	os.popen("chown root:root /etc/cron.d")
	os.popen("chmod og-rwx /etc/cron.d")

# 5.1.8 Ensure at/cron is restricted to authorized users
def task_5_1_8(fixbug=False):
	stat = os.popen("stat /etc/cron.deny").read()
	stat2 = os.popen("stat /etc/at.deny").read()

	stat3 = os.popen("stat /etc/cron.allow").read()
	stat4 = os.popen("stat /etc/at.allow").read()
	if (stat == '' and stat2 == '' and re.search("Access:[\s]+\(0600/-rw-------\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat3) and re.search("Access:[\s]+\(0600/-rw-------\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat4)):
		return True
	if(fixbug == True): fix_5_1_8()
	return False

def fix_5_1_8():
	os.popen("rm /etc/cron.deny")
	os.popen("rm /etc/at.deny")
	os.popen("touch /etc/cron.allow")
	os.popen("touch /etc/at.allow")
	os.popen("chmod og-rwx /etc/cron.allow")
	os.popen("chmod og-rwx /etc/at.allow")
	os.popen("chown root:root /etc/cron.allow")
	os.popen("chown root:root /etc/at.allow")

# 5.2 SSH Server Configuration
def check_SSH_daemon_installed():
	check = os.popen("ls -ld /etc/ssh/sshd_config").read()

	if (re.search("/etc/ssh/sshd_config", check)):
		return True
	rehelper.replaceLine('/etc/audit/auditd.conf', 'space_left_action', 'space_left_action = email')turn False

# 5.2.1 Ensure permissions on /etc/ssh/sshd_config are configured
def task_5_2_1(fixbug=False):
	if (check_SSH_daemon_installed):
		stat = os.popen("stat /etc/ssh/sshd_config").read()

		if (re.search("Access:[\s]+\(0600/-rw-------\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat)):
			return True
		if(fixbug == True): fix_5_2_1()
		return False
	return True

def fix_5_2_1():
	os.popen("chown root:root /etc/ssh/sshd_config")
	os.popen("chmod og-rwx /etc/ssh/sshd_config")

# 5.2.2 Ensure SSH Protocol is set to 2
def task_5_2_2(fixbug=False):
	if (check_SSH_daemon_installed):
		check = os.popen('grep "^Protocol" /etc/ssh/sshd_config').read()

		if (check == 'Protocol 2'):
			return True
		if(fixbug == True): fix_5_2_2()
		return False
	return True

def fix_5_2_2():
	helper.replaceLine('/etc/ssh/sshd_config', '^Protocol', 'Protocol 2')

# 5.2.3 Ensure SSH LogLevel is set to INFO
def task_5_2_3(fixbug=False):
	if (check_SSH_daemon_installed):
		check = os.popen('grep "^LogLevel" /etc/ssh/sshd_config').read()

		if (check == 'LogLevel INFO'):
			return True
		if(fixbug == True): fix_5_2_3()
		return False
	return True

def fix_5_2_3():
	helper.replaceLine('/etc/ssh/sshd_config', '^LogLevel', 'LogLevel INFO')

# 5.2.4 Ensure SSH X11 forwarding is disabled
def task_5_2_4(fixbug=False):
	if (check_SSH_daemon_installed):
		check = os.popen('grep "^X11Forwarding" /etc/ssh/sshd_config').read()

		if (check == 'X11Forwarding no'):
			return True
		if(fixbug == True): fix_5_2_4()
		return False
	return True

def fix_5_2_4():
	helper.replaceLine('/etc/ssh/sshd_config', '^X11Forwarding', 'X11Forwarding no')

# 5.2.5 Ensure SSH MaxAuthTries is set to 4 or less
def task_5_2_5(fixbug=False):
	if (check_SSH_daemon_installed):
		check = os.popen('grep "^MaxAuthTries" /etc/ssh/sshd_config').read()

		if (check == 'MaxAuthTries 4'):
			return True
		if(fixbug == True): fix_5_2_5()
		return False
	return True

def fix_5_2_5():
	helper.replaceLine('/etc/ssh/sshd_config', '^MaxAuthTries', 'MaxAuthTries 4')

# 5.2.6 Ensure SSH IgnoreRhosts is enabled
def task_5_2_6(fixbug=False):
	if (check_SSH_daemon_installed):
		check = os.popen('grep "^IgnoreRhosts" /etc/ssh/sshd_config').read()

		if (check == 'IgnoreRhosts yes'):
			return True
		if(fixbug == True): fix_5_2_6()
		return False
	return True

def fix_5_2_6():
	helper.replaceLine('/etc/ssh/sshd_config', '^IgnoreRhosts', 'IgnoreRhosts yes')

# 5.2.7 Ensure SSH HostbasedAuthentication is disabled
def task_5_2_7(fixbug=False):
	if (check_SSH_daemon_installed):
		check = os.popen('grep "^HostbasedAuthentication" /etc/ssh/sshd_config').read()

		if (check == 'HostbasedAuthentication no'):
			return True
		if(fixbug == True): fix_5_2_7()
		return False
	return True

def fix_5_2_7():
	helper.replaceLine('/etc/ssh/sshd_config', '^HostbasedAuthentication', 'HostbasedAuthentication no')

# 5.2.8 Ensure SSH root login is disabled
def task_5_2_8(fixbug=False):
	if (check_SSH_daemon_installed):
		check = os.popen('grep "^PermitRootLogin" /etc/ssh/sshd_config').read()

		if (check == 'PermitRootLogin no'):
			return True
		if(fixbug == True): fix_5_2_8()
		return False
	return True

def fix_5_2_8():
	helper.replaceLine('/etc/ssh/sshd_config', '^PermitRootLogin', 'PermitRootLogin no')

# 5.2.9 Ensure SSH PermitEmptyPasswords is disabled
def task_5_2_9(fixbug=False):
	if (check_SSH_daemon_installed):
		check = os.popen('grep "^PermitEmptyPasswords" /etc/ssh/sshd_config').read()

		if (check == 'PermitEmptyPasswords no'):
			return True
		if(fixbug == True): fix_5_2_9()
		return False
	return True

def fix_5_2_9():
	helper.replaceLine('/etc/ssh/sshd_config', '^PermitEmptyPasswords', 'PermitEmptyPasswords no')

# 5.2.10 Ensure SSH PermitUserEnvironment is disabled
def task_5_2_10(fixbug=False):
	if (check_SSH_daemon_installed):
		check = os.popen('grep "^PermitUserEnvironment" /etc/ssh/sshd_config').read()

		if (check == 'PermitUserEnvironment no'):
			return True
		if(fixbug == True): fix_5_2_10()
		return False
	return True

def fix_5_2_10():
	helper.replaceLine('/etc/ssh/sshd_config', '^PermitUserEnvironment', 'PermitUserEnvironment no')