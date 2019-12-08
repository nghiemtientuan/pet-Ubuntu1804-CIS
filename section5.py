import subprocess, os, re, sys
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
	return False

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

# 5.2.11 Ensure only approved MAC algorithms are used
def task_5_2_11(fixbug=False):
	if (check_SSH_daemon_installed):
		check = os.popen('grep "MACs" /etc/ssh/sshd_config').read()

		if (check == 'MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512,hmac-sha2-256,umac-128@openssh.com'):
			return True
		if(fixbug == True): fix_5_2_11()
		return False
	return True

def fix_5_2_11():
 	helper.replaceLine('/etc/ssh/sshd_config', 'MACs', 'MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512,hmac-sha2-256,umac-128@openssh.com')

# 5.2.12 Ensure SSH Idle Timeout Interval is configured
def task_5_2_12(fixbug=False):
	if (check_SSH_daemon_installed):
		check = os.popen('grep "^ClientAliveInterval" /etc/ssh/sshd_config').read()
		check2 = os.popen('grep "^ClientAliveCountMax" /etc/ssh/sshd_config').read()

		if (check == 'ClientAliveInterval 300' and check2 == 'ClientAliveCountMax 0'):
			return True
		if(fixbug == True): fix_5_2_12()
		return False
	return True

def fix_5_2_12():
	helper.replaceLine('/etc/ssh/sshd_config', '^ClientAliveInterval', 'ClientAliveInterval 300')
	helper.replaceLine('/etc/ssh/sshd_config', '^ClientAliveCountMax', 'ClientAliveCountMax 0')

# 5.2.13 Ensure SSH LoginGraceTime is set to one minute or less
def task_5_2_13(fixbug=False):
	if (check_SSH_daemon_installed):
		check = os.popen('grep "^LoginGraceTime" /etc/ssh/sshd_config').read()

		if (check == 'LoginGraceTime 60'):
			return True
		if(fixbug == True): fix_5_2_13()
		return False
	return True

def fix_5_2_13():
	helper.replaceLine('/etc/ssh/sshd_config', '^LoginGraceTime', 'LoginGraceTime 60')

# 5.2.15 Ensure SSH warning banner is configured
def task_5_2_15(fixbug=False):
	if (check_SSH_daemon_installed):
		check = os.popen('grep "^Banner" /etc/ssh/sshd_config').read()

		if (check == 'LoginGraceTime 60'):
			return True
		if(fixbug == True): fix_5_2_15()
		return False
	return True

def fix_5_2_15():
	helper.replaceLine('/etc/ssh/sshd_config', '^Banner', 'Banner /etc/issue.net')

# 5.3 Configure PAM
# 5.3.1 Ensure password creation requirements are configured
def task_5_3_1(fixbug=False):
	check = os.popen('grep pam_pwquality.so /etc/pam.d/common-password').read()
	check2 = os.popen('grep ^minlen /etc/security/pwquality.conf').read()
	check3 = os.popen('grep ^dcredit /etc/security/pwquality.conf').read()
	check4 = os.popen('grep ^lcredit /etc/security/pwquality.conf').read()
	check5 = os.popen('grep ^ocredit /etc/security/pwquality.conf').read()
	check6 = os.popen('grep ^ucredit /etc/security/pwquality.conf').read()

	if (check == 'password requisite pam_pwquality.so retry=3' and check2 == 'minlen = 14' and check3 == 'dcredit = -1' and check4 == 'lcredit = -1' and check5 == 'ocredit = -1' and check6 == 'ucredit = -1'):
		return True
	if(fixbug == True): fix_5_3_1()
	return False

def fix_5_3_1():
	os.popen("apt-get install libpam-pwquality -y")
	helper.replaceLine('/etc/pam.d/common-password', 'pam_pwquality.so', 'password requisite pam_pwquality.so retry=3')
	helper.replaceLine('/etc/security/pwquality.conf', '^minlen', 'minlen = 14')
	helper.replaceLine('/etc/security/pwquality.conf', '^dcredit', 'dcredit = -1')
	helper.replaceLine('/etc/security/pwquality.conf', '^lcredit', 'ucredit = -1')
	helper.replaceLine('/etc/security/pwquality.conf', '^ocredit', 'ocredit = -1')
	helper.replaceLine('/etc/security/pwquality.conf', '^ucredit', 'ocredit = -1')

# 5.3.2 Ensure lockout for failed password attempts is configured
def task_5_3_2(fixbug=False):
	check = os.popen('grep "pam_tally2" /etc/pam.d/common-auth').read()

	if (check == 'auth required pam_tally2.so onerr=fail audit silent deny=5 unlock_time=900'):
		return True
	if(fixbug == True): fix_5_3_2()
	return False

