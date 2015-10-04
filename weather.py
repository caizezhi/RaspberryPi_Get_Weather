# -*- coding: utf-8 -*-
import time
import os
import commands
import sys
import string

now = time.strftime('%M%S',time.localtime(time.time()))
hour = time.strftime('%H',time.localtime(time.time()))
def get_weather():
    temp = os.popen("weather 'beijing'").read()#.strip('\n')
    ntemp = temp.replace("Temperature","温度")
    ntemp = ntemp.replace("Relative Humidity","相对湿度")
    ntemp = ntemp.replace("Wind","风力")
    ntemp = ntemp.replace("Sky conditions","天空状况")
    ntemp = ntemp.replace("Heat index","热指数")
    ntemp = ntemp.replace("Weather","天气")
    print temp
    temp1 = os.popen("weather 'hefei'").read()#.strip('\n')
    ntemp1 = temp1.replace("Temperature","温度")
    ntemp1 = ntemp1.replace("Relative Humidity","相对湿度")
    ntemp1 = ntemp1.replace("Wind","风力")
    ntemp1 = ntemp1.replace("Sky conditions","天空状况")
    ntemp1 = ntemp1.replace("Heat index","热指数")
    ntemp1 = ntemp1.replace("Weather","天气")
    print temp1
    temp2 = os.popen("weather 'xiamen'").read()#.strip('\n')
    ntemp2 = temp2.replace("Temperature","温度")
    ntemp2 = ntemp2.replace("Relative Humidity","相对湿度")
    ntemp2 = ntemp2.replace("Wind","风力")
    ntemp2 = ntemp2.replace("Sky conditions","天空状况")
    ntemp2 = ntemp2.replace("Heat index","热指数")
    ntemp2 = ntemp2.replace("Weather","天气")
    print temp2
    temp3 = '============================'+time.strftime('%Y-%m-%d %a %H:%M:%S',time.localtime(time.time()))+'============================='
    print temp3
    fw = open(r"weather.txt",'a')
    fw.writelines(ntemp+"\r\n"+ntemp1+"\r\n"+ntemp2+"\r\n"+temp3+"\r\n")
    fw.close()

while True:
    now = time.strftime('%M%S',time.localtime(time.time()))
    hour = time.strftime('%H',time.localtime(time.time()))
    if hour == '21' and now == '5300':
        get_weather()

