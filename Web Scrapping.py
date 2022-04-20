#!/usr/bin/env python
# coding: utf-8

# In[12]:


from platform import python_version
print(python_version())


# In[15]:


from bs4 import BeautifulSoup


# In[26]:


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException


# In[59]:


driver = webdriver.Chrome(executable_path=r"C:/Users/Madhu/.wdm/drivers/chromedriver/win32/100.0.4896.60/chromedriver.exe")


# In[55]:


driver = webdriver.Chrome(ChromeDriverManager().install())


# In[60]:


driver.get('https://www.giiresearch.com/material_report.shtml')


# In[61]:


Product_code=[] 
Market_Name=[] 
Published_by=[]
Published_date=[]


# In[46]:


html_source= '''
<a href="https://www.giiresearch.com/material_report.shtml">Converting File Size in Python</a> 
'''


# In[62]:


soup = BeautifulSoup(html_source, 'html.parser')
el = soup.find(href=True)
print(el['href'])


# In[69]:


content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'https://www.giiresearch.com/material_report.shtml'}):
    product=a.find('div', attrs={'class':'plist_codeinfo'})
    Market=a.find('div', attrs={'class':'list_title'})
    Publishedby=a.find('div', attrs={'class':'plist_pubinfo'})
    Publisheddate=a.find('div', attrs={'class':'plist_dateinfo'})
    Product_code.append(product.text)
    Market_Name.append(Market.text)
    Published_by.append(Publishedby.text)
    Published_date.append(Publisheddate.text)


# In[64]:


python web-s.py


# In[70]:


df = pd.DataFrame({'Product_code':product,'Market_Name':Market,'Published_by':Publishedby,'Published_date':Publisheddate}) 
df.to_csv('Material_Market.csv', index=False, encoding='utf-8')

