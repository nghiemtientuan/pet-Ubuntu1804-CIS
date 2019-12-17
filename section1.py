import subprocess, os, re, sys
from crontab import CronTab
test_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(test_path)

import helper as helper

# 1 setting up
# 1.1 filesystem configuration
# 1.1.1 disable unused filesystems
# 1.1.1.1 ensure mounting of cramfs filesystems is disabled
def task_1_1_1_1(fixbug=False):
	install_cramfs = os.popen("modprobe -n -v cramfs").read()
	lsmod_cramfs = os.popen("lsmod | grep cramfs").read()

	if (re.search("install[a-zA-Z\s]+/bin/true", install_cramfs) and lsmod_cramfs == ''):
		return True
	if (fixbug == True): fix_1_1_1_1()
	return False

def fix_1_1_1_1():
	with open('/etc/modprobe.d/cramfs.conf', 'a+') as file:
		file.write('install cramfs /bin/true')
	os.popen("modprobe -r cramfs")

# 1.1.1.2 Ensure mounting of freevxfs filesystems is disabled
def task_1_1_1_2(fixbug=False):
	install_freevxfs = os.popen("modprobe -n -v freevxfs").read()
	lsmod_freevxfs = os.popen("lsmod | grep freevxfs").read()

	if (re.search("install[a-zA-Z\s]+/bin/true", install_freevxfs) and lsmod_freevxfs == ''):
		return True
	if (fixbug == True): fix_1_1_1_2()
	return False

def fix_1_1_1_2():
	with open('/etc/modprobe.d/freevxfs.conf', 'a+') as file:
		file.write('install freevxfs /bin/true')
	os.popen("modprobe -r freevxfs")

# 1.1.1.3 Ensure mounting of jffs2 filesystems is disabled
def task_1_1_1_3(fixbug=False):
	install_jffs2 = os.popen("modprobe -n -v jffs2").read()
	lsmod_jffs2 = os.popen("lsmod | grep jffs2").read()

	if (re.search("install[a-zA-Z\s]+/bin/true", install_jffs2) and lsmod_jffs2 == ''):
		return True
	if (fixbug == True): fix_1_1_1_3()
	return False

def fix_1_1_1_3():
	with open('/etc/modprobe.d/jffs2.conf', 'a+') as file:
		file.write('install jffs2 /bin/true')
	os.popen("modprobe -r jffs2")

# 1.1.1.4 Ensure mounting of hfs filesystems is disabled
def task_1_1_1_4(fixbug=False):
	install_hfs = os.popen("modprobe -n -v hfs").read()
	lsmod_hfs = os.popen("lsmod | grep hfs").read()

	if (re.search("install[a-zA-Z\s]+/bin/true", install_hfs) and lsmod_hfs == ''):
		return True
	if (fixbug == True): fix_1_1_1_4()
	return False

def fix_1_1_1_4():
	with open('/etc/modprobe.d/hfs.conf', 'a+') as file:
		file.write('install hfs /bin/true')
	os.popen("modprobe -r hfs")

# 1.1.1.5 Ensure mounting of hfsplus filesystems is disabled
def task_1_1_1_5(fixbug=False):
	install_hfsplus = os.popen("modprobe -n -v hfsplus").read()
	lsmod_hfsplus = os.popen("lsmod | grep hfsplus").read()

	if (re.search("install[a-zA-Z\s]+/bin/true", install_hfsplus) and lsmod_hfsplus == ''):
		return True
	if (fixbug == True): fix_1_1_1_5()
	return False

def fix_1_1_1_5():
	with open('/etc/modprobe.d/hfsplus.conf', 'a+') as file:
		file.write('install hfsplus /bin/true')
	os.popen("modprobe -r hfsplus")

# 1.1.1.6 Ensure mounting of udf filesystems is disabled
def task_1_1_1_6(fixbug=False):
	install_udf = os.popen("modprobe -n -v udf").read()
	lsmod_udf = os.popen("lsmod | grep udf").read()

	if (re.search("install[a-zA-Z\s]+/bin/true", install_udf) and lsmod_udf == ''):
		return True
	if (fixbug == True): fix_1_1_1_6()
	return False

