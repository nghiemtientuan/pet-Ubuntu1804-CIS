import subprocess, os, re
from crontab import CronTab

#p = subprocess.Popen('modprobe -n -v cramfs', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	#for line in p.stdout.readlines():
    #	print line,

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
		# mkdir_var()
		return False
	except OSError:
		return False

# 1.1.6 Ensure separate partition exists for /var/tmp
def task_1_1_6(fixbug=False):
	try:
		exists_var_tmp = os.popen("ls -ld /var/tmp").read()

		if (re.search("/var/tmp", exists_var_tmp)):
			return True
		# mkdir /var/tmp
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
		# mkdir /var/log/audit
		return False
	except OSError:
		return False

# 1.1.12 Ensure separate partition exists for /home
def task_1_1_12(fixbug=False):
	try:
		exists_var_log_audit = os.popen("ls -ld /home").read()

		if (re.search("/home", exists_var_log_audit)):
			return True
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
# 1.1.18 Ensure nosuid option set on removable media partitions
# 1.1.19 Ensure noexec option set on removable media partitions
# 1.1.20 Ensure sticky bit is set on all world-writable directories

# 1.1.21 Disable Automounting
def task_1_1_21(fixbug=False):
	disable_automounting = os.popen("systemctl is-enabled autofs").read()

	if (re.search("enabled", disable_automounting)):
		if(fixbug == True): fix_1_1_21()			
		return False
	return True

def fix_1_1_21():
	os.popen("systemctl disable autofs")

# 1.2 Configure Software Updates

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
# 1.4.3 Ensure authentication required for single user mode
# def task_1_4_3(fixbug=False):
# 	command = os.popen("grep ^root:[*\!]: /etc/shadow").read()

# 	if (command == ''):
# 		return True
# 	if (fixbug == True): fix_1_4_3()
# 	return False

# def fix_1_4_3():
# 	os.popen("passwd root")

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
	if (not checkContentFile('* hard core 0', '/etc/security/limits.conf')):
		with open('/etc/security/limits.conf', 'a+') as file:
			file.write('* hard core 0')

	if (not checkContentFile('fs.suid_dumpable = 0', '/etc/sysctl.conf')):
		with open('/etc/sysctl.conf', 'a+') as file:
			file.write('fs.suid_dumpable = 0')

	os.popen("sysctl -w fs.suid_dumpable=0")

def checkContentFile(string, base):
	found = False
	with open(base, 'a+') as file:
		lineList = file.read()
		if (string in lineList):
			found = True

	return found

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
	if (not checkContentFile('kernel.randomize_va_space = 2', '/etc/sysctl.conf')):
		with open('/etc/sysctl.conf', 'a+') as file:
			file.write('kernel.randomize_va_space = 2')

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
def task_1_6_1_1(fixbug=True):
	command = os.popen('grep "^\s*linux" /boot/grub/grub.cfg').read()

	if (re.search("selinux=0", command) and re.search("enforcing=0", command)):
		if (fixbug == True): fix_1_5_4()
		return False
	return True

def fix_1_6_1_1():
	os.popen("update-grub")

print task_1_6_1_1()