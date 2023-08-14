from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

# 替换为你的URL列表
url_list = [
    "https://www.polimi.it/",
    "https://www.polito.it/",
    "https://www.polimi.it/footer/policy/amministrazione-trasparente/altri-contenuti/altri-contenuti-procedura-di-segnalazione-illeciti",
    "https://twitter.com/?lang=zh",
    "https://github.com/tinyos/tinyos-main",
    "https://www.tencent.com/zh-cn/",
    "https://it.wikipedia.org/wiki/Tencent_Holdings",
    "https://www.tencentcloud.com/",
    "https://news.sky.com/story/ukraine-russia-war-latest-12541713",
    "https://ec.europa.eu/eurostat/web/products-eurostat-news/w/wdn-20230811-1",
    "https://www.skysports.com/football/transfer-paper-talk",
    "https://edition.cnn.com/2023/08/13/media/cbs-news-chief-is-out/index.html",
    "https://www.hust.edu.cn/",
    "https://www.tsinghua.edu.cn/",
    "https://scholar.google.com.hk/?hl=zh-CN",
    "https://ieeexplore.ieee.org/abstract/document/8418688/",
    "https://www.bbc.com/news/world"
    # ...添加更多URL
]

# 创建一个Chrome浏览器实例
driver = webdriver.Chrome()
initial_window = driver.current_window_handle
# 遍历URL列表
while 1==1:
    for url in url_list:
        try:

            # 打开URL
            driver.get(url)
            print(f"Visited {url}")

            # 在每个页面上停留7秒钟
            time.sleep(random.randint(7, 15))

            actions = ActionChains(driver)
            actions.send_keys(Keys.PAGE_DOWN).perform()

            time.sleep(random.randint(7, 15))

            actions = ActionChains(driver)
            actions.send_keys(Keys.PAGE_DOWN).perform()

            time.sleep(random.randint(7, 15))
        except Exception as e:
            with open("stop_flag.txt", "w") as flag_file:
                flag_file.write("1")

# 关闭浏览器
driver.quit()
