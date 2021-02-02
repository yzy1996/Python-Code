from selenium import webdriver
import time
import random

with open('ip.txt') as f:
    lines = (line.strip() for line in f)
    ip = list(lines)

with open('user_agent.txt') as f:
    lines = (line.strip() for line in f)
    user_agent = list(lines)

# http://httpbin.org/get
count = 0
for i in range(len(ip)):
    try:
        # 添加配置
        options = webdriver.ChromeOptions()
        options.add_argument('User-Agent=' + random.choice(user_agent))
        options.add_argument('proxy-server=http://' + ip[i])

        # 创建浏览器驱动
        driver = webdriver.Chrome(chrome_options=options)
        driver.get("http://www.baidu.com")

        input = driver.find_element_by_css_selector('#kw')
        input.send_keys("如吉生物")

        button = driver.find_element_by_css_selector('#su')
        button.click()

        # print(driver.page_source)
        time.sleep(10)
        print(str(count) + 'times')
        count = count + 1
        driver.quit()

    except Exception:  # 其他异常
        driver.quit()
        print('Retry')


        