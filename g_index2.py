import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By

print('可能会有点慢哈(大概是网络的问题吧)，得耐心等chrome“转”完，实在转不出来也别干耗着')
url = input('所查询作者的引文报告地址：')
print('在转了，在转了...')
driver = uc.Chrome()
# driver.get('https://www.webofscience.com/wos/alldb/basic-search')
driver.get(url)
# driver.get('https://www.webofscience.com/wos/woscc/citation-report/30be9f42-cf19-411b-a862-df79ea8c514a-8a33c5f5')
print(driver.title)

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
