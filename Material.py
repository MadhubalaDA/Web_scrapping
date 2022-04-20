import os
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv


class Material():

    def __init__(self):

        self.current_path = os.getcwd()
        self.url = 'https://www.giiresearch.com/material_report.shtml'
       
        self.driver = webdriver.Chrome(executable_path=r"C:/Users/Madhu/.wdm/drivers/chromedriver/win32/100.0.4896.60/chromedriver.exe")

    def page_load(self):

        self.driver.get(self.url)

        
        page_html = self.driver.page_source
        
        self.soup = BeautifulSoup(page_html, 'html.parser')

    def create_csv_file(self):

     
	with open('Material.csv', 'w', newline='') as file:
    	   writer = csv.writer(file)
           rowheaders = ['Product_code','Market_Name','Published_by', 'Published_date']
           writer.writerow(rowheaders)
           for data in datas:
               writer.writerow(data)


    def data_scrap(self):

        
        soup = (self.soup.find_all('div', class_='wrapper')) 
        for i in soup:
            product = i.find('div', class_='plist_codeinfo')
            Market= i.find('div', class_='list_title')
            Publishedby = i.find('div', class_='plist_pubinfo')
            Publisheddate = i.find('div', class_='plist_dateinfo')
            
            self.mycsv.writerow({'Product_code':product,'Market_Name':Market,'Published_by':Publishedby,'Published_date':Publisheddate})

    def tearDown(self):

        
        self.driver.quit()
       
        self.file_csv.close()

if __name__ == "__main__":

    Material = Material()
    Material.page_load()
    Material.create_csv_file()
    Material.data_scrap()
    Material.tearDown()