from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time

def get_content1(url):
    driver = Chrome()

    driver.get(url)
    time.sleep(20)

    shadow_host = driver.find_element(By.CSS_SELECTOR, '.sl-layout-content-container')
    shadow_root = shadow_host.shadow_root
    # 获取所有 class 为 sl-content-name 的标签
    shadow_content = shadow_root.find_element(By.CSS_SELECTOR, '.sl-vm-object-bp-container')

    html_content = shadow_content.get_attribute('innerHTML')
    # print("HTML Content:", html_content)
    with open('temp.html', 'w+', encoding='utf-8') as f:
        f.write(html_content)
        f.close()

    driver.quit()

def get_content2(url):
    driver = Chrome()

    driver.get(url)
    time.sleep(2)

    shadow_host = driver.find_element(By.CSS_SELECTOR, '.sl-layout-content-container')
    shadow_root = shadow_host.shadow_root
    # 获取所有 class 为 sl-content-name 的标签
    shadow_content = shadow_root.find_element(By.CSS_SELECTOR, '.sl-two-column-container')

    html_content = shadow_content.get_attribute('innerHTML')
    # print("HTML Content:", html_content)
    with open('temp.html', 'w+', encoding='utf-8') as f:
        f.write(html_content)
        f.close()

    driver.quit()

def get_content3(url):
    driver = Chrome()

    driver.get(url)
    time.sleep(2)

    dict = {}
    shadow_host = driver.find_element(By.CSS_SELECTOR, '.sl-layout-content-container')
    shadow_root = shadow_host.shadow_root
    # 获取所有 class 为 sl-content-name 的标签
    shadow_content1 = shadow_root.find_element(By.CSS_SELECTOR, '.sl-svp')
    shadow_content1.get_attribute('innerHTML')
    dict['svp'] = shadow_content1.get_attribute('innerHTML')

    shadow_content2 = shadow_root.find_element(By.CSS_SELECTOR, '.sl-parent-description')
    dict['parent_description'] = shadow_content2.get_attribute('innerHTML')

    shadow_content3 = shadow_root.find_element(By.CSS_SELECTOR, '.sl-description')
    dict['description'] = [i.get_attribute('innerHTML') for i in shadow_content3.find_elements(By.CSS_SELECTOR, 'li')]

    driver.quit()
    return dict
