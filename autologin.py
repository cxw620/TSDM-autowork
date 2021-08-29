# 2021-07-05 学习浏览器程序化控制练手之作
# Copyright @WENJUNXIN
import pickle
import time

from selenium import webdriver

driver = webdriver.Edge(executable_path="E:\\Live\\Auto Login\\msedgedriver.exe")


def getCookies(relogin):
    url = "https://www.tsdm39.net/forum.php"
    driver.get("https://www.tsdm39.net/member.php?mod=logging&action=login")
    while driver.current_url != url:
        pass
    try:
        outputPath = open("sgCookies.pickle", "wb")
        pickle.dump(driver.get_cookies(), outputPath)
        outputPath.close()
        driver.quit()
    except:
        print("Get cookies Error!")
        driver.close()
    if relogin:
        login()


def login():
    global Cookies
    try:
        readPath = open("sgCookies.pickle", "rb")
        Cookies = pickle.load(readPath)
    except:
        getCookies(relogin=True)
    driver.get("https://www.tsdm39.net/forum.php")
    driver.delete_all_cookies()
    for cookie in Cookies:
        # k代表着add_cookie的参数cookie_dict中的键名，这次我们要传入这5个键
        for k in {'name', 'value', 'domain', 'path', 'expiry'}:
            # cookie.keys()属于'dict_keys'类，通过list将它转化为列表
            if k not in list(cookie.keys()):
                # saveCookies中的第一个元素，由于记录的是登录前的状态，所以它没有'expiry'的键名，我们给它增加
                if k == 'expiry':
                    t = time.time()
                    cookie[k] = int(t)  # 时间戳s
        # 将每一次遍历的cookie中的这五个键名和键值添加到cookie
        driver.add_cookie({k: cookie[k] for k in {'name', 'value', 'domain', 'path', 'expiry'}})
    driver.get("https://www.tsdm39.net/forum.php")
    # 实际上，cookies可能过期。这里可能需要加上登陆状态检测

def arubaito():
    driver.get("https://www.tsdm39.net/plugin.php?id=np_cliworkdz:work")


def sign():
    driver.get("https://www.tsdm39.net/plugin.php?id=dsu_paulsign:sign")


# getCookies()
login()

# class autoOperation:
#     def getNsInput(self):
#         inputTemp = input("请输入你想自动填入的字段的名称：")
#         inputTemp = str(inputTemp)
#         try:
#             print("你输入的字段是：",inputTemp)
#             try:
#                 outputPath = open("inputTemp.pickle", "wb")
#                 pickle.dump(inputTemp, outputPath)
#                 os.rename("inputTemp.pickle", os.path.join(inputTemp, ".pickle"))
#                 outputPath.close()
#             except:
#                 print("Failed!")
#         except:
#             print("输入数据有误，请重新输入！")
#             exit(1)


# driver.find_element_by_class_name("username")

# time.sleep(random.random()+1)
#

# time.sleep(random.random()+1)
#
# driver.find_element_by_css_selector("[class='blink blue category-toggle']").click()
# # 有时候，遇到“blink blue category-toggle”这种带空格的class名，直接find_element_by_class_name会报错，此时请使用上面的方法
# time.sleep(random.random()+1)
#
# driver.find_element_by_class_name("name").click()
# time.sleep(random.random()+1)
#
# driver.find_element_by_css_selector("[class='btn live-btn']").click()
# # 有时候，遇到“blink blue category-toggle”这种带空格的class名，直接find_element_by_class_name会报错，此时请使用上面的方法
# time.sleep(random.random()+1)
#
# # 完成了，关闭浏览器即可