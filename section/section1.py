import os, re

"""1 setting up"""
# 1.1 filesystem configuration
# 1.1.1 disable unused filesystems

# 1.1.1.1 ensure mounting of cramfs filesystems is disabled
def ensure_mounting_of_cramfs():
	install_cramfs = os.popen("modprobe -n -v cramfs").read()
	lsmod_cramfs = os.popen("lsmod | grep cramfs").read()

	if (re.search("install /bin/true", install_cramfs) and lsmod_cramfs == ''):
		return True
	return False

def unload_the_cramfs():
	with open('/etc/modprobe.d/cramfs.conf', 'a+') as file:
		file.write('install cramfs /bin/true')
	os.popen("modprobe -r cramfs")

# 1.1.1.2 Ensure mounting of freevxfs filesystems is disabled
def ensure_mounting_of_freevxfs():
	install_freevxfs = os.popen("modprobe -n -v freevxfs").read()
	lsmod_freevxfs = os.popen("lsmod | grep freevxfs").read()

	if (re.search("install /bin/true", install_freevxfs) and lsmod_freevxfs == ''):
		return True
	return False

def unload_the_freevxfs():
	with open('/etc/modprobe.d/freevxfs.conf', 'a+') as file:
		file.write('install freevxfs /bin/true')
	os.popen("modprobe -r freevxfs")

# 1.1.1.3 Ensure mounting of jffs2 filesystems is disabled
def ensure_mounting_of_jffs2():
	install_jffs2 = os.popen("modprobe -n -v jffs2").read()
	lsmod_jffs2 = os.popen("lsmod | grep jffs2").read()

	if (re.search("install /bin/true", install_jffs2) and lsmod_jffs2 == ''):
		return True
	return False

def unload_the_jffs2():
	with open('/etc/modprobe.d/jffs2.conf', 'a+') as file:
		file.write('install jffs2 /bin/true')
	os.popen("modprobe -r jffs2")

# 1.1.1.4 Ensure mounting of hfs filesystems is disabled
def ensure_mounting_of_hfs():
	install_hfs = os.popen("modprobe -n -v hfs").read()
	lsmod_hfs = os.popen("lsmod | grep hfs").read()

	if (re.search("install /bin/true", install_hfs) and lsmod_hfs == ''):
		return True
	return False

def unload_the_hfs():
	with open('/etc/modprobe.d/hfs.conf', 'a+') as file:
		file.write('install hfs /bin/true')
	os.popen("modprobe -r hfs")

# 1.1.1.5 Ensure mounting of hfsplus filesystems is disabled
def ensure_mounting_of_hfsplus():
	install_hfsplus = os.popen("modprobe -n -v hfsplus").read()
	lsmod_hfsplus = os.popen("lsmod | grep hfsplus").read()

	if (re.search("install /bin/true", install_hfsplus) and lsmod_hfsplus == ''):
		return True
	return False

def unload_the_hfsplus():
	with open('/etc/modprobe.d/hfsplus.conf', 'a+') as file:
		file.write('install hfsplus /bin/true')
	os.popen("modprobe -r hfsplus")

# 1.1.1.6 Ensure mounting of udf filesystems is disabled
def ensure_mounting_of_udf():
	install_udf = os.popen("modprobe -n -v udf").read()
	lsmod_udf = os.popen("lsmod | grep udf").read()

	if (re.search("install /bin/true", install_udf) and lsmod_udf == ''):
		return True
	return False

def unload_the_udf():
	with open('/etc/modprobe.d/udf.conf', 'a+') as file:
		file.write('install udf /bin/true')
	os.popen("modprobe -r udf")


# 1.1.2 Ensure separate partition exists for /tmp
def ensure_separate_partition_exists_tmp():
	exists_tmp = os.popen("ls -ld /tmp").read()

	if (re.search("/tmp", exists_tmp)):
		return True
	# mkdir_tmp()
	return False

def mkdir_tmp():
	os.popen("sudo mkdir -m 1777 /tmp")

# 1.1.3 Ensure nodev option set on /tmp partition
def ensure_separate_partition_tmp_nodev():
	mount_tmp = os.popen("mount | grep /tmp").read()

	if (re.search("nodev", mount_tmp)):
		return True
	return False

def set_nodev_nosuid_option_tmp_nodev():
	os.popen("sudo mount -o remount,nodev /tmp /var/tmp")

# 1.1.4 Ensure nosuid option set on /tmp partition
def ensure_separate_partition_tmp_nosuid():
	mount_tmp = os.popen("mount | grep /tmp").read()

	if (re.search("nosuid", mount_tmp)):
		return True
	return False

def set_nodev_nosuid_option_tmp_nosuid():
	os.popen("sudo mount -o remount,nosuid /tmp /var/tmp")

# 1.1.5 Ensure separate partition exists for /var
def ensure_separate_partition_exists_var():
	exists_tmp = os.popen("ls -ld /var").read()

	if (re.search("/var", exists_tmp)):
		return True
	# mkdir_var()
	return False

# 1.1.6 Ensure separate partition exists for /var/tmp
def ensure_separate_partition_exists_var_tmp():
	exists_var_tmp = os.popen("ls -ld /var/tmp").read()

	if (re.search("/var/tmp", exists_var_tmp)):
		return True
	return False

# 1.1.7 Ensure nodev option set on /var/tmp partition
def ensure_separate_partition_var_tmp_nodev():
	mount_var_tmp = os.popen("mount | grep /var/tmp").read()

	if (re.search("nodev", mount_var_tmp)):
		return True
	return False

def set_nodev_nosuid_option_var_tmp_nodev():
	os.popen("sudo mount -o remount,nodev /var/tmp")

# 1.1.8 Ensure nosuid option set on /var/tmp partition
def ensure_separate_partition_var_tmp_nosuid():
	mount_var_tmp = os.popen("mount | grep /var/tmp").read()

	if (re.search("nosuid", mount_var_tmp)):
		return True
	return False

def set_nodev_nosuid_option_var_tmp_nosuid():
	os.popen("sudo mount -o remount,nosuid /var/tmp")

# 1.1.9 Ensure noexec option set on /var/tmp partition
def ensure_separate_partition_var_tmp():
	mount_var_tmp = os.popen("mount | grep /var/tmp").read()

	if (re.search("noexec", mount_var_tmp)):
		return True
	return False

def set_nodev_nosuid_option_var_tmp():
	os.popen("sudo mount -o remount,noexec /var/tmp")

# 1.1.10 Ensure separate partition exists for /var/log
