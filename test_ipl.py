from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.iplt20.com/points-table/men')
driver.maximize_window()
wait = WebDriverWait(driver, 10)
try:
    accept_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Accept cookies')]")))
    accept_button.click()
except:
    # If the button doesn't appear, just continue
    pass

row = driver.find_elements(By.XPATH, "//tbody[@id='pointsdata']/tr")

element_list = []
for i in row:
    data = []
    for j in i.find_elements(By.TAG_NAME, "td"):
        data.append(j.text)
    element_list.append(data)

dict_count_W = {}

for i in element_list:
  is_match = i[-1].split('\n')
  count_w = is_match.count('W')
  dict_count_W[i[2]] = count_w

Max_val = max(dict_count_W.values())
Max_won = {k:v for k,v in dict_count_W.items() if v == Max_val}

print(Max_won)