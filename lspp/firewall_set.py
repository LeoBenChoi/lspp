# -*- coding: UTF-8 -*-
#!/usr/bin/python3
# This is firewall setting

import os
import time


# firewall list
def firewall_status():
    os.system("firewall-cmd --list-all")

# prohibit ping
def ping_off():
    # icmp-block-inversion add
    os.system('firewall-cmd --zone=public --add-icmp-block-inversion --permanent')
    print('重启服务, 请稍等...')
    os.system("systemctl restart firewalld")
    time.sleep(1)

def ping_no():
    # icmp-block-inversion remove
    os.system('firewall-cmd --zone=public --remove-icmp-block-inversion --permanent')
    print('重启服务, 请稍等...')
    os.system("systemctl restart firewalld")
    time.sleep(1)

# add open service
def firewall_add_services():
    try:
        service = input("请输入要增加放通的服务: ")
        os.system("firewall-cmd --zone=public --add-service={} --permanent".format(service))
        print('重启服务, 请稍等...')
        os.system("systemctl restart firewalld")
        time.sleep(1)
    except:
        print("请输入正确的服务")
        time.sleep(1)


# remove open service
def firewall_remove_services():
    try:
        service = input("请输入要关闭放通的服务: ")
        os.system("firewall-cmd --zone=public --remove-service={} --permanent".format(service))
        print('重启服务, 请稍等...')
        os.system("systemctl restart firewalld")
        time.sleep(1)
    except:
        print("请输入正确的服务")
        time.sleep(1)

# add open port
def firewall_add_port():
    port = int(input("请输入要增加放通的端口号: "))
    if port <= 65535 and port >= 1:
        os.system("firewall-cmd --zone=public --add-port={}/tcp --permanent".format(port))
        print('重启服务, 请稍等...')
        os.system("systemctl restart firewalld")
        time.sleep(1)
    elif port > 65535 or port < 1:
        print("请输入1-65535端口")
        time.sleep(1)
        
# remove open port
def firewall_remove_port():
    port = int(input("请输入要关闭放通的端口号: "))
    if port <= 65535 and port >= 1:
        os.system("firewall-cmd --zone=public --remove-port={}/tcp --permanent".format(port))
        print('重启服务, 请稍等...')
        os.system("systemctl restart firewalld")
        time.sleep(1)
    elif port > 65535 or port < 1:
        print("请输入1-65535端口")
        time.sleep(1)


# add open protocol
def firewall_add_protocol():
    protocol = input("请输入要放通的协议: ")
    os.system("firewall-cmd --zone=public --add-protocol={} --permanent".format(protocol))
    print('重启服务, 请稍等...')
    os.system("systemctl restart firewalld")
    time.sleep(1)

# remove open protocol
def firewall_remove_protocol():
    protocol = input("请输入要禁止放通的协议: ")
    os.system("firewall-cmd --zone=public --remove-protocol={} --permanent".format(protocol))
    print('重启服务, 请稍等...')
    os.system("systemctl restart firewalld")
    time.sleep(1)

def main_part():
    while(True):
        firewall_status()
        print("""功能列表:
        1. 设置禁ping
        2. 设置不禁ping

        3. 放通服务
        4. 不放通服务

        5. 放通端口
        6. 不放通端口

        7. 放通协议
        8. 不放通协议

        0. 退出\n\n""")
        
        fun_select = input('选择功能(输入编号): ')
        try:
            fun_select = int(fun_select)
        except:
            print('请输入一个功能列表存在的数字\n\n')
            continue
        if fun_select == 0:
            print('退出')
            time.sleep(1)
            exit()
        elif fun_select == 1:
            ping_off()
        elif fun_select == 2:
            ping_no()
        elif fun_select == 3:
            firewall_add_services()
        elif fun_select == 4:
            firewall_remove_services()
        elif fun_select == 5:
            firewall_add_port()
        elif fun_select == 6:
            firewall_remove_port()       
        elif fun_select == 7:
            firewall_add_protocol()
        elif fun_select == 8:
            firewall_remove_protocol()
        print('\n\n')        

if __name__ == '__main__':
    main_part()