def fix_1_1_1_6():
	with open('/etc/modprobe.d/udf.conf', 'a+') as file:
		file.write('install udf /bin/true')
	os.popen("modprobe -r udf")

# 1.1.2 Ensure separate partition exists for /tmp
def task_1_1_2(fixbug=False):
	try:
		exists_tmp = os.popen("ls -ld /tmp").read()

		if (re.search("/tmp", exists_tmp)):
			return True
		if (fixbug == True): fix_1_1_2()
		return False
	except OSError:
		return False

def fix_1_1_2():
	os.popen("sudo mkdir -m 1777 /tmp")

# 1.1.3 Ensure nodev option set on /tmp partition
def task_1_1_3(fixbug=False):
	mount_tmp = os.popen("mount | grep /tmp").read()

	if (re.search("nodev", mount_tmp)):
		return True
	if (fixbug == True): fix_1_1_3()
	return False

def fix_1_1_3():
	os.popen("sudo mount -o remount,nodev /tmp /var/tmp")

# 1.1.4 Ensure nosuid option set on /tmp partition
def task_1_1_4(fixbug=False):
	mount_tmp = os.popen("mount | grep /tmp").read()

	if (re.search("nosuid", mount_tmp)):
		return True
	if (fixbug == True): fix_1_1_4()
	return False

def fix_1_1_4():
	os.popen("sudo mount -o remount,nosuid /tmp /var/tmp")

# 1.1.5 Ensure separate partition exists for /var
def task_1_1_5(fixbug=False):
	try:
		exists_tmp = os.popen("ls -ld /var").read()

		if (re.search("/var", exists_tmp)):
			return True
		# show guide
		return False
	except OSError:
		return False

# 1.1.6 Ensure separate partition exists for /var/tmp
def task_1_1_6(fixbug=False):
	try:
		exists_var_tmp = os.popen("ls -ld /var/tmp").read()

		if (re.search("/var/tmp", exists_var_tmp)):
			return True
		# show guide
		return False
	except OSError:
		return False

# 1.1.7 Ensure nodev option set on /var/tmp partition
def task_1_1_7(fixbug=False):
	mount_var_tmp = os.popen("mount | grep /var/tmp").read()

	if (re.search("nodev", mount_var_tmp)):
		return True
	if (fixbug == True): fix_1_1_7()
	return False

def fix_1_1_7():
	os.popen("sudo mount -o remount,nodev /var/tmp")

# 1.1.8 Ensure nosuid option set on /var/tmp partition
def task_1_1_8(fixbug=False):
	mount_var_tmp = os.popen("mount | grep /var/tmp").read()

	if (re.search("nosuid", mount_var_tmp)):
		return True
	if (fixbug == True): fix_1_1_8()
	return False

def fix_1_1_8():
	os.popen("sudo mount -o remount,nosuid /var/tmp")

# 1.1.9 Ensure noexec option set on /var/tmp partition
def task_1_1_9(fixbug=False):
	mount_var_tmp = os.popen("mount | grep /var/tmp").read()

	if (re.search("noexec", mount_var_tmp)):
		return True
	if (fixbug == True): fix_1_1_9()
	return False

def fix_1_1_9():
	os.popen("sudo mount -o remount,noexec /var/tmp")

# 1.1.10 Ensure separate partition exists for /var/log
def task_1_1_10(fixbug=False):
	try:
		exists_var_log = os.popen("ls -ld /var/log").read()

		if (re.search("/var/log", exists_var_log)):
			return True
		# mkdir /var/log
		return False
	except OSError:
		return False

# 1.1.11 Ensure separate partition exists for /var/log/audit
def task_1_1_11(fixbug=False):
	try:
		exists_var_log_audit = os.popen("ls -ld /var/log/audit").read()
		if (re.search("/var/log/audit", exists_var_log_audit)):
			return True
		# show guide
		return False
	except OSError:
		return False

