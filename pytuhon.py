from selenium import webdriver
import time
#
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-extensions')
options.add_argument("--incognito")
options.add_argument("--disable-plugins-discovery")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options, executable_path=r"R:\chromedriver.exe")

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
          const newProto = navigator.__proto__
          delete newProto.webdriver
          navigator.__proto__ = newProto
          """
})
driver.get("https://bot.sannysoft.com")
time.sleep(225)
driver.quit()