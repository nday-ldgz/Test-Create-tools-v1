#! /usr/bin/python3

'''
2020 Greekn developers (Test-Create-tools@v1)

'''

import logging,requests,json,sys,jsonpath
from vultr import Vultr
from termcolor import colored, cprint
from lib.config import *


api_key = vultr_config()
vultr = Vultr(api_key)

def account_info_1(): #初始化获取Vultr平台基础信息     
    authinfo = requests.get('https://api.vultr.com/v1/auth/info?api_key='+api_key) #账号信息
    auth_info = json.loads(authinfo.text)
    try:
        logging.info('---------------------------------------------')
        logging.info('加载Vultr平台初始化中......')
        logging.info('名称:'+auth_info['name'])
        logging.info('邮箱：'+auth_info['email'])
        logging.info('---------------------------------------------')
        pass
    except:
        logging.info('[-]请检查网络是否正常!,请检查key是否填写正确.')
        pass
    
def account_info_2(): #Vultr充值信息  
    account_info = vultr.account.info()  
    try:
        logging.info('---------------------------------------------')
        logging.info('余额:'+account_info['balance'])
        logging.info('待定费用:'+account_info['pending_charges'])
        logging.info('最后付款时间:'+account_info['last_payment_date'])
        logging.info('最后付款金额:'+account_info['last_payment_amount'])
        logging.info('---------------------------------------------')
        pass
 
    except:
        logging.info('[-]请检查网络是否正常!,请检查key是否填写正确.')
        pass

    
def account_info_3(): #获取主机信息
    server_list = vultr.server.list()
    server_text=jsonpath.jsonpath(server_list,'*')
    try:
        for e in range(len(server_text)):
            logging.info('---------------------------------------------')
            logging.info('获取主机信息......')
            logging.info('主机名称:'+server_text[e]['label'])
            logging.info('SUBID:'+server_text[e]['SUBID'])
            logging.info('操作系统:'+server_text[e]['os'])
            logging.info('内存:'+server_text[e]['ram'])
            logging.info('硬盘:'+server_text[e]['disk'])
            logging.info('IP:'+server_text[e]['main_ip'])
            logging.info('位置:'+server_text[e]['location'])
            logging.info('账号:root')
            logging.info('密码:'+server_text[e]['default_password'])
            logging.info('---------------------------------------------')
            pass
    except:
        logging.info('[-]未创建主机!')
        pass

def account_info_4(): #获取自定义ISO信息
    iso_list = vultr.iso.list()
    ISO_ID = jsonpath.jsonpath(iso_list,'$..ISOID')
    date_created = jsonpath.jsonpath(iso_list,'$..date_created')
    filename = jsonpath.jsonpath(iso_list,'$..filename')
    size = jsonpath.jsonpath(iso_list,'$..size')
    md5sum = jsonpath.jsonpath(iso_list,'$..md5sum')
    sha512sum = jsonpath.jsonpath(iso_list,'$..sha512sum')
    status = jsonpath.jsonpath(iso_list,'$..status')
    try:
        for e in range(len(iso_list)):
            logging.info('获取ISO信息......')
            logging.info('ISOID:')
            logging.info(ISO_ID[e])
            logging.info('-----------------')
            logging.info('创建日期:')
            logging.info(date_created[e])
            logging.info('-----------------')
            logging.info('文件名称:')
            logging.info(filename[e])
            logging.info('-----------------')
            logging.info('大小:')
            logging.info(size[e])
            logging.info('-----------------')
            logging.info('md5:')
            logging.info(md5sum[e])
            logging.info('-----------------')
            logging.info('sha512:')
            logging.info(sha512sum[e])
            logging.info('-----------------')
            logging.info('状态:')
            logging.info(status[e])
            pass
        
    except:
        logging.info('[-]请检查网络是否正常!')
        pass
        
        
    