# 1.1.12 Ensure separate partition exists for /home
def task_1_1_12(fixbug=False):
	try:
		exists_var_log_audit = os.popen("ls -ld /home").read()

		if (re.search("/home", exists_var_log_audit)):
			return True
		# show guide
		return False
	except OSError:
		return False

# 1.1.13 Ensure nodev option set on /home partition
def task_1_1_13(fixbug=False):
	mount_home = os.popen("mount | grep /home").read()

	if (re.search("nodev", mount_home)):
		return True
	if (fixbug == True): fix_1_1_13()
	return False

def fix_1_1_13():
	os.popen("sudo mount -o remount,nodev /home")

# 1.1.14 Ensure nodev option set on /dev/shm partition
def task_1_1_14(fixbug=False):
	mount_dev_shm = os.popen("mount | grep /dev/shm").read()

	if (re.search("nodev", mount_dev_shm)):
		return True
	if (fixbug == True): fix_1_1_14()
	return False

def fix_1_1_14():
	os.popen("sudo mount -o remount,nodev /dev/shm")

# 1.1.15 Ensure nosuid option set on /dev/shm partition
def task_1_1_15(fixbug=False):
	mount_dev_shm = os.popen("mount | grep /dev/shm").read()

	if (re.search("nosuid", mount_dev_shm)):
		return True
	if (fixbug == True): fix_1_1_15()
	return False

def fix_1_1_15():
	os.popen("sudo mount -o remount,nosuid /dev/shm")

# 1.1.16 Ensure noexec option set on /dev/shm partition
def task_1_1_16(fixbug=False):
	mount_dev_shm = os.popen("mount | grep /dev/shm").read()

	if (re.search("noexec", mount_dev_shm)):
		return True
	if (fixbug == True): fix_1_1_16()

	return False

def fix_1_1_16():
	os.popen("sudo mount -o remount,noexec /dev/shm")

# 1.1.17 Ensure nodev option set on removable media partitions
def task_1_1_17(fixbug=False):
	check = helper.checkMountOptionSet('nodev')
	if (check == False):
		if (fixbug == True):
			helper.mountOptionSet('nodev')

		return False


	return True

# 1.1.18 Ensure nosuid option set on removable media partitions
def task_1_1_18(fixbug=False):
	check = helper.checkMountOptionSet('nosuid')
	if (check == False):
		if (fixbug == True):
			helper.mountOptionSet('nosuid')

		return False


	return True

# 1.1.19 Ensure noexec option set on removable media partitions
def task_1_1_19(fixbug=False):
	check = helper.checkMountOptionSet('noexec')
	if (check == False):
		if (fixbug == True):
			helper.mountOptionSet('noexec')

		return False


	return True

# 1.1.20 Ensure sticky bit is set on all world-writable directories
def task_1_1_20(fixbug=False):
	check = os.popen("df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -type d \( -perm -0002 -a ! -perm -1000 \) 2>/dev/null").read()

	if (check == ''):
		return True
	if (fixbug == True): fix_1_1_20()			
	return False

def fix_1_1_20():
	os.popen("df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -type d -perm -0002 2>/dev/null | xargs chmod a+t")

# 1.1.21 Disable Automounting
def task_1_1_21(fixbug=False):
	disable_automounting = os.popen("systemctl is-enabled autofs").read()

	if (re.search("enabled", disable_automounting)):
		if (fixbug == True): fix_1_1_21()			
		return False
	return True

def fix_1_1_21():
	os.popen("systemctl disable autofs")

# 1.2 Configure Software Updates (not scored)

# 1.3 Filesystem Integrity Checking
# 1.3.1 Ensure AIDE is installed
def task_1_3_1(fixbug=False):
	dpkg_AIDE = os.popen("dpkg -s aide").read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg_AIDE)):
		return True
	if (fixbug == True): fix_1_3_1()
	return False

def fix_1_3_1():
	os.popen("apt-get install aide aide-common -y")
	os.popen("aideinit")

# 1.3.2 Ensure filesystem integrity is regularly checked
def task_1_3_2(fixbug=False):
	crontab = os.popen("crontab -u root -l | grep aide").read()

	if (crontab == ''):
		if (fixbug == True): fix_1_3_2()
		return False
	return True

