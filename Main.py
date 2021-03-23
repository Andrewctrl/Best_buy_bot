import time
from selenium import webdriver
driver = webdriver.Chrome()
#signs in the best buy with the account 
# ealry march 
def setup():
    driver.find_element_by_xpath('/html/body/div[2]/div/div/header/div[2]/div[2]/div/nav[2]/ul/li[1]/button/div[2]/span').click() # pressesthe account 
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/header/div[2]/div[2]/div/nav[2]/ul/li[1]/div/div/div/div/div[2]/div/div/a').click() # presses the sign in button 
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[1]/div/input').send_keys(email)
    driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[2]/div/div/input').send_keys(bestBuypass)
    driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[4]/button').click()

#driver.get('https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402')
driver.get('https://www.bestbuy.com/site/pny-nvidia-geforce-gt-710-verto-2gb-ddr3-pci-express-2-0-graphics-card-black/5092306.p?skuId=5092306')
#driver.get('https://www.bestbuy.com/site/ibuypower-trace-mr-gaming-desktop-intel-i5-10400f-8gb-memory-nvidia-geforce-gtx-1650-4gb-240gb-ssd-1tb-hdd/6436829.p?skuId=6436829')
#driver.get('https://www.bestbuy.com/site/evga-geforce-rtx-3080-ftw3-gaming-10gb-gddr6x-pci-express-4-0-graphics-card/6436191.p?skuId=6436191')
buyButton = False
#shipping information 
first_name = 'Andrew'
last_name = 'Li'
address = ''
city = 'San Francisco'
state = 'CA'
zip_code = ''
email = ''
phone = ''
bestBuypass = ''
# WebElement.sendKeys(Keys.RETURN);    - example on how to use return link ---> https://stackoverflow.com/questions/1629053/typing-the-enter-return-key-using-python-and-selenium

setup() 
time.sleep(2)                              
while not buyButton:
    try: # when the buyButton isn't false it trys out this scrpit 
        # shows finds the button by id 
        addToCartBtn = addButton = driver.find_elements_by_class_name('btn-disabled')

        #shows that the button couldn't be clicked
        print("Button isn't ready")

        #refreh page after a delay 
        time.sleep(1)
        driver.refresh()

    except: # if you can press the button then uses tehis script 
        addToCartBtn = addButton = driver.find_element_by_class_name('btn-primary')
        
        #clicks the button 
        print('Button was clicked')
        addToCartBtn.click()
        buyButton = True 
        time.sleep(2)
        # presses the go to cart button 
        driver.find_element_by_xpath('/html/body/div[7]/div/div[1]/div/div/div/div/div[1]/div[3]/a').click()
        time.sleep(1)
        # presses the button for free shipping 
        #driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[1]/div[4]/ul/li/section/div[2]/div[2]/form/div[2]/fieldset/div[2]/div[1]/div/div/div/input').click()
        #time.sleep(1)
        # press the check out button 
        driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button').click()
        time.sleep(1)                  
        # the visa codes 
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div/div[2]/div/input').send_keys() # send in the cvt code 
        # press the place order button 
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/div/div[4]/div[3]/div/button').click()
