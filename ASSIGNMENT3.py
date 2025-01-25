from selenium import webdriver
import time
import re
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()

link_dict={}

driver.get('https://www.daraz.com.bd/routers/?page=1')
driver.maximize_window()
total_number_of_page=driver.find_element(By.CSS_SELECTOR,'#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div.xYcXp > div > div.Ck3Nt > div > div > span:nth-child(1)').text
print(f'Total :{total_number_of_page}')
numbers = int(re.findall(r'\d+', total_number_of_page)[0])
total_number_of_page=round(numbers/40)
print(total_number_of_page)


for page_no in range(1,3):
    driver.get(f'https://www.daraz.com.bd/routers/?page={page_no}')
    driver.maximize_window()

    for prod in range(1,41):
        try:
            type_p=str(prod)
            link=driver.find_element(By.CSS_SELECTOR,'#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child('+type_p+') > div > div > div.buTCk > div.RfADt > a').get_attribute('href')
            link_dict[f'page_no_{page_no}_product_{prod}']=link
        except Exception as e :
            print(f"Error processing Page {page_no},product {prod}: {e}")

print(link_dict)
print(len(link_dict))



time.sleep(30)
driver.quit()