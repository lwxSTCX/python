#encoding=utf-8
import requests
import re
import os
import sys
from lxml import etree

def stringlistsave(save_path,filename,myPageResults):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path=save_path+"/"+filename+".txt"
    with open(path,"w+") as fp:
        for s in myPageResults:
            fp.write("%s------------%s\n" %(s[0],s[1]))
    
def page_info(mypage):
    mypage_info=re.findall(r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>',mypage,re.S)
    print (mypage_info)
    return mypage_info

def new_page_info(new_page):
    dom=etree.HTML(new_page)
    new_items=dom.xpath('//tr/td/a/text()')
    new_urls=dom.xpath('//tr/td/a/@href')
    assert(len(new_items)==len(new_urls))
    return zip(new_items,new_urls)
    
def spider(url):
    i=0
    print ("downloading ", url)
    mypage=requests.get(url).content.decode("gbk")
    mypageresults=page_info(mypage)
    save_path=u"网易新闻抓取"
    filename=str(i)+"_"+u"新闻排行榜"
    stringlistsave(save_path,filename,mypageresults)
    i+=1
    for item,url in mypageresults:
        print ("downloading",url)
        #print ("aaa")
        new_page=requests.get(url).content.decode("gbk")
        newpageresults=new_page_info(new_page)
        filename=str(i)+"_"+item
        stringlistsave(save_path,filename,newpageresults)
        i+=1
    
if __name__=='__main__':
    print ("start")
    start_url="http://news.163.com/rank/"
    spider(start_url)
    print ("end")