def fix_1_3_2():
	cron = CronTab(user=True)
	job = cron.new(command='/usr/bin/aide.wrapper --config /etc/aide/aide.conf --check')
	job.minute.on(0)
	job.hour.on(5)
	cron.write()

# 1.4 Secure Boot Settings
# 1.4.1 Ensure permissions on bootloader config are configured
def task_1_4_1(fixbug=False):
	stat = os.popen("stat /boot/grub/grub.cfg").read()

	if (re.search("Access:[\s]+\(0400/-r--------\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat)):
		return True
	if(fixbug == True): fix_1_4_1()
	return False

def fix_1_4_1():
	os.popen("chown root:root /boot/grub/grub.cfg")
	os.popen("chmod og-rwx /boot/grub/grub.cfg")

# 1.4.2 Ensure bootloader password is set
def task_1_4_2(fixbug=False):
	check = os.popen('grep "^set superusers" /boot/grub/grub.cfg').read()
	check2 = os.popen('grep "^password" /boot/grub/grub.cfg').read()

	if (re.search('set superusers=', check) and re.search('password_pbkdf2', check2)):
		return True
	# show huong dan tren giao dien
	return False

# 1.4.3 Ensure authentication required for single user mode
def task_1_4_3(fixbug=False):
	command = os.popen("grep ^root:[*\!]: /etc/shadow").read()

	if (command == ''):
		return True
	# show huong dan tren giao dien
	return False

def fix_1_4_3():
	os.popen("passwd root")

# 1.5 Additional Process Hardening
# 1.5.1 Ensure core dumps are restricted
def task_1_5_1(fixbug=False):
	command1 = os.popen('grep "hard core" /etc/security/limits.conf /etc/security/limits.d/*').read()
	command2 = os.popen('sysctl fs.suid_dumpable').read()
	command3 = os.popen('grep "fs.suid_dumpable" /etc/sysctl.conf /etc/sysctl.d/*').read()

	if (re.search("\* hard core 0", command1) and re.search("fs.suid_dumpable = 0", command2) and re.search("fs.suid_dumpable = 0", command3)):
		return True
	if (fixbug == True): fix_1_5_1();
	return False

def fix_1_5_1():
	helper.replaceLine('/etc/security/limits.conf', '\* hard core', '* hard core 0')
	helper.replaceLine('/etc/sysctl.conf', 'fs.suid_dumpable =', 'fs.suid_dumpable = 0')

	os.popen("sysctl -w fs.suid_dumpable=0")

# 1.5.2 Ensure XD/NX support is enabled
# 1.5.3 Ensure address space layout randomization (ASLR) is enabled
def task_1_5_3(fixbug=False):
	command1 = os.popen('sysctl kernel.randomize_va_space').read()
	command2 = os.popen('grep "kernel\.randomize_va_space" /etc/sysctl.conf /etc/sysctl.d/*').read()

	if (re.search("kernel.randomize_va_space = 2", command1) and re.search("kernel.randomize_va_space = 2", command2)):
		return True
	if (fixbug == True): fix_1_5_3();
	return False

def fix_1_5_3():
	helper.replaceLine('/etc/sysctl.conf', 'kernel.randomize_va_space =', 'kernel.randomize_va_space = 2')
	os.popen("sysctl -w kernel.randomize_va_space=2")

# 1.5.4 Ensure prelink is disabled
def task_1_5_4(fixbug=False):
	command = os.popen('dpkg -s prelink').read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", command)):
		if (fixbug == True): fix_1_5_4()
		return False
	return True

def fix_1_5_4():
	os.popen("prelink -ua")
	os.popen("apt-get remove prelink -y")

# 1.6 Mandatory Access Control
# 1.6.1 Configure SELinux
# 1.6.1.1 Ensure SELinux is not disabled in bootloader configuration
def task_1_6_1_1(fixbug=False):
	command = os.popen('grep "^\s*linux" /boot/grub/grub.cfg').read()

	if (re.search("selinux[\s]+=[\s]+0", command) and re.search("enforcing[\s]+=[\s]+0", command)):
		if (fixbug == True): fix_1_6_1_1()
		return False
	return True

def fix_1_6_1_1():
	helper.replaceLine('/etc/default/grub', 'GRUB_CMDLINE_LINUX_DEFAULT=', 'GRUB_CMDLINE_LINUX_DEFAULT="quiet"')
	helper.replaceLine('/etc/default/grub', 'GRUB_CMDLINE_LINUX=', 'GRUB_CMDLINE_LINUX=""')
	os.popen("update-grub")

# 1.6.1.2 Ensure the SELinux state is enforcing
def task_1_6_1_2(fixbug=False):
	command = os.popen('grep SELINUX=enforcing /etc/selinux/config').read()

	if (re.search("SELINUX=enforcing", command)):
		return True
	if (fixbug == True): fix_1_6_1_2()
	return False

def fix_1_6_1_2():
	helper.replaceLine('/etc/selinux/config', 'SELINUX=', 'SELINUX=enforcing')

# 1.6.1.3 Ensure SELinux policy is configured
def task_1_6_1_3(fixbug=False):
	command = os.popen('grep SELINUXTYPE= /etc/selinux/config').read()

	if (re.search("SELINUXTYPE=ubuntu", command) or re.search("SELINUXTYPE=default", command) or re.search("SELINUXTYPE=mls", command)):
		return True
	if (fixbug == True): fix_1_6_1_3()
	return False

def fix_1_6_1_3():
	helper.replaceLine('/etc/selinux/config', 'SELINUXTYPE=', 'SELINUXTYPE=ubuntu')

# 1.6.1.4 Ensure no unconfined daemons exist
def task_1_6_1_4(fixbug=False):
	command = os.popen('ps -eZ | egrep "initrc" | egrep -vw "tr|ps|egrep|bash|awk" | tr \':\' \' \' | awk \'{ print $NF }\'').read()
	
	if (command == ''):
		return True
	# show guide
	return False

# 1.6.2 Configure AppArmor
# 1.6.2.1 Ensure AppArmor is not disabled in bootloader configuration
def task_1_6_2_1(fixbug=False):
	command = os.popen('grep "^\s*linux" /boot/grub/grub.cfg').read()

	if (re.search("apparmor=0", command) and re.search("enforcing[\s]+=[\s]+0", command)):
		if (fixbug == True): fix_1_6_2_1()
		return False
	return True

def fix_1_6_2_1():
	helper.replaceLine('/etc/default/grub', 'GRUB_CMDLINE_LINUX_DEFAULT=', 'GRUB_CMDLINE_LINUX_DEFAULT="quiet"')
	helper.replaceLine('/etc/default/grub', 'GRUB_CMDLINE_LINUX=', 'GRUB_CMDLINE_LINUX=""')
	os.popen("update-grub")

# 1.6.2.2 Ensure all AppArmor Profiles are enforcing
def task_1_6_2_2(fixbug=False):
	command = os.popen('apparmor_status').read()

	if (re.search("0 profiles are in complain mode", command) and re.search("0 processes are unconfined", command)):
		return True
	if (fixbug == True): fix_1_6_2_2()
	return False

def fix_1_6_2_2():
	os.popen("aa-enforce /etc/apparmor.d/*")

# 1.6.3 Ensure SELinux or AppArmor are installed
def task_1_6_3(fixbug=False):
	dpkg_selinux = os.popen("dpkg -s selinux").read()
	dpkg_apparmor = os.popen("dpkg -s apparmor").read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg_selinux) and re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg_apparmor)):
		return True
	if (fixbug == True): fix_1_6_3()
	return False

