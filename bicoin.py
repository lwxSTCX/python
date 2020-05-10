#coding=utf-8

import requests
import re
import json
import base64
import sys
import sys

reload(sys)

sys.setdefaultencoding('utf8')

headers={
        'Host': 'blz.bicoin.com.cn',
        'Connection': 'keep-alive',
        'Origin': 'https://test1.bicoin.info',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/521.26 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.410',
        'Referer': 'https://test1.bicoin.info/place-mgr/notice/report',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',

}
cookies={'Cookie': 'JSESSIONID=B606540911AD2964C5C6662AC23D9410'}

def crawler(url):
    html=requests.get(url=url,headers=headers,cookies=cookies)
    content=json.dumps(html.content,indent=2).decode('unicode_escape')
    content1=content.replace(',"dialog":{"cancelAndClose":false,"cancelBtn":"","cancelColor":"","code":"0","confirmBtn":"","confirmColor":"","content":"","contentColor":"","time":"","title":"OK","titleColor":"","type":"3","url":""}}"','')
    content2=content1.replace('"{"code":0,"data":{"totalPage":4,"dataList":','')
    l=0
    with open('C:\Users\TR\Desktop\sfile\\123.txt', 'w') as f:
        for s in content2.split():
            if '0.00%' not in s:
                l=l+1
                news=s
                t1=re.findall('"endTime":(.*?),"exchange":', news)
                str2="".join(t1)
                str1 = 'uTime":' + str2
                if str2 in s:
                    f.write(news+'\n')
    chuli()

def chuli():
    l=[]
    j=0
    with open('C:\Users\TR\Desktop\sfile\\123.txt', 'r') as f:
        for i in f.readlines():
            l.append(i)
            if 'endTime' in i:
                print l[0]
if __name__ == '__main__':
    for i in range(1,2):
        url='https://blz.bicoin.com.cn/transactOrder/bigOrder/get24DataInfoList?coin=BTC&pageSize=20&continueTimeType=2&dealRatioType=0&limitTimeType=0&limitAmountType=3&pageNum='+str(i)
        crawler(url=url)