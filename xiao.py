__author__ = 'xiao'
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
from threading import Timer
import threading
import csv
import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#爬取单页的数据
def crawl(url):
    data_all=[]
    page = urllib.request.urlopen(url)
    contents = page.read()
    soup = BeautifulSoup(contents, "html.parser")
    dic=soup.body
    print (u'爬取信息如下:\n')
    for tag in dic.find_all('div',attrs={"class":"cfcpn_list_content"}):
        temp=[]
        url1="http://www.cfcpn.com"+tag.find('a')['href']
        print(url1)
        page1=urllib.request.urlopen(url1)
        contents1=page1.read()
        data=BeautifulSoup(contents1,"html.parser")
        title=data.find(class_='cfcpn_news_title')
        if(title):
          print(title.string)
          temp.append(title.string)
        else:
          print("title")
          temp.append("title")
        time=data.find(class_='cfcpn_news_date')
        print(time.string)
        temp.append(time.string)


        datas=data.find(id='news_content')
        #for string in data.stripped_string:
            #print(repr(string))
        f=datas.get_text("",strip=True)
        print(f)
        temp.append(f)
        data_all.append(temp)
    return data_all


#获取爬取网页的总数
def pagemax(url):
    page = urllib.request.urlopen(url)
    contents = page.read()
    soup = BeautifulSoup(contents, "html.parser")
    pages=soup.find_all(class_='page')
    #print(pages)
    pagenum=pages[-2].get_text()
    return (int(pagenum))

def crawl_all(url):
    #url='http://www.cfcpn.com/plist/caigou'
    with open('xiao.csv','a',errors='ignore',newline='') as f:
     f_csv=csv.writer(f)
     for i in range(1,pagemax(url)+1):
       url1='http://www.cfcpn.com:80/plist/caigou?pageNo='+str(i)+'&kflag=0&keyword=&keywordType=&province=&city=&typeOne=&ptpTwo='
       result=crawl(url1)
       f_csv.writerows(result)


def maildata():
    server = smtplib.SMTP('smtp.163.com', 25) #用的163邮箱做的服务器
    server.login('自己的用户名', '密码')
    message = MIMEMultipart()
    msg = MIMEText('今天的数据的汇总情况', 'plain', 'utf-8') 
    message['From'] = 'm17621755797@163<m17621755797@163.com>' #发送方
    message['Subject'] = Header(u'数据汇总', 'utf-8').encode() #邮件主题
    message['To'] = u'肖茂 <876963995@qq.com>' #接收方
    att1 = MIMEText(open('C:/Users/xiao/PycharmProjects/untitled/xiao.csv', 'rb').read(), 'base64', 'utf-8') #添加的附件
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="xiao.csv"'
    message.attach(msg)
    message.attach(att1)
    server.sendmail('m17621755797@163.com', ['876963995@qq.com'], message.as_string())
    server.quit()


def run():
    url='http://www.cfcpn.com/plist/caigou'
    filename='C:/Users/xiao/PycharmProjects/untitled/xiao.csv'#存放抓取数据的文件的目录
    if os.path.exists(filename):
        os.remove(filename)
        crawl_all(url)
        maildata()
    else:
        crawl_all(url)
        maildata()


def runbytime():
    print("程序马上启动。。。。")
    run()
    global t
    t=threading.Timer(300,runbytime()) #设定的时间稍微长点，防止数据还没读完就重新开始了
    t.start()





#主函数
if __name__ == '__main__':
    t=threading.Timer(3,runbytime())
    t.start()



