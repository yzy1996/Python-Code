# *-* coding: utf-8 *-*
import BeautifulSoup
import requests
import time

# to check if the ip proxy can work
URL_CHECK = 'http://1212.ip138.com/ic.asp'
RESPONSE_TIME = 2
IP_LOCAL = '120.236.174.144'

# this is the pages of the website "http://www.ip181.com/daili/1.html"
# you can check out in the browser.
# the program will crawl the ip proxy from pages [start_page, end_page]
# as: [1,2], it will crawl the page 1 and page 2.
start_page = input('Please input your start page to crawl: ')
end_page = input('Please input your end page to crawl: ')


s = requests.Session()

# check if the exit IP is changed
def check_a_ip(ip):
    start = time.time()
    try:
        connection = s.get(URL_CHECK, headers={
            'Host': '1212.ip138.com',
            'Referer': 'http://www.ip138.com/',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        }, proxies={'http': 'http://' + ip}, timeout=RESPONSE_TIME)
        res = connection.content
        # print res

        soup = BeautifulSoup.BeautifulSoup(res)
        ip_return = soup.findAll('center')[0].text.split('[')[1].split(']')[0]
        return ip_return != IP_LOCAL, '%.6f' % (time.time() - start)
    except Exception:
        # print '<ERROR>'
        # print e
        return False, '-1'

url = 'http://www.ip181.com/daili/%s.html'
ip_proxy_file = open('proxy.txt', 'w')
ip_proxy_file.write('ip_port,response_time\n')
ip_proxy_file.close()

for i in range(int(start_page), int(end_page) + 1):
    ip_proxy_file = open('proxy.txt', 'a')

    connection_crawl = s.get(url % str(i),headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        })
    soup_crawl = BeautifulSoup.BeautifulSoup(connection_crawl.content)

    # parse each page,find the good ip proxy
    trs = soup_crawl.findAll('tr')
    for tr in trs[1:len(trs)]:
        tds = tr.findAll('td')
        ip = tds[0].contents[0] + ':' + tds[1].contents[0]
        is_good, res_time = check_a_ip(ip)
        if is_good:
            ip_proxy_file.write(ip + ',' + res_time + '\n')

    print('%s : Finish to crawl the page %d.  %s' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), i, url % str(i)))
    ip_proxy_file.close()