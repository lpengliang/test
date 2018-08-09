#梨视频网站全部视频下载
import requests
from urllib.request import urlretrieve
import re
import os
import time
#获取页面源代码
#获取视频ID
#拼接url
#获取视频播放地址
#下载视频
#url="http://www.pearvideo.com/category_9"
def download(url):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    html = requests.get(url,headers=header).text
    #print (html)
    reg='<a href="(.*?)" class="vervideo-lilink actplay">'
    vedio_id=re.findall(reg,html)
    #print(vedio_id)
    straturl="http://www.pearvideo.com"
    vedio_url=[]
    for vid in vedio_id:
        newurl=straturl+"/"+vid
        #print(newurl)
        vedio_url.append(newurl)
    #print(vedio_url)
    #获取视频播放地址
    for playurl in vedio_url:
        phtml=requests.get(playurl).text
        reg='srcUrl="(.*?)"'
        purl=re.findall(reg,phtml)
        #print(purl)
        #获取视频名称
        reg='<h1 class="video-tt">(.*?)</h1>'
        vedio_name=re.findall(reg,phtml)
        print(vedio_name)
        print("正在下载视频：%s"%vedio_name[0])
        path="vedio"
        if path not in os.listdir():
            os.mkdir(path)
        #urlretrieve(purl[0], path + "/%s.mp4" % vedio_name[0])
        print(purl[0])
        #time.sleep(1)


#分析加载更多的情况
#http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=12
#http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=24
#http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=36
#发现每一次加载为12个视频
#编写下载更多函数
def downloadmore(category_id):
    n = 12
    while True:
        #以下载48个视频为例
        if n>48:
            return

        url="http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=%d&start=%d"%(category_id,n)
        n = n + 12
        download(url)

#downloadmore()

#获取所有栏目的视频
category=[9,10,1,2]
for category_id in category:
    downloadmore(category_id)