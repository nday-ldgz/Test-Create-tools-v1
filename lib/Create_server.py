#! /usr/bin/python3

'''
2020 Greekn developers (Test-Create-tools@v1)

'''

import logging,requests,json,sys,jsonpath
from vultr import Vultr
from termcolor import colored, cprint
from lib.config import *

def dcid():
    logging.info('创建主机请选择地区DC/ID号') #选择地区
    logging.info('---------------') #分割
    logging.info('DC/ID:6') #选择地区6
    logging.info('名称:亚特兰大')
    logging.info('国家:美国')
    logging.info('地区:北美')
    logging.info('---------------') #分割
    logging.info('DC/ID:2') #选择地区2
    logging.info('名称:芝加哥')
    logging.info('国家:美国')
    logging.info('地区:北美')
    logging.info('---------------') #分割
    logging.info('DC/ID:3') #选择地区3
    logging.info('名称:德克萨斯')
    logging.info('国家:美国')
    logging.info('地区:北美')
    logging.info('---------------') #分割
    logging.info('DC/ID:5') #选择地区5
    logging.info('名称:洛杉矶')
    logging.info('国家:美国')
    logging.info('地区:北美')
    logging.info('---------------') #分割
    logging.info('DC/ID:39') #选择地区39
    logging.info('名称:迈阿密')
    logging.info('国家:美国')
    logging.info('地区:北美')   
    logging.info('---------------') #分割
    logging.info('DC/ID:1') #选择地区1
    logging.info('名称:新泽西')
    logging.info('国家:美国')
    logging.info('地区:北美')  
    logging.info('---------------') #分割
    logging.info('DC/ID:4') #选择地区4
    logging.info('名称:西雅图')
    logging.info('国家:美国')
    logging.info('地区:北美')       
    logging.info('---------------') #分割
    logging.info('DC/ID:12') #选择地区12
    logging.info('名称:硅谷')
    logging.info('国家:美国')
    logging.info('地区:北美')      
    logging.info('---------------') #分割
    logging.info('DC/ID:40') #选择地区40
    logging.info('名称:新加坡')
    logging.info('国家:新加坡')
    logging.info('地区:亚太')      
    logging.info('---------------') #分割
    logging.info('DC/ID:7') #选择地区7
    logging.info('名称:阿姆斯特丹')
    logging.info('国家:荷兰')
    logging.info('地区:欧洲')      
    logging.info('---------------') #分割
    logging.info('DC/ID:34') #选择地区34
    logging.info('名称:首尔')
    logging.info('国家:韩国')
    logging.info('地区:亚太')      
    logging.info('---------------') #分割
    logging.info('DC/ID:25') #选择地区25
    logging.info('名称:东京')
    logging.info('国家:日本')
    logging.info('地区:亚太')  
    logging.info('---------------') #分割
    logging.info('DC/ID:8') #选择地区8
    logging.info('名称:伦敦')
    logging.info('国家:英国')
    logging.info('地区:欧盟')      
    logging.info('---------------') #分割
    logging.info('DC/ID:24') #选择地区24
    logging.info('名称:巴黎')
    logging.info('国家:法国')
    logging.info('地区:欧盟')      
    logging.info('---------------') #分割
    logging.info('DC/ID:9') #选择地区9
    logging.info('名称:法兰克福')
    logging.info('国家:德国')
    logging.info('地区:欧盟')      
    logging.info('---------------') #分割
    logging.info('DC/ID:22') #选择地区22
    logging.info('名称:多伦多')
    logging.info('国家:加拿大')
    logging.info('地区:北美')
    logging.info('---------------') #分割
    logging.info('DC/ID:19') #选择地区19
    logging.info('名称:悉尼')
    logging.info('国家:澳大利亚')
    logging.info('地区:澳洲')  
    pass

