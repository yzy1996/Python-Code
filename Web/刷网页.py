#coding: utf-8

from urllib import request
from urllib import parse
import urllib.error
import time
from http import cookiejar
import threading
import linecache

#cj = http.cookiejar.CookieJar()
#opener = request.build_opener(request.HTTPCookieProcessor(cj), request.HTTPHandler)
#request.install_opener(opener)

THREAD_NUMBER = 2
IP_NUMBER = 20

url = ['http://yun.zjer.cn/index.php?r=space/person/show&sid=NID555912']

head = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
global count
count = 0
global count1
count1 = 0

lock = threading.Lock()


def brash(proxy_dict):
    #print(proxy_dict)
    global count
    global count1
    if count1 < 100:
        try:  #正常运行
            count = count + 1
            print(count, 'times')  #监视程序是否在正常运行，输出运行了多少次
            proxy_handler = request.ProxyHandler({'http': proxy_dict})
            opener = request.build_opener(proxy_handler)
            request.install_opener(opener)
            countUrl = len(url)
            for i in range(countUrl):  #遍历所有url
                req = request.Request(url[i], headers=head, method='POST')
                try:
                    #lock.acquire()
                    response = request.urlopen(req)  #访问网页
                    html = response.read().decode('utf-8')
                    print(html)
                    #lock.release()
                except urllib.error.URLError as e:
                    print(e.reason)
                    print("EEEEEE")
            #time.sleep(1)  #间隔执行

        except Exception:  #出现异常
            print('Retry')
            count1 = count1 + 1
            time.sleep(1)  #间隔执行
    else:
        print('much error')


def ReadSpecialLine(ipfilename, linenumber):
    proxy_dict = linecache.getline(ipfilename, linenumber).strip('\n')
    lock.acquire()
    #print(proxy_dict)
    print(linenumber)
    lock.release()
    return proxy_dict


#while True:  #让程序一直执行
def For_EveryThread(Thread_i):
    while True:
        for i in range(int(IP_NUMBER / THREAD_NUMBER)):
            linenumber = THREAD_NUMBER * i + Thread_i
            proxy_dict = ReadSpecialLine('ip.txt', linenumber)
            brash(proxy_dict)
    return


if __name__ == '__main__':
    count = 0
    count1 = 0
    thread_list = []
    start = time.clock()
    for Thread_i in range(THREAD_NUMBER):
        temp = threading.Thread(target=For_EveryThread, args=(Thread_i + 1, ))
        thread_list.append(temp)
    for t in thread_list:
        t.start()  # 开启线程
    for t in thread_list:
        t.join()  # 所有子线程都结束了主线程才关闭
    end = time.clock()
    print('用时：', str(end - start))
