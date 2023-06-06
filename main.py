from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd 

driver = webdriver.Firefox()

driver.get('https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787')
driver.implicitly_wait(30)

table = driver.find_element(By.CLASS_NAME, 'datatable')
thead = table.find_element(By.TAG_NAME, 'thead')
tbody = table.find_element(By.TAG_NAME, 'tbody')

fields = []
data=[]

temp = []
for e in thead.find_elements(By.TAG_NAME, 'th'):
    if e.text != '':
        temp.append(e.text)
fields.append(temp)

for e in tbody.find_elements(By.TAG_NAME, 'tr'):
    temp = []
    for detail in e.find_elements(By.TAG_NAME, 'td'):
        temp.append(detail.text)
    data.append(temp)

searpost = {'Sr.No.':[i for i in range(1, 6)], 'Est. Value Notes':["NA"]*5, 'Description':[i[2] for i in data][0:5], 'Closing Date':[i[4] for i in data][0:5]}
       
dataframe = pd.DataFrame(searpost).set_index('Sr.No.')

dataframe.to_csv('Search Postings.csv') 