def fix_1_6_3():
	os.popen("apt-get install selinux -y")
	os.popen("apt-get install apparmor -y")

# 1.7 Warning Banners
# 1.7.1 Command Line Warning Banners
# 1.7.1.1 Ensure message of the day is configured properly
def task_1_7_1_1(fixbug=False):
	command_egrep = os.popen('egrep \'(\\v|\\r|\\m|\\s)\' /etc/motd').read()

	if (command_egrep == ''):
		return True
	if (fixbug == True): fix_1_7_1_1()
	return False

def fix_1_7_1_1():
	helper.removeStringInLine('/etc/motd', '\\m')
	helper.removeStringInLine('/etc/motd', '\\r')
	helper.removeStringInLine('/etc/motd', '\\s')
	helper.removeStringInLine('/etc/motd', '\\v')


# 1.7.1.2 Ensure local login warning banner is configured properly
def task_1_7_1_2(fixbug=False):
	command_egrep = os.popen('egrep \'(\\v|\\r|\\m|\\s)\' /etc/issue').read()

	if (command_egrep == ''):
		return True
	if (fixbug == True): fix_1_7_1_2()
	return False

def fix_1_7_1_2():
	helper.removeStringInLine('/etc/issue', '\\m')
	helper.removeStringInLine('/etc/issue', '\\r')
	helper.removeStringInLine('/etc/issue', '\\s')
	helper.removeStringInLine('/etc/issue', '\\v')

