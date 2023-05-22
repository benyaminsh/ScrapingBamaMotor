from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep,time
import json

start_time = time()


driver = webdriver.Firefox()


driver.get('https://bama.ir/sell/motorcycle')
sleep(2)
brands = driver.find_elements(By.CSS_SELECTOR,'#__layout > div > div.main-wrapper.sell-type-wrapper > div > div > div.content.firstStep > div > div > div > button')


d = []
# e = 0
    
for b in range(1,len(brands)+50):
    try:
        brand_slug = driver.find_element(By.CSS_SELECTOR,'#__layout > div > div.main-wrapper.sell-type-wrapper > div > div > div.content.firstStep > div > div > div > button').get_attribute('data-trackervalue')
        brand = driver.find_element(By.CSS_SELECTOR,f'#__layout > div > div.main-wrapper.sell-type-wrapper > div > div > div.content.firstStep > div > div > div > button:nth-child({b}) > span > span')
        brand_name = "".join( str(brand.get_attribute('textContent')).split()[0])
        sleep(1)
        brand.click()
        sleep(1)
        models_data = []
        models = driver.find_elements(By.CSS_SELECTOR,'#__layout > div > div.main-wrapper.sell-type-wrapper > div > div > div.content > div > div > div > button')

        
        for m in range(1,len(models)+50):
            try:
                model_slug = str(driver.find_element(By.CSS_SELECTOR,f'#__layout > div > div.main-wrapper.sell-type-wrapper > div > div > div.content > div > div > div > button:nth-child({m})').get_attribute('data-trackervalue')).replace(',',' ')
                model = driver.find_element(By.CSS_SELECTOR,f'#__layout > div > div.main-wrapper.sell-type-wrapper > div > div > div.content > div > div > div > button:nth-child({m}) > span > span')
                model_name = str(model.get_attribute('textContent')).strip()
                models_data.append({'name': model_name,'slug': model_slug,'name_en': model_slug.capitalize()})
            except:
                continue
            
        d.append({'name': brand_name,'slug': brand_slug,'name_en': str(brand_slug).capitalize(),'models': [ {'name': m['name'],'slug': m['slug'],'name_en': m['name_en']} for m in models_data]})
        back = driver.find_element(By.CSS_SELECTOR,'.prev-step').click()
        sleep(1)
        # e += 1
        # if e == 7:
        #     break
    except:
        continue



jsonString = json.dumps(d, ensure_ascii=False,indent=4)
jsonFile = open("dataMotor.json", "w",encoding='utf-8')
jsonFile.write(jsonString)
jsonFile.close()


driver.close()

end_time = time()

print(f'End Time : {round(end_time-start_time)}S')