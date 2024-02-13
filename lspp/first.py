# -*- coding: UTF-8 -*-
#!/usr/bin/python2
# First use, Prepare the environment

import os
import time
import flag


# first use, init.
def main_part():
    # Judgment    
    if  flag.judge_flag('first') == True:
        os.system('echo "已经进行过初始化, 准备跳过脚本..."')
        time.sleep(3)

    elif  flag.judge_flag('first') == False:
        os.system('echo "即将开始准备初始环境..."')

        # change my yum source
        time.sleep(5)
        os.system("mkdir /etc/yum.repos.d/bak")
        os.system("mv /etc/yum.repos.d/*.repo /etc/yum.repos.d/bak/")
        os.system("curl -o /etc/yum.repos.d/aliyun.repo http://mirrors.aliyun.com/repo/Centos-7.repo")
        os.system("sed -i 's/http/https/g' /etc/yum.repos.d/aliyun.repo")
        os.system("yum clean all")
        os.system("yum makecache")   

        # install software
        with open("software_list.txt", "r") as f:
            for line in f.readlines():
                line = line.strip('\n')
                os.system("echo '准备安装 '"+line)
                time.sleep(3)
                os.system("yum install {} -y".format(line))

        os.system("echo '初始化完成...'")
        
        # write flag
        os.system('echo "初始化准备完成, 写入flag"')
        os.system('echo "first" >> flag')    

if __name__ == '__main__':
    main_part()
