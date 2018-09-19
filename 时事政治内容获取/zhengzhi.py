#encoding=utf-8
import requests
import re
import os
import sys
import random
import time
from bs4 import BeautifulSoup

def stringlistsave(save_path,filename,myPageResults):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path=save_path+"/"+filename+".txt"
    with open(path,"a+") as fp:
        for s in myPageResults:
            fp.write("%s------------%s\n" %(s[0],s[1]))
    
def page_info(mypage):
    mypage_info=re.findall(r'<dt><a href="(.*?)" title="(.*?)" target="_blank">.*?</a></dt>',mypage,re.S)
    print (mypage_info)
    return mypage_info

def new_page_info(url):
    html=requests.get(url)
    soup=BeautifulSoup(html,'html.parser')
    url_famous = soup.select('<div class="zgsz_sContent clearfix">  <p><strong>导语</strong> >p')  
    url_famous .append(soup.select('<div class="zgsz_sContent clearfix">  <p><strong>导语</strong> >p'))   
    print(url_famous)
    #mypage_info=re.findall(r'<div class="zgsz_sContent clearfix"> <p><strong>(.*?)</strong>:(.*?)</p>',new_page,re.S)
    #dom=etree.HTML(new_page)
    #new_items=dom.xpath('//tr/td/a/text()')
    #new_urls=dom.xpath('//tr/td/a/@href')
    #assert(len(new_items)==len(new_urls))
    #return zip(new_items,new_urls)
    
def spider(url):
    i=time.strftime("%F",time.localtime())
    #i=time.strftime("%c",time.localtime())
    print ("downloading ", url)
    mypage=requests.get(url).content.decode("gbk")
    mypageresults=page_info(mypage)
    save_path=u"时事政治"
    filename=i+"_"+u"创建"
    stringlistsave(save_path,filename,mypageresults)
    #i+=1
    #for url,item in mypageresults:
        #print ("downloading",url)
        ##print ("aaa")
        ##new_page=requests.get(url).content.decode("gbk")
        #newpageresults=new_page_info(url)
        #filename=str(i)+"_"+item
        #stringlistsave(save_path,filename,newpageresults)
        #i+=1
    
if __name__=='__main__':
    print ("用法:")
    start_url1='http://www.offcn.com/shizheng/szrd/zhengzhi/'
    spider(start_url1)
    a=int(sys.argv[1])+1
    for i in range(2,a):
        start_url='http://www.offcn.com/shizheng/szrd/zhengzhi/{}.html'.format(i)
        spider(start_url)
    print ("end")