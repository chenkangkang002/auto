#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：aylahome 
@File    ：fresh_air.py    新风
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/6/3 16:39 
'''
from selenium.webdriver.common.by import By

from lib.page.base_page import BasePage


class FreshAir(BasePage):

    loc_PowerSwitch =  (By.XPATH,'//android.view.View/android.view.View[2]/android.view.View[6]/android.view.View[3]/android.widget.Image')#开挂按钮
    loc_PowerSwitch_on = (By.XPATH,'//android.view.View/android.view.View[2]/android.view.View[6]/android.view.View[1]')  #开关打开on
    loc_PowerSwitch_off = (By.XPATH, '//android.view.View/android.view.View[2]/android.view.View[6]/android.view.View[2]')  # 开关打开off
    loc_offline_status = (By.XPATH, '//android.view.View/android.view.View[2]/android.view.View[2]/android.view.View')    #在离线状态

    # {"propertyCode":"PowerSwitch","propertyValue":0}    #开关关闭 0-1
    # {"propertyCode":"WindSpeed","propertyValue":3}  #风速中速 2-3-4

    def switch_windspeed(self,gear):
        '''
        根据档位切换风速
        :param gear: 档位,1,2,3或"1","2","3"
        :return:
        '''
        if isinstance(int(gear),int):
            gear = int(gear)
            if gear == 1:
                self.get_element_text('低速').click()
            elif gear == 2:
                self.get_element_text('中速').click()
            elif gear == 3:
                self.get_element_text('高速').click()
        else:
            return '请传入正确的档位int：1,2,3或者str："1","2","3"'

    def get_offline_status(self):
        '''获取在离线状态'''
        # self.get_element_resourceId(self.loc_app).find_element_by_xpath(self.loc_back_01).click()
        return self.get_element_text('在线')
        # return self.get_children_element_to_parent(self.loc_offline_status)
