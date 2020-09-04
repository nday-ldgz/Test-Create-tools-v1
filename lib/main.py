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

def vultr_server_create(dcid,vpsplanid,osid): #创建主机
    try:
        vultr_server_create = vultr.server.create(dcid,vpsplanid,osid)
        logging.info(vultr_server_create)
        pass
    except:
        logging.info('[-]请检查网络是否正常,请检查账号余额是否充足!')
        pass
    
def server_os_destroy(subid): #删除主机
    try:
        server_os_destroy = vultr.server.destroy(subid)
        logging.info(server_os_destroy)   
        pass
    except:
        logging.info('[-]请检查网络是否正常!')
        pass
        

def iso_os(url_iso): #自定义iso镜像上传
    try:
        url = 'https://api.vultr.com/v2/iso'
        header = {'Content-Type':'application/json','Authorization':'Bearer '+api_key}
        data ={'url':url_iso}   
        isoos = requests.post(url,data=json.dumps(data),headers=header)
        logging.info('[*]状态码/201成功')
        logging.info(isoos.status_code)
        if isoos.status_code == 201:
            logging.info('[+]iso创建成功')
            pass
        else:
            logging.info('[-]iso创建失败')
            pass
    except:
        logging.info('[-]请检查网络是否正常!')
        pass
    

def delete_iso(dl_isoid): #自定义删除iso镜像
    try:
        header = {'API-Key':api_key,'application':'x-www-form-urlencoded'}
        data = {'ISOID':str(dl_isoid)}
        delete_isoid = requests.post('https://api.vultr.com/v1/iso/destroy',data=data,headers=header)
        if delete_isoid.status_code == 200:
            logging.info('[+]iso删除成功')
            pass
        else:
            logging.info('[-]iso删除失败')
            pass
    
    except:
        logging.info('[-]请检查网络是否正常!')
        pass
    
    
def iso_server(DCID,VPSPLANID,ISOID): #创建自定义ISO主机
    try:
        header = {'API-Key':api_key,'application':'x-www-form-urlencoded'}
        data = {'DCID':int(DCID),'VPSPLANID':int(VPSPLANID),'OSID':'159','ISOID':str(ISOID)} #40 206 788302
        telliso_server = requests.post('https://api.vultr.com/v1/server/create',data=data,headers=header)
        tell = json.loads(telliso_server.text)
        logging.info('[+]创建主机成功SUBID:'+tell['SUBID'])
        pass
    except:
        logging.info('[-]请检查网络是否正常!')
        pass

def server_tag(SUBID,label): #创建主机标签
    try:
        header = {'API-Key':api_key,'application':'x-www-form-urlencoded'}
        data = {'SUBID':SUBID,'label':label} 
        tag_server = requests.post('https://api.vultr.com/v1/server/label_set',data=data,headers=header)
        if tag_server.status_code == 200:
            logging.info('[+]主机标签创建成功')
            pass
        else:
            logging.info('[-]主机标签创建失败')
            pass

    except:
        logging.info('[-]请检查网络是否正常!')
        pass

        
    
    
    