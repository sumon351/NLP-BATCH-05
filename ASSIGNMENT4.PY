from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--incognito")
driver=webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://www.daraz.com.bd/products/4g-wifi-i468701703-s2256167219.html')

height=driver.execute_script('return document.body.scrollHeight')
print(height)

for i in range(0,height+2000,30):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)
# 4G Wifi Airport Router with Battery black colur    
h1=driver.find_element(By.CLASS_NAME,'pdp-mod-product-badge-title').text
print(h1)  
# product price 
price=driver.find_element(By.XPATH,'//*[@id="module_product_price_1"]/div/div/span').text
print(price)  

# product details 
prod_details = driver.find_element(By.XPATH,'//*[@id="module_product_detail"]/div/div/div[1]/div[1]/ul/li[1]').text
print(prod_details)

# rating 
rating=driver.find_element(By.CLASS_NAME,'score').text
print(rating)

# comments scraping 
all_comments=driver.find_elements(By.CLASS_NAME,'content')
for i in all_comments:
    print(i.text)

time.sleep(60)
driver.quit()