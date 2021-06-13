#Importing dependencies
import pymongo
import os
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

#Defining the browser
def my_browser():
#Making a path to the drive to be able to install ChromeDriverManager and access Chrome
    executable_path={'executable_path':ChromeDriverManager().install()
    }
    browser = Browser('chrome',**executable_path,headless=False)
    return browser
#Creating our dictionary
mars_dict = {}
#Defining and making the scrapper
def scraper_web_mars():
    try:
        browser = init_browser()
        url = 'https://redplanetscience.com/'
        #Make the browser access the url assigned
        browser.visit(url)
        #Browser format
        html = browser.html
        #Adding our BeautifulSoup
        soup = bs(html,'html.parser')
        #Finding the content title
        title_news = soup.find_all("div", class_ =  "list_text")[0].find("div", class_ = "content_title").text
        body_news = soup.find_all("div", class_ =  "list_text")[0].find("div", class_ = "article_teaser_body").text
        
        mars_dict['title_news'] = title_news
        mars_dict['body_news'] =body_news

        return mars_dict
    #Closing the browser
    finally:

        browser.quit()

#Defining our images

def scraper_web_mars_image():
    try:
        browser = init_browser()
        #Defining the url to use
        Url = "https://spaceimages-mars.com/"
        #Making sure the browser we created visits the URL
        browser.visit(url)
        #Browser format
        html = browser.html
        #Beggining our Beautiful Soup
        soup = bs(html, "html.parser")
        #First image url
        image_1 = soup.find("div", class_ = "header").find("div",  class_ = "floating_text_area").a.get("href")
        fimage_1 = url + image_1
        fimage_1

        mars_dict['fimage_1'] = fimage_1

        return mars_dict
    
    finally:
        #Always making sure to close the browser
        browser.quit()


#Geting our facts

def scrape_web_mars_facts():
    #Assigning the facts url
    url_facts = "https://galaxyfacts-mars.com/"
    #Assigning the url to a table
    table = pd.read_html(url_facts)
    #Creating a table 
    table_df = table[0]
    #Assigning column name to DF
    table_df.columns = ['Description','Value']
    #Setting our index with set index function 
    table_df.set_index('Description', inplace = True)
    #Making or df to html
    mars_data = table_df.to_html()
    #Adding mars_data to our
    mars_dict['mars_facts'] = mars_data

    return mars_dict

#Scrapping our hemisphere
def scrape_web_mars_hemisphere():
    try:
       #Setting up the browser
        browser = init_browser()
        #Defining the URL
        url_hemisphere = 'https://marshemispheres.com/'
        #Making sure the browser connects to the URL
        browser.visit(hemispheres_url)
        #Starting the SOUP
        soup = bs(browser.html, 'html.parser')
        #Finding the items
        items = soup.find_all('div', class_='item')
        h_image_urls = []
    #For function created so it goes through the items
        for x in items: 
            item_title = x.find('h3').text
            image_url = x.find('a', class_='itemLink product-item')['href']
            browser.visit(hemispheres_url + img_url_1)
            image_url = browser.html
            soup = bs( img_url_1, 'html.parser')
            img_url = hemispheres_url + soup.find('img', class_='wide-image')['src']
            h_image_urls.append({"Title" : item_title, "Image_URL" : image_url})

        mars_dict[h_image_urls] = hemisphere_image_urls
    
        return mars_dict
    
    finally:
        #Closing the browser ta-da
        browser.quit()