def vpsplanid():
    logging.info('创建主机请选择主机套餐VPSplanid/ID号') #选择主机套餐
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:201') #选择主机套餐201
    logging.info('主机信息:1024 MB RAM,25 GB SSD,1.00 TB BW')
    logging.info('cpu/1')
    logging.info('带宽:1')
    logging.info('价格月:5')
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:202') #选择主机套餐202
    logging.info('主机信息:2048 MB RAM,55 GB SSD,2.00 TB BW')
    logging.info('cpu/1')
    logging.info('带宽:2')
    logging.info('价格月:10')
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:203') #选择主机套餐203
    logging.info('主机信息:4096 MB RAM,80 GB SSD,3.00 TB BW')
    logging.info('cpu/2')    
    logging.info('带宽:3')
    logging.info('价格月:20')
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:204') #选择主机套餐204
    logging.info('主机信息:8192 MB RAM,160 GB SSD,4.00 TB BW')
    logging.info('cpu/4')    
    logging.info('带宽:4')
    logging.info('价格月:40')
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:205') #选择主机套餐205
    logging.info('主机信息:16384 MB RAM,320 GB SSD,5.00 TB BW')
    logging.info('cpu/6')    
    logging.info('带宽:5')
    logging.info('价格月:80')            
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:206') #选择主机套餐206
    logging.info('主机信息:32768 MB RAM,640 GB SSD,6.00 TB BW')
    logging.info('cpu/8')    
    logging.info('带宽:8')
    logging.info('价格月:160')    
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:207') #选择主机套餐207
    logging.info('主机信息:65536 MB RAM,1280 GB SSD,10.00 TB BW')
    logging.info('cpu/16')    
    logging.info('带宽:10')
    logging.info('价格月:320')        
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:208') #选择主机套餐208
    logging.info('主机信息:98304 MB RAM,1600 GB SSD,15.00 TB BW')
    logging.info('cpu/24')    
    logging.info('带宽:15')
    logging.info('价格月:640')    
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:115') #选择主机套餐115
    logging.info('主机信息:8192 MB RAM,110GB SSD,10.00 TB BW')
    logging.info('cpu/2')
    logging.info('带宽:10')
    logging.info('价格月:60')
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:116') #选择主机套餐116
    logging.info('主机信息:16384 MB RAM,2x110 GB SSD,20.00 TB BW')
    logging.info('cpu/4')
    logging.info('带宽:20')
    logging.info('价格月:120')
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:117') #选择主机套餐117
    logging.info('主机信息:24576 MB RAM,3x110 GB SSD,30.00 TB BW')
    logging.info('cpu/6')
    logging.info('带宽:30')
    logging.info('价格月:180')  
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:118') #选择主机套餐118
    logging.info('主机信息:32768 MB RAM,4x110 GB SSD,40.00 TB BW')
    logging.info('cpu/8')
    logging.info('带宽:40')
    logging.info('价格月:240')        
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:400') #选择主机套餐400
    logging.info('主机信息:1024 MB RAM,32 GB SSD,1.00')
    logging.info('cpu/1')
    logging.info('带宽:1')
    logging.info('价格月:6')      
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:401') #选择主机套餐401
    logging.info('主机信息:2048 MB RAM,64 GB SSD,2.00 TB BW')
    logging.info('cpu/1')    
    logging.info('带宽:2')
    logging.info('价格月:12')  
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:402') #选择主机套餐402
    logging.info('主机信息:4096 MB RAM,128 GB SSD,3.00 TB BW')
    logging.info('cpu/2')     
    logging.info('带宽:3')
    logging.info('价格月:24')  
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:403') #选择主机套餐403
    logging.info('主机信息:8192 MB RAM,256 GB SSD,4.00 TB BW')
    logging.info('cpu/3')
    logging.info('带宽:4')
    logging.info('价格月:48')      
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:404') #选择主机套餐404
    logging.info('主机信息:16384 MB RAM,384 GB SSD,5.00 TB BW')
    logging.info('cpu/4')
    logging.info('带宽:5')
    logging.info('价格月:96')  
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:405') #选择主机套餐405
    logging.info('主机信息:32768 MB RAM,512 GB SSD,6.00 TB BW')
    logging.info('cpu/8') 
    logging.info('带宽:6')
    logging.info('价格月:192')      
    logging.info('---------------') #分割
    logging.info('VPSplanid/ID:406') #选择主机套餐406
    logging.info('主机信息:49152 MB RAM,768 GB SSD,8.00 TB BW')
    logging.info('cpu/12')     
    logging.info('带宽:12')
    logging.info('价格月:256')  
    pass
    
