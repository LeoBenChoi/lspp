# -*- coding: UTF-8 -*-
#!/usr/bin/python3
# This is three admin moudle

import os
import time
import flag

# create admin user
def create_three_admin():
    # Judgment
    if flag.judge_flag('create_three_admin') == True:
        print('已经创建三员账号')
        time.sleep(5)
    elif flag.judge_flag('create_three_admin') == False:

        # Create user is system admin
        print('准备创建系统管理员: sysadmin')
        time.sleep(5)
        os.system("useradd sysadmin")
        os.system("echo 'sysadmin:sysadmin' | chpasswd")
        print('系统管理员创建完成...')
        
        # Create user is security admin
        print('准备创建安全管理员: secadmin')
        time.sleep(5)
        os.system("useradd secadmin")
        os.system("echo 'secadmin:secadmin' | chpasswd")
        print('安全管理员创建完成...')

        # Create user is audit admin
        print('准备创建审计管理员: audadmin')
        time.sleep(5)
        os.system("useradd audadmin")
        os.system("echo 'audadmin:audadmin' | chpasswd")
        print('审计管理员创建完成...')

        # write flag
        os.system('echo "完成创建, 写入flag"')
        os.system('echo "create_three_admin" >> flag')

# create safe group
def create_safe_group():
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
        os.system("useradd -aG safe sysadmin")
        os.system("useradd -aG safe secadmin")
        os.system("useradd -aG safe audadmin")

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
