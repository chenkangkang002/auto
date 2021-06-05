#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：testgrouppub 
@File    ：auth.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/5/6 14:27 
'''
import requests
from setting.variament import HOME_URL, TOKEN, DEVICE_LIST_URL, PROPERTIES_URL, HOME_NAME, \
    HOST, HOST_H5

login_pwd = {
    'url':'https://abp-test.ayla.com.cn/api/v1/miya/user/passwordlogin',
    'method':'POST',
    'header': None,
    'requestBody':{"account":"15885537820","password":"12345678"}
}
device_list = {
    'url':'https://abp-test.ayla.com.cn/api/v1/miya/device/list',
    'method':'POST',
    'header':{'Authorization':'111111111111111111111'},
    'requestBody':{"roomId":"1326465137380630568","pageNo":1,"pageSize":500}
}

api_lis = [
    {'login_pwd':login_pwd}
]
def get_home_info():
    '''
    获取账号下的家庭信息列表:[{home1},{home2},{home3}]
    '''
    url = HOST + HOME_URL
    headers = {'Authorization' : TOKEN}
    return requests.get(url = url, headers = headers).json()['data']

def get_device_list(home_name = HOME_NAME):
    # homeId = find_specified_homeId(home_name)
    home_list = get_home_info()
    homeId = None
    for var in home_list:
        if home_name == var['homeName']:
            homeId = var['homeId']
    url = HOST + DEVICE_LIST_URL
    headers = {'Authorization': TOKEN}
    requestBody = {"roomId": homeId,"pageNo":1,"pageSize":500}
    return requests.post(url=url, headers=headers, json = requestBody).json()['data']['devices']

def get_device_h5_properties(deviceId):
    '''获取设备的H5属性'''
    url = HOST_H5 + PROPERTIES_URL.format(deviceId)
    headers = {'Authorization': TOKEN}
    return requests.get(url=url, headers=headers).json()['data']