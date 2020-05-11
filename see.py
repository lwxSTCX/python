#coding=UTF-8
import requests
import os
import sys
import threading
import queue

list_name=sys.argv[1]
num=int(sys.argv[2])

quit=queue.Queue()
threading_num= num

url_list=open(list_name,'r')
lines=url_list.readlines()
url_list.close()

for line in lines:
        line=line.rstrip()
        quit.put(line)

def crawler():
        while not quit.empty():
                url=quit.get()
                try:
                        requests.packages.urllib3.disable_warnings()
                        urlx= url+'/seeyon/htmlofficeservlet'
                        r = requests.get(urlx,timeout=10,verify=False)
                        
                        if 'DBSTEP' in r.content:
                            print url + "-----" + "success"
                            fw=open("success.txt","a")
                            fw.write(url+"\n")
                            fw.close()
                        else:
                            print url + "-----" + "error"
                except requests.RequestException as e:
                        pass

if __name__ == '__main__':
    for i in range(threading_num):
        t = threading.Thread(target=crawler)
        t.start()
