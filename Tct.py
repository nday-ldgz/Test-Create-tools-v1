#! /usr/bin/python3

'''
2020 Greekn developers (Test-Create-tools@v1)

'''

import sys,json,logging,requests,click
from lib.initial import *
from lib.Create_server import *
from lib.main import *
from termcolor import colored, cprint


print(
'''
 _______        _    _____                _       _              _             
|__   __|      | |  / ____|              | |     | |            | |      ____  
   | | ___  ___| |_| |     _ __ ___  __ _| |_ ___| |_ ___   ___ | |___  / __ \ 
   | |/ _ \/ __| __| |    | '__/ _ \/ _` | __/ _ \ __/ _ \ / _ \| / __|/ / _` |
   | |  __/\__ \ |_| |____| | |  __/ (_| | ||  __/ || (_) | (_) | \__ \ | (_| |
   |_|\___||___/\__|\_____|_|  \___|\__,_|\__\___|\__\___/ \___/|_|___/\ \__,_|
                                                                        \____/ 

                                                          BY:Greekn@v1 
''')

@click.group()
def main():
 pass

@main.command()
def initial_state():
    logging.info(account_info_1()) #账号信息
    logging.info(account_info_2()) #vultr充值信息   
    logging.info(account_info_4()) #获取ISO信息
    logging.info(account_info_3()) #获取主机信息
    pass

@main.command()    
def host_list():
    logging.info(dcid())   #选择地区  
    logging.info(vpsplanid()) #选择主机套餐
    logging.info(osid()) #选择操作系统
    pass

@main.command()
@click.option('-d', '--dcid', type=str, help='选择地区')
@click.option('-v', '--vpsplanid', type=str, help='选择主机套餐')  
@click.option('-o', '--osid', type=str, help='选择操作系统')    
def new_host(dcid,vpsplanid,osid):
    logging.info(vultr_server_create(dcid,vpsplanid,osid)) #创建主机dcid 选择地区 vpsplanid选择主机套餐 osid 选择操作系统
    pass  

@main.command()
@click.option('-s', '--subid', type=str, help='删除主机subid')    
def delete_server(subid):
    logging.info(server_os_destroy(subid)) #删除主机subid
    pass

@main.command()
@click.option('-u', '--url', type=str, help='创建ISO url下载')      
def iso_os_wget(url):
    logging.info(iso_os(url)) #创建ISO url下载
    pass

@main.command()
@click.option('-i', '--isoid', type=str, help='参数isoid')          
def delete_iso_isoid(isoid):
    logging.info(delete_iso(isoid))#删除iso 参数isoid
    pass

@main.command()
@click.option('-d', '--dcid', type=str, help='选择地区')
@click.option('-v', '--vpsplanid', type=str, help='选择主机套餐')  
@click.option('-i', '--osid', type=str, help='选择自定义ISO')        
def new_iso_server(dcid,vpsplanid,ISOID):
    logging.info(iso_server(dcid,vpsplanid,ISOID))#创建自定义ISO主机 dcid 选择地区 vpsplanid选择主机套餐 ISOID选择自定义ISO
    pass

@main.command()
@click.option('-s', '--subid', type=str, help='subid主机ID')
@click.option('-t', '--tag', type=str, help='创建主机标签')  
def new_server_tag(subid,tag):
    logging.info(server_tag(subid,tag))#创建主机标签
    pass
       
if __name__=="__main__":
    logging.basicConfig(format='[%(asctime)s] -- [%(levelname)s]:%(message)s',
                        level=logging.DEBUG)
    main()
    

