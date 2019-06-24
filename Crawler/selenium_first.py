from selenium import webdriver
import time

# http://httpbin.org/get
with open('ip.txt') as f:
    lines = (line.strip() for line in f)
    ip = list(lines)

with open('user_agent.txt') as f:
    lines = (line.strip() for line in f)
    user_agent = list(lines)

# 添加配置
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36")
options.add_argument("proxy-server=http://117.191.11.105:8080")

# 创建浏览器驱动
driver = webdriver.Chrome(chrome_options=options)
driver.get("http://httpbin.org/get")

# input = driver.find_element_by_css_selector('#kw')
# input.send_keys("如吉生物")

# button = driver.find_element_by_css_selector('#su')
# button.click()

print(driver.page_source)
time.sleep(10)
driver.quit()