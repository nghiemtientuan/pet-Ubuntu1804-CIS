import subprocess, os, re, sys
test_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(test_path)

import helper as helper

# 6 System Maintenance
# 6.1 System File Permissions
# 6.1.2 Ensure permissions on /etc/passwd are configured
def task_6_1_2(fixbug=False):
	stat = os.popen("stat /etc/passwd").read()

	if (re.search("Access:[\s]+\(0644/-rw-r--r--\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat)):
		return True
	if(fixbug == True): fix_6_1_2()
	return False

def fix_6_1_2():
	os.popen("chown root:root /etc/passwd")
	os.popen("chmod 644 /etc/passwd")

# 6.1.3 Ensure permissions on /etc/shadow are configured
def task_6_1_3(fixbug=False):
	stat = os.popen("stat /etc/shadow").read()

	if (re.search("Access:[\s]+\(0640/-rw-r-----\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+42/[\s]+shadow\)", stat)):
		return True
	if(fixbug == True): fix_6_1_3()
	return False

def fix_6_1_3():
	os.popen("chown root:shadow /etc/shadow")
	os.popen("chmod o-rwx,g-wx /etc/shadow")

# 6.1.4 Ensure permissions on /etc/group are configured
def task_6_1_4(fixbug=False):
	stat = os.popen("stat /etc/group").read()

	if (re.search("Access:[\s]+\(0644/-rw-r--r--\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat)):
		return True
	if(fixbug == True): fix_6_1_4()
	return False

def fix_6_1_4():
	os.popen("chown root:root /etc/group")
	os.popen("chmod 644 /etc/group")

# 6.1.5 Ensure permissions on /etc/gshadow are configured
def task_6_1_5(fixbug=False):
	stat = os.popen("stat /etc/gshadow").read()

	if (re.search("Access:[\s]+\(0640/-rw-r-----\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+42/[\s]+shadow\)", stat)):
		return True
	if(fixbug == True): fix_6_1_5()
	return False

def fix_6_1_5():
	os.popen("chown root:shadow /etc/gshadow")
	os.popen("chmod o-rwx,g-rw /etc/gshadow")

# 6.1.6 Ensure permissions on /etc/passwd- are configured
def task_6_1_6(fixbug=False):
	stat = os.popen("stat /etc/passwd-").read()

	if (re.search("Access:[\s]+\(0644/-rw-r--r--\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat)):
		return True
	if(fixbug == True): fix_6_1_6()
	return False

def fix_6_1_6():
	os.popen("chown root:root /etc/passwd-")
	os.popen("chmod u-x,go-wx /etc/passwd-")

# 6.1.7 Ensure permissions on /etc/shadow- are configured
def task_6_1_7(fixbug=False):
	stat = os.popen("stat /etc/shadow-").read()

	if (re.search("Access:[\s]+\(0640/-rw-r-----\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+42/[\s]+shadow\)", stat)):
		return True
	if(fixbug == True): fix_6_1_7()
	return False

def fix_6_1_7():
	os.popen("chown root:shadow /etc/shadow-")
	os.popen("chmod o-rwx,g-rw /etc/shadow-")

# 6.1.8 Ensure permissions on /etc/group- are configured
def task_6_1_8(fixbug=False):
	stat = os.popen("stat /etc/group-").read()

	if (re.search("Access:[\s]+\(0644/-rw-r--r--\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+0/[\s]+root\)", stat)):
		return True
	if(fixbug == True): fix_6_1_8()
	return False

def fix_6_1_8():
	os.popen("chown root:root /etc/group-")
	os.popen("chmod u-x,go-wx /etc/group-")

# 6.1.9 Ensure permissions on /etc/gshadow- are configured
def task_6_1_9(fixbug=False):
	stat = os.popen("stat /etc/gshadow-").read()

	if (re.search("Access:[\s]+\(0640/-rw-r-----\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+42/[\s]+shadow\)", stat)):
		return True
	if(fixbug == True): fix_6_1_9()
	return False

def fix_6_1_9():
	os.popen("chown root:shadow /etc/gshadow-")
	os.popen("chmod o-rwx,g-rw /etc/gshadow-")
