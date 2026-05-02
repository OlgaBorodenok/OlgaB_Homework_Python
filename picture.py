from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
wait = WebDriverWait(driver, 15)

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#image-container img")))

wait.until(EC.invisibility_of_element_located((By.ID, "spinner")))
    
pics = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    
if len(pics) >= 3:
        src_value = pics[2].get_attribute("src")
       
        print(f"Атрибут src третьей картинки: {src_value}")
        
driver.quit()