def osid():
    logging.info('创建主机请选择OS系统osid/ID号') #选择OS系统
    logging.info('---------------') #分割
    logging.info('osid/ID:127') #选择主机套餐127
    logging.info('主机系统:CentOS 6 x64')
    logging.info('架构:x64')
    logging.info('系谱:centos')
    logging.info('---------------') #分割
    logging.info('osid/ID:147') #选择主机套餐147
    logging.info('主机系统:CentOS 6 i386')
    logging.info('架构:i386')
    logging.info('系谱:centos')
    logging.info('---------------') #分割
    logging.info('osid/ID:147') #选择主机套餐167
    logging.info('主机系统:CentOS 6 i386')
    logging.info('架构:i386')
    logging.info('系谱:centos')
    logging.info('---------------') #分割
    logging.info('osid/ID:381') #选择主机套餐381
    logging.info('主机系统:CentOS 7 SELinux x64')
    logging.info('架构:x64')
    logging.info('系谱:centos')
    logging.info('---------------') #分割
    logging.info('osid/ID:362') #选择主机套餐362
    logging.info('主机系统:CentOS 8 x64')
    logging.info('架构:x64')
    logging.info('系谱:centos')
    logging.info('---------------') #分割
    logging.info('osid/ID:215') #选择主机套餐215
    logging.info('主机系统:Ubuntu 16.04 x64')
    logging.info('架构:x64')
    logging.info('系谱:ubuntu')
    logging.info('---------------') #分割
    logging.info('osid/ID:216') #选择主机套餐216
    logging.info('主机系统:Ubuntu 16.04 i386')
    logging.info('架构:i386')
    logging.info('系谱:ubuntu')    
    logging.info('---------------') #分割
    logging.info('osid/ID:270') #选择主机套餐270
    logging.info('主机系统:Ubuntu 18.04 x64')
    logging.info('架构:x64')
    logging.info('系谱:ubuntu')
    logging.info('---------------') #分割
    logging.info('osid/ID:365') #选择主机套餐365
    logging.info('主机系统:CentOS 6 i386')
    logging.info('架构:i386')
    logging.info('系谱:centos')
    logging.info('---------------') #分割
    logging.info('osid/ID:387') #选择主机套餐387
    logging.info('主机系统:Ubuntu 20.04 x64')
    logging.info('架构:x64')
    logging.info('系谱:ubuntu')
    logging.info('---------------') #分割
    logging.info('osid/ID:194') #选择主机套餐194
    logging.info('主机系统:Debian 8 i386 (jessie)')
    logging.info('架构:i386')
    logging.info('系谱:debian')   
    logging.info('---------------') #分割
    logging.info('osid/ID:244') #选择主机套餐244
    logging.info('主机系统:Debian 9 x64 (stretch)')
    logging.info('架构:x64')
    logging.info('系谱:centos')
    logging.info('---------------') #分割
    logging.info('osid/ID:352') #选择主机套餐352
    logging.info('主机系统:Debian 10 x64 (buster)')
    logging.info('架构:x64')
    logging.info('系谱:debian')
    logging.info('---------------') #分割
    logging.info('osid/ID:230') #选择主机套餐230
    logging.info('主机系统:FreeBSD 11 x64')
    logging.info('架构:x64')
    logging.info('系谱:freebsd')
    logging.info('---------------') #分割
    logging.info('osid/ID:327') #选择主机套餐327
    logging.info('主机系统:FreeBSD 12 x64')
    logging.info('架构:x64')
    logging.info('系谱:freebsd')   
    logging.info('---------------') #分割
    logging.info('osid/ID:366') #选择主机套餐366
    logging.info('主机系统:OpenBSD 6.6 x64')
    logging.info('架构:x64')
    logging.info('系谱:openbsd')
    logging.info('---------------') #分割
    logging.info('osid/ID:394') #选择主机套餐394
    logging.info('主机系统:CentOS 6 i386')
    logging.info('架构:i386')
    logging.info('系谱:centos')
    logging.info('---------------') #分割
    logging.info('osid/ID:179') #选择主机套餐179
    logging.info('主机系统:CoreOS Stable')
    logging.info('架构:x64')
    logging.info('系谱:coreos')
    logging.info('---------------') #分割
    logging.info('osid/ID:391') #选择主机套餐391
    logging.info('主机系统:Fedora CoreOS')
    logging.info('架构:x64')
    logging.info('系谱:edora-coreos')   
    logging.info('---------------') #分割
    logging.info('osid/ID:367') #选择主机套餐367
    logging.info('主机系统:Fedora 31 x64')
    logging.info('架构:x64')
    logging.info('系谱:fedora')
    logging.info('---------------') #分割
    logging.info('osid/ID:389') #选择主机套餐389
    logging.info('主机系统:Fedora 32 x64')
    logging.info('架构:x64')
    logging.info('系谱:fedora') 
    logging.info('---------------') #分割
    logging.info('osid/ID:124') #选择主机套餐124
    logging.info('主机系统:Windows 2012 R2 x64')
    logging.info('架构:x64')
    logging.info('系谱:windows')
    logging.info('---------------') #分割
    logging.info('osid/ID:240') #选择主机套餐240
    logging.info('主机系统:Windows 2016 x64')
    logging.info('架构:x64')
    logging.info('系谱:windows') 
    logging.info('---------------') #分割
    logging.info('osid/ID:159') #选择主机套餐159
    logging.info('主机系统:Custom')
    logging.info('架构:x64')
    logging.info('系谱:自定义iso')
    logging.info('---------------') #分割
    logging.info('osid/ID:164') #选择主机套餐164
    logging.info('主机系统:Snapshot')
    logging.info('架构:x64')
    logging.info('系谱:snapshot') 
    logging.info('---------------') #分割
    logging.info('osid/ID:180') #选择主机套餐180
    logging.info('主机系统:Backup')
    logging.info('架构:x64')
    logging.info('系谱:backup')
    logging.info('---------------') #分割
    logging.info('osid/ID:147') #选择主机套餐186
    logging.info('主机系统:Application')
    logging.info('架构:x64')
    logging.info('系谱:application') 
    pass



