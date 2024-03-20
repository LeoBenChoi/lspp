# -*- coding: UTF-8 -*- 
#!/usr/bin/python3

import os
import time
import random

import pass_strong
import three_admin
import firewall_set

from plugins import clamav

# print title
def print_title():
    path = 'namestyle'
    for root,dirs,files in os.walk(path):
        pass
        #print(files)
    file = files

    title_num = random.randint(0, len(file)-1 )
    title_name = file[title_num]
    os.system(f'cat namestyle/{title_name}')
    print("""
    软件: Linux Sec ++
    作者: Lio Ben 
    版本: v0.4.35
    项目地址: https://github.com/LioBenChoi/lspp/
    """)
    # 主要版本（结构）.次要版本（功能）.补丁（细节修改）

def main_part():
    print_title()
    username = os.getlogin()
    print("当前用户: {}".format(username))
    while(True):
        print("""功能列表:
        1. Linux 密码安全加固
        2. 三员安全账号创建
        3. 防火墙配置(可选)
        
    扩展模块:
        4. 病毒扫描

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
            pass_strong.main_part()
        elif fun_select == 2:
            three_admin.main_part()
        elif fun_select == 3:
            firewall_set.main_part()
        elif fun_select == 4:
            clamav.main_part()
        else:
            print("请输入功能列表里存在的数字")
            # 进行一次功能操作输出两行空白，优化一下排版
        print("\n\n")
        

if __name__ == '__main__':
    main_part()
