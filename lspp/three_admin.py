# -*- coding: UTF-8 -*-
#!/usr/bin/python3
# This is three admin moudle

import os
import time
import flag

# create admin user
def create_three_admin():
    print('''
    三员账号:
        系统管理员: sysadmin
            权限: 系统配置，有配置etc目录下所有文件的权限
        安全管理员: secadmin
            权限: 安全配置，可以创建、删除、锁定、解锁用户
        审计管理员: aduadmin
            描述: 日志审计，有查看日志的权限
    ''')    
        
    time.sleep(5)

    # Judgment
    if flag.judge_flag('create_three_admin') == True:
        print('已经创建过三员账号')
        time.sleep(5)
    elif flag.judge_flag('create_three_admin') == False:

        # Create users
        print('准备创建三员账号')
        time.sleep(3)
        print('准备创建系统管理员: sysadmin')
        time.sleep(3)
        os.system("useradd sysadmin")
        print('系统管理员创建...')
        print('准备创建安全管理员: secadmin')
        time.sleep(3)
        os.system("useradd secadmin")
        print('安全管理员创建...')
        print('准备创建审计管理员: audadmin')
        time.sleep(3)
        os.system("useradd audadmin")
        print('审计管理员创建...')

        # Init password
        print('给三员账号分配初始密码')
        time.sleep(3)
        os.system("echo 'sysadmin:sysadmin' | chpasswd")
        os.system("echo 'secadmin:secadmin' | chpasswd")
        os.system("echo 'audadmin:audadmin' | chpasswd")
        #print('设置三员第一次登录账号需要更改密码...')
        #time.sleep(3)
        #os.system('chage -d 0 sysadmin')
        #os.system('chage -d 0 secadmin')
        #os.system('chage -d 0 audadmin')

        # Init permission (write sudoers)
        # PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
        print('正在进行命令权限配置, 时间较长, 请勿中途退出...')
        time.sleep(5)

        #os.system("echo -e 'sysadmin\tALL=(ALL)\t /usr/bin/vi,/usr/bin/vim /usr/share/vim' >> /etc/sudoers")
        os.system("echo -e 'secadmin\tALL=(ALL)\t /usr/sbin/useradd, /usr/sbin/userdel, /usr/sbin/groupadd, /usr/sbin/groupdel, /usr/bin/passwd, /usr/sbin/usermod, /sbin/pam_tally2' >> /etc/sudoers")
        #os.system("echo -e 'audadmin\tALL=(ALL)\t /usr/bin/cat, /usr/bin/tac, /usr/bin/less, /usr/bin/more, /usr/bin/tail, /usr/bin/head' >> /etc/sudoers")

        #os.system("echo -e 'sysadmin\tALL=(ALL)\tNOPASSWD: ALL' >> /etc/sudoers")
        #os.system("echo -e 'secadmin\tALL=(ALL)\tNOPASSWD: /usr/sbin/useradd, /usr/sbin/userdel, /usr/sbin/groupadd, /usr/sbin/groupdel, /usr/bin/passwd' >> /etc/sudoers")
        #os.system("echo -e 'audadmin\tALL=(ALL)\tNOPASSWD: /usr/bin/cat, /usr/bin/tac, /usr/bin/less, /usr/bin/more, /usr/bin/tail, /usr/bin/head' >> /etc/sudoers")

        # Init permission (path) 
        print('正在进行访问权限配置, 时间较长, 请勿中途退出...')
        time.sleep(5)
        os.system('setfacl -Rm u:sysadmin:rwx /etc /opt')
        #os.system('setfacl -Rm u:secadmin:rwx')
        os.system('setfacl -Rm u:audadmin:rwx /var')

        # Fixing permissions
        os.system('setfacl -Rb /var/empty/sshd/')
        os.system('setfacl -Rb /etc/ssh/')
    
        # 加入root组
        print('将三员加入root组')
        time.sleep(3)
        os.system('usermod -aG root sysadmin')
        os.system('usermod -aG root secadmin')
        os.system('usermod -aG root audadmin')

        # write flag
        os.system('echo "完成创建, 写入flag"')
        os.system('echo "create_three_admin" >> flag')



# create safe group
def create_safe_group():
    print('配置安全组')    
    time.sleep(5)

    # Judgment
    if flag.judge_flag('create_safe_group') == True:
        print('已经创建安全组')
        time.sleep(5)
    elif flag.judge_flag('create_safe_group') == False:

        print('准备创建安全组...')
        time.sleep(5)
        # Create group is safe, and only safe group can use su root
        os.system("groupadd safe")
        # user add safe group
        os.system("usermod -aG safe sysadmin")
        os.system("usermod -aG safe secadmin")
        os.system("usermod -aG safe audadmin")

        # write flag
        os.system('echo "完成创建, 写入flag"')
        os.system('echo "create_safe_group" >> flag')

def main_part():
    while(True):
        print("""功能列表:
        1. 创建三员账号
        2. 创建安全组(用于提权)
        0. 退出\n""")
        fun_select = input('选择功能(输入编号): ')
        try:
            fun_select = int(fun_select)
        except:
            print('请输入一个功能列表存在的数字\n\n')
            continue
        if fun_select == 0:
            exit()
        elif fun_select == 1:
            create_three_admin()
        elif fun_select == 2:
            create_safe_group()
        else:
            print("请输入功能列表里存在的数字")
            # 进行一次功能操作输出两行空白，优化一下排版
        print('\n\n')


if __name__ == '__main__':
    main_part()
