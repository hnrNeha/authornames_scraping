# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 20:53:14 2023

@author: hnrne
"""
import pandas
import sqlite3
from itertools import zip_longest
from selenium import webdriver
from time import sleep
import csv
path = r'C:\Users\hnrne\Downloads\chromedriver_win32\chromedriver'
# open the browser
browser = webdriver.Chrome(executable_path=path)
# load the webpage
browser.get('https://www.theverge.com/')
browser.maximize_window()
# get the input elements
#input_search = browser.find_element_by_id('twotabsearchtextbox')
#search_button = browser.find_element_by_xpath("(//input[@type='submit'])[1]")
# send the input to the webpage
#input_search.send_keys("Smartphones under 10000")
#sleep(1)
#search_button.click()
ids = []
urls=[]
headings=[]
authors=[]
dates=[]
total=[]
#for i in range(10):
   # print('Scraping page', i+1)
urlclass = browser.find_elements_by_xpath("//a[@class='group-hover:shadow-underline-franklin']")
url = [link.get_attribute("href") for link in urlclass]

author= browser.find_elements_by_xpath("//a[@class='text-gray-31 hover:shadow-underline-inherit dark:text-franklin mr-8']")
date = browser.find_elements_by_xpath("//span[@class='text-gray-63 dark:text-gray-94']")
    
   
for p in urlclass:
        url = p.get_attribute("href")
        urls.append(url)
        headings.append(p.text)
for i in author:
        authors.append(i.text)
for k in date:
        dates.append(k.text)
for j in range(0,len(urls)):
    ids.append(j)
        
    
    

header=['id','URL','headline','author','date']
data=[ids,urls,authors,dates]
with open(r"C:\Users\hnrne\Downloads\ddmmyyy_verge.csv", 'w', newline='',encoding='UTF8') as output_file:
    dict_writer = csv.writer(output_file)
    dict_writer.writerow(header)
    for row in zip(ids,urls,headings,authors,dates):
        dict_writer.writerow(row)
df = pandas.read_csv(r"C:\Users\hnrne\Downloads\ddmmyyy_verge.csv")
con = sqlite3.connect("scraping.db")
table_name="new"
df.to_sql(table_name, con, if_exists='append', index=False)