# 1.7.1.3 Ensure remote login warning banner is configured properly
def task_1_7_1_3(fixbug=False):
	command_egrep = os.popen('egrep \'(\\v|\\r|\\m|\\s)\' /etc/issue.net').read()

	if (command_egrep == ''):
		return True
	if (fixbug == True): fix_1_7_1_3()
	return False

def fix_1_7_1_3():
	helper.removeStringInLine('/etc/issue.net', '\\m')
	helper.removeStringInLine('/etc/issue.net', '\\r')
	helper.removeStringInLine('/etc/issue.net', '\\s')
	helper.removeStringInLine('/etc/issue.net', '\\v')

# 1.7.1.4 Ensure permissions on /etc/motd are configured
def task_1_7_1_4(fixbug=False):
	stat = os.popen('stat /etc/motd').read()

	if (re.search("Access:[\s]+\(0644/-rw-r--r--\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat)):
		return True
	if (fixbug == True): fix_1_7_1_4()
	return False

def fix_1_7_1_4():
	os.popen("chown root:root /etc/motd")
	os.popen("chmod 644 /etc/motd")

# 1.7.1.5 Ensure permissions on /etc/issue are configured
def task_1_7_1_5(fixbug=False):
	stat = os.popen('stat /etc/issue').read()

	if (re.search("Access:[\s]+\(0644/-rw-r--r--\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat)):
		return True
	if (fixbug == True): fix_1_7_1_5()
	return False

def fix_1_7_1_5():
	os.popen("chown root:root /etc/issue")
	os.popen("chmod 644 /etc/issue")

# 1.7.1.6 Ensure permissions on /etc/issue.net are configured
def task_1_7_1_6(fixbug=False):
	stat = os.popen('stat /etc/issue.net').read()

	if (re.search("Access:[\s]+\(0644/-rw-r--r--\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat)):
		return True
	if (fixbug == True): fix_1_7_1_6()
	return False

def fix_1_7_1_6():
	os.popen("chown root:root /etc/issue.net")
	os.popen("chmod 644 /etc/issue.net")

# 1.7.2 Ensure GDM login banner is configured
def task_1_7_2(fixbug=False):
	dpkg = os.popen("dpkg -s gdm3").read()

	if (re.search("Status[a-zA-Z\s:]+install[a-zA-Z\s]+ok[a-zA-Z\s]+installed", dpkg)):
		check = os.popen('grep banner-message-enable /etc/gdm3/greeter.dconf-defaults').read()

		if (check == 'banner-message-enable=true'):
			return True
		if (fixbug == True): fix_1_7_2()

		return False
	return True

def fix_1_7_2():
	helper.replaceLine('/etc/gdm3/greeter.dconf-defaults', 'banner-message-enable=', 'banner-message-enable=true')

	check = os.popen('grep banner-message-text /etc/gdm3/greeter.dconf-defaults').read()
	if (check == '' and not re.search("^[^#]?banner-message-text", check)):
		helper.replaceLine('/etc/gdm3/greeter.dconf-defaults', 'banner-message-text=', "banner-message-text='Authorized uses only. All activity may be monitored and reported.'")