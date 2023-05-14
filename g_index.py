# Chrome_version: 113.0.5672.93（正式版本） （64 位）
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:/Program Files/Google/Chrome/Application/chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)
print(driver.title)

# H_index的Xpath
# /html/body/app-wos/main/div/div/div[2]/div/div/div[2]/app-input-route/app-citation-report/div[2]/div[4]/div[2]
H_index = driver.find_elements(By.XPATH, '/html/body/app-wos/main/div/div/div[2]/div/div/div['
                                         '2]/app-input-route/app-citation-report/div[2]/div[4]/div[2]')
for i in H_index:
    print('H_index: ', i.text)

# G_index的Xpath
# /html/body/app-wos/main/div/div/div[2]/div/div/div[2]/app-input-route/app-citation-report/div[3]/table/tr[5]/td[8]/a
# /html/body/app-wos/main/div/div/div[2]/div/div/div[2]/app-input-route/app-citation-report/div[3]/table/tr[6]/td[8]/a
n = 5
m = 1
sum_citation = 0

while 1:
    pre_citation = driver.find_elements(By.XPATH, '/html/body/app-wos/main/div/div/div[2]/div/div/div['
                                              '2]/app-input-route/app-citation-report/div[3]/table/tr[%s]/td[8]/a' % n)
    for i in pre_citation:
        sum_citation = sum_citation + int(i.text)
        if sum_citation <= m*m:
            print('G_index: %s' % str(m))
            exit()
    n = n+1
    m = m+1