def fix_5_3_2():
	helper.replaceLine('/etc/pam.d/common-auth', 'pam_tally2', 'auth required pam_tally2.so onerr=fail audit silent deny=5 unlock_time=900')

# 5.3.3 Ensure password reuse is limited
def task_5_3_3(fixbug=False):
	check = os.popen("egrep '^password\s+required\s+pam_pwhistory.so' /etc/pam.d/common-password").read()

	if (check == 'password required pam_pwhistory.so remember=5'):
		return True
	if(fixbug == True): fix_5_3_3()
	return False

def fix_5_3_3():
	helper.replaceLine('/etc/pam.d/common-password', '^password\s+required\s+pam_pwhistory.so', 'password required pam_pwhistory.so remember=5')

# 5.3.4 Ensure password hashing algorithm is SHA-512
def task_5_3_4(fixbug=False):
	check = os.popen("egrep '^password\s+(\S+\s+)+pam_unix\.so\s+(\S+\s+)*sha512' /etc/pam.d/common-password").read()

	if (check == 'password [success=1 default=ignore] pam_unix.so sha512'):
		return True
	if(fixbug == True): fix_5_3_4()
	return False

def fix_5_3_4():
	helper.replaceLine('/etc/pam.d/common-password', '^password\s+(\S+\s+)+pam_unix\.so\s+(\S+\s+)*sha512', 'password [success=1 default=ignore] pam_unix.so sha512')

# 5.4 User Accounts and Environment
# 5.4.1 Set Shadow Password Suite Parameters
# 5.4.1.1 Ensure password expiration is 365 days or less

# 5.4.2 Ensure system accounts are non-login
def task_5_4_2(fixbug=False):
	check = os.popen("""egrep -v "^\+" /etc/passwd | awk -F: '($1!="root" && $1!="sync" && $1!="shutdown" && $1!="halt" && $3<1000 && $7!="/usr/sbin/nologin" && $7!="/bin/false") {print}'""").read()
	check2 = os.popen("""for user in `awk -F: '($1!="root" && $3 < 1000) {print $1 }' /etc/passwd`; do passwd -S $user | awk -F ' ' '($2!="L") {print $1}'; done""").read()

	if (check == '' and check2 == ''):
		return True
	#if(fixbug == True): fix_5_4_2()
	return False

# 5.4.3 Ensure default group for the root account is GID 0
def task_5_4_3(fixbug=False):
	check = os.popen('grep "^root:" /etc/passwd | cut -f4 -d:').read()

	if (check == 0):
		return True
	if(fixbug == True): fix_5_4_3()
	return False

def fix_5_4_3():
	os.popen("usermod -g 0 root")

# 5.4.4 Ensure default user umask is 027 or more restrictive
def task_5_4_4(fixbug=False):
	check = os.popen('grep "umask" /etc/bash.bashrc').read()
	check2 = os.popen('grep "umask" /etc/profile /etc/profile.d/*.sh').read()

	if (check == 'umask 027' and check2 == 'umask 027'):
		return True
	if(fixbug == True): fix_5_4_4()
	return False

def fix_5_4_4():
	helper.replaceLine('/etc/bash.bashrc', 'umask', 'umask 027')

# 5.4.5 Ensure default user shell timeout is 900 seconds or less
def task_5_4_5(fixbug=False):
	check = os.popen('grep "^TMOUT" /etc/bash.bashrc').read()
	check2 = os.popen('grep "^TMOUT" /etc/profile /etc/profile.d/*.sh').read()

	if (check == 'TMOUT=600' and check2 == 'TMOUT=600'):
		return True
	if(fixbug == True): fix_5_4_5()
	return False

def fix_5_4_5():
	helper.replaceLine('/etc/bash.bashrc', 'TMOUT', 'TMOUT=600')

# 5.5 Ensure root login is restricted to system console
# 5.6 Ensure access to the su command is restricted
def task_5_6(fixbug=False):
	check = os.popen('grep pam_wheel.so /etc/pam.d/su').read()
	check2 = os.popen('grep sudo /etc/group').read()

	if (check == 'auth required pam_wheel.so' and check2 == 'sudo:x:10:root,<user list>'):
		return True
	if(fixbug == True): fix_5_6()
	return False

def fix_5_6():
	helper.replaceLine('/etc/pam.d/su', 'pam_wheel.so', 'auth required pam_wheel.so')
	helper.replaceLine('/etc/group', 'sudo', 'sudo:x:10:root,<user list>')