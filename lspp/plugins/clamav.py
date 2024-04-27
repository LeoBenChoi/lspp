# -*- coding: UTF-8 -*-
#!/usr/bin/python3
# This is clamav moudle, this a Virus Scanning Software

import os
import time
import flag


def install_clamav():
    # Judgment
    if flag.judge_flag('install_clamav') == True:
        print('clamav已安装, 请选择功能')
    elif flag.judge_flag('install_clamav') == False:
        print('第一次使用, 准备进行安装与初始化...')
        time.sleep(3)
        os.system('yum install https://www.clamav.net/downloads/production/clamav-1.3.0.linux.x86_64.rpm -y')
        init_clamav()
    
        # write flag
        os.system('echo "完成安装, 写入flag"')
        os.system('echo "install_clamav" >> flag')

def init_clamav():
    # init
    print('准备创建clamav 用户')
    time.sleep(3)
    os.system('useradd clamav')
    os.system("echo 'clamav:clamav' | chpasswd")
    print('创建用户完成, 准备创建日志文件夹...')
    os.system('mkdir -p /var/log/clamav/virus')
    os.system('chown -R clamav:clamav /var/log/clamav')
    time.sleep(3)    
    print("创建日志文件夹完成, 开始配置clamav...")
    time.sleep(5)
    os.system("cp -f /usr/local/etc/clamd.conf.sample /usr/local/etc/clamd.conf")
    os.system("cp -f /usr/local/etc/freshclam.conf.sample /usr/local/etc/freshclam.conf")
    os.system("sed -i '/Example\(.*\)$/ s/^\(.*\)$/#\1/g' /usr/local/etc/clamd.conf")
    os.system("sed -i '/Example\(.*\)$/ s/^\(.*\)$/#\1/g' /usr/local/etc/freshclam.conf")
    print('clamav配置完成, 准备更新病毒库...')
    time.sleep(5)
    os.system("freshclam")
    #print('更新病毒库完成, 准备创建自动任务...')
    print('给管理员准备扫描病毒脚本')
    time.sleep(3)
    os.system("echo 'clamscan -r -i  --log=/var/log/clamav/clamav.log --move=/var/log/clamav/virus/ --exclude-dir=/var/log/clamav/virus --exclude-dir=/sys /' > /home/sysadmin/clam.sh")
    os.system("echo 'clamscan -r -i  --log=/var/log/clamav/clamav.log --move=/var/log/clamav/virus/ --exclude-dir=/var/log/clamav/virus --exclude-dir=/sys /' > /home/secadmin/clam.sh")
    os.system("echo 'clamscan -r -i  --log=/var/log/clamav/clamav.log --move=/var/log/clamav/virus/ --exclude-dir=/var/log/clamav/virus --exclude-dir=/sys /' > /home/audadmin/clam.sh")
    os.system('chown sysadmin:sysadmin /home/sysadmin/clam.sh')
    os.system('chown secadmin:secadmin /home/secadmin/clam.sh')
    os.system('chown audadmin:audadmin /home/audadmin/clam.sh')
    os.system('chmod +x /home/sysadmin/clam.sh')
    os.system('chmod +x /home/secadmin/clam.sh')
    os.system('chmod +x /home/audadmin/clam.sh')
    print('初始化完成, 将要进行安装完成之后的第一次扫描...')
    time.sleep(5)
    os.system('chmod 622 /var/log/clamav/clamav.log')
    clamav_scan()

def clamav_scan():
    os.system("freshclam")
    os.system('clamscan -r -i  --log=/var/log/clamav/clamav.log --move=/var/log/clamav/virus/ --exclude-dir=/var/log/clamav/virus --exclude-dir=/sys /')

def clamav_view_logs():
    os.system('cat /var/log/clamav/clamav.log')


def main_part():
    install_clamav()
    while(True):
        print("""功能列表:
        1. 扫描病毒
        2. 查看日志
        0. 退出""")
        
        fun_select = input('选择功能(输入编号): ')
        try:
            fun_select = int(fun_select)
        except:
            print('请输入一个功能列表存在的数字\n\n')
            continue
        if fun_select == 0:
            exit()
        elif fun_select == 1:
            clamav_scan()
        elif fun_select == 2:
            clamav_view_logs()
        else:
            print("请输入功能列表里存在的数字")
            # 进行一次功能操作输出两行空白，优化一下排版
        print('\n\n')


if __name__ == '__main__':
    print('ok')
