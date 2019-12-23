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

	if (re.search("Access:[\s]+\(0640/-rw-r-----\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+[0-9]+/[\s]+shadow\)", stat)):
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

	if (re.search("Access:[\s]+\(0640/-rw-r-----\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+[0-9]+/[\s]+shadow\)", stat)):
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

	if (re.search("Access:[\s]+\(0640/-rw-r-----\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+[0-9]+/[\s]+shadow\)", stat)):
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

	if (re.search("Access:[\s]+\(0640/-rw-r-----\)[\s]+Uid: \([\s]+0/[\s]+root\)[\s]+Gid:[\s]+\([\s]+[0-9]+/[\s]+shadow\)", stat)):
		return True
	if(fixbug == True): fix_6_1_9()
	return False

def fix_6_1_9():
	os.popen("chown root:shadow /etc/gshadow-")
	os.popen("chmod o-rwx,g-rw /etc/gshadow-")

# 6.1.10 Ensure no world writable files exist
def task_6_1_10(fixbug=False):
	command = 'df --local -P | awk {\'if (NR!=1) print $6\'} | xargs -I \'{}\' find \'{}\' -xdev -type f -perm -0002'
	check = os.popen(command).read()
	if (check == ''):
		return True
	else:
		if(fixbug == True):
			check = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			for line in check.stdout.readlines():
				if (line):
					os.popen("chmod o-w " + line)

		return False

# 6.1.11 Ensure no unowned files or directories exist
def task_6_1_11(fixbug=False):
	command = 'df --local -P | awk {\'if (NR!=1) print $6\'} | xargs -I \'{}\' find \'{}\' -xdev -nouser'
	check = os.popen(command).read()
	if (check == ''):
		return True
	else:
		return False

# 6.1.12 Ensure no ungrouped files or directories exist
def task_6_1_12(fixbug=False):
	command = 'df --local -P | awk {\'if (NR!=1) print $6\'} | xargs -I \'{}\' find \'{}\' -xdev -nogroup'
	check = os.popen(command).read()
	if (check == ''):
		return True
	else:
		return False

# 6.1.13 Audit SUID executables
def task_6_1_13(fixbug=False):
	command = 'df --local -P | awk {\'if (NR!=1) print $6\'} | xargs -I \'{}\' find \'{}\' -xdev -type f -perm -4000'
	check = os.popen(command).read()
	if (check == ''):
		return True
	else:
		return False

# 6.1.14 Audit SGID executables
def task_6_1_14(fixbug=False):
	command = 'df --local -P | awk {\'if (NR!=1) print $6\'} | xargs -I \'{}\' find \'{}\' -xdev -type f -perm -2000'
	check = os.popen(command).read()
	if (check == ''):
		return True
	else:
		return False

# 6.2 User and Group Settings
# 6.2.1 Ensure password fields are not empty
def task_6_2_1(fixbug=False):
	command = 'cat /etc/shadow | awk -F: \'($2 == "" ) { print $1 " does not have a password "}\''
	check = os.popen(command).read()
	if (check == ''):
		return True
	else:
		return False

# 6.2.2 Ensure no legacy "+" entries exist in /etc/passwd
def task_6_2_2(fixbug=False):
	check = os.popen('grep \'^\\+:\' /etc/passwd').read()
	if (check == ''):
		return True
	else:
		return False

# 6.2.3 Ensure no legacy "+" entries exist in /etc/shadow
def task_6_2_3(fixbug=False):
	check = os.popen('grep \'^\\+:\' /etc/shadow').read()
	if (check == ''):
		return True
	else:
		return False

# 6.2.4 Ensure no legacy "+" entries exist in /etc/group
def task_6_2_4(fixbug=False):
	check = os.popen('grep \'^\\+:\' /etc/group').read()
	if (check == ''):
		return True
	else:
		return False

# 6.2.5 Ensure root is the only UID 0 account
def task_6_2_5(fixbug=False):
	check, after = os.popen('cat /etc/passwd | awk -F: \'($3 == 0) { print $1 }\'').read().split('\n')

	if (check == 'root'):
		return True
	else:
		return False

# 6.2.6 Ensure root PATH Integrity
def task_6_2_6(fixbug=False):
	check = os.popen('scripts/script_6_2_6').read()

	if (check == ''):
		return True
	else:
		return False

# 6.2.7 Ensure all users' home directories exist
def task_6_2_7(fixbug=False):
	check = os.popen('scripts/script_6_2_7').read()

	if (check == ''):
		return True
	else:
		return False

# 6.2.8 Ensure users' home directories permissions are 750 or more restrictive
def task_6_2_8(fixbug=False):
	check = os.popen('scripts/script_6_2_8').read()

	if (check == ''):
		return True
	else:
		return False

# 6.2.9 Ensure users own their home directories
def task_6_2_9(fixbug=False):
	check = os.popen('scripts/script_6_2_9').read()

	if (check == ''):
		return True
	else:
		return False

# 6.2.10 Ensure users' dot files are not group or world writable
def task_6_2_10(fixbug=False):
	check = os.popen('scripts/script_6_2_10').read()

	if (check == ''):
		return True
	else:
		return False

# 6.2.11 Ensure no users have .forward files
def task_6_2_11(fixbug=False):
	check = os.popen('scripts/script_6_2_11').read()

	if (check == ''):
		return True
	else:
		return False

# 6.2.12 Ensure no users have .netrc files
def task_6_2_12(fixbug=False):
	check = os.popen('scripts/script_6_2_12').read()

	if (check == ''):
		return True
	else:
		return False

# 6.2.13 Ensure users' .netrc Files are not group or world accessible
def task_6_2_13(fixbug=False):
	check = os.popen('scripts/script_6_2_13').read()

	if (check == ''):
		return True
	else:
		return False

# 6.2.14 Ensure no users have .rhosts files
def task_6_2_14(fixbug=False):
	check = os.popen('scripts/script_6_2_14').read()

	if (check == ''):
		return True
	else:
		return False

# 6.2.15 Ensure all groups in /etc/passwd exist in /etc/group
def task_6_2_15(fixbug=False):
	check = os.popen('scripts/script_6_2_15').read()

	if (check == ''):
		return True
	else:
		return False

# 6.2.16 Ensure no duplicate UIDs exist
def task_6_2_16(fixbug=False):
	check = os.popen('scripts/script_6_2_16').read()

	if (check == ''):
		return True
	else:
		return False

# 6.2.17 Ensure no duplicate GIDs exist
def task_6_2_17(fixbug=False):
	check = os.popen('scripts/script_6_2_17').read()

	if (check == ''):
		return True
	else:
		return False

# 6.2.18 Ensure no duplicate user names exist
def task_6_2_18(fixbug=False):
	check = os.popen('scripts/script_6_2_18').read()

	if (check == ''):
		return True
	else:
		return False

# 6.2.19 Ensure no duplicate group names exist
def task_6_2_19(fixbug=False):
	check = os.popen('scripts/script_6_2_19').read()

	if (check == ''):
		return True
	else:
		return False

# 6.2.20 Ensure shadow group is empty
def task_6_2_20(fixbug=False):
	check = os.popen('grep ^shadow:[^:]*:[^:]*:[^:]+ /etc/group').read()
	check2 = os.popen('awk -F: \'($4 == "<shadow-gid>") { print }\' /etc/passwd').read()

	if (check == '' and check2 == ''):
		return True
	else:
		return False