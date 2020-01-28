# Author: Kevin
# File: slickdeals.py
# Modification: - Added ability to modulate the url.
#               - Added quit browser command
#               - Added beautiful soup command to scrape url
#               - Added a way to save product title.

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

import mongodbConnect

class SlickdealScraper(object):
    def __init__(self, category, cat_nav):
        self.driver = webdriver.Chrome()
        
        # If urls doesn't work without deals/, check url with deals/. If link doesn't work afterwards, then link is not valid.
        self.url_deals = "deals/"       
        self.url = f"https://slickdeals.net/{self.url_deals}{category}/?src=catnav_{cat_nav}"
        
        # Delay given to webdriver in case it needs to catchup in loading before attempting to scrape the page.
        self.delay = 10
    def load_slickdeals_url(self):
        self.driver.get(self.url)
        try:
            wait = WebDriverWait(self.driver, self.delay)
            
            # Wait until a specific element, ID is searched
            wait.until(EC.presence_of_element_located((By.ID, "fpMainContent")))
            #print ("Page is ready")
        except TimeoutException:
            print ("Loading not complete yet or cannot find ID")
    
    def extract_product_title(self):
        all_post = self.driver.find_elements_by_class_name("fpItem  ")
        #print(all_post)
        title_list = []
        #frontpage_or_popular = []
        # company_brand = []
        # product_title = []
        # price = []
        
        for post in all_post:
            print (post.text)
            post_information = post.text
            
            post_information.split("\n")
            
            print("FP Deals: " + post_information)
            # print("Brand: ")
            # print("Title: ")
            # print("Price: ")
            
            
            title_list.append(post.text)
        return (title_list)
    
    def extract_product_urls(self):
        url_list = []
        page_html = urllib.request.urlopen(self.url)
        soup_scraping = BeautifulSoup(page_html, "lxml")
        
        for product_links in soup_scraping.findAll("a", {"class": "itemTitle"}):
            href_portion = str(product_links["href"])
            completed_url = f"https://www.slickdeals.net{href_portion}"
            url_list.append(completed_url)
            print(completed_url)
        return (url_list)

    def quit_driver(self):
        self.driver.close()
            

if (__name__=="__main__"):
    category = "tech"
    cat_nav = "tech"

    slick_deals = SlickdealScraper(category, cat_nav)
    slick_deals.load_slickdeals_url()
    slick_deals.extract_product_title()
    #slick_deals.extract_product_urls()
    slick_deals.quit_driver()