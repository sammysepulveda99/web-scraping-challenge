#!/usr/bin/env python
# coding: utf-8


    #Importing dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def scrape():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)



    # **Mars News**



    #Future reference for self, do NOT close the browser that just opened on the previos code! It won't open itself again
    #Retrieving data fron redplanetscience.com
    url = 'https://redplanetscience.com/'
    browser.visit(url)



    #Starting the beautiful soup with html
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')



    #Getting the latest news title
    news_title = soup.find("div", class_="content_title").get_text()
    print(news_title)




    #Getting latest Article Text along with News Title
    news_p = soup.find("div", class_ ="article_teaser_body").text
    print(news_p)




    #browser.quit()
    #Not done yet so I'm not running it


    # **JPL Mars Space Images (Featured Image)**



    #Retrieving data fron redplanetscience.com
    url = 'http://spaceimages-mars.com/'
    browser.visit(url)




    #Starting the beautiful soup with html
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')




    #Using soup to find header and its featured image
    image = soup.find("div", class_="header")
    f_image = image.find("img", class_="headerimage")["src"]
    featured_image_url = url + f_image
    print(featured_image_url)
    #Aw, a beautiful dusty cloud



    #browser.quit()
    #Not done yet so I'm not running it


    # **Mars Facts**


    #Retrieving data fron redplanetscience.com
    url = 'https://galaxyfacts-mars.com'
    browser.visit(url)




    #Reading the table to see columns and size
    tables = pd.read_html(url)
    tables



    #Transforming table to df
    tables = pd.read_html(url)
    mars_facts_df = tables[0]
    mars_facts_df.head(5)



    #Checking our column names
    mars_facts_df.columns



    #A fixed column name can't be written so it is better to get it from a function because it is not the same as the table goes
    #We get the first values as the name for the columns
    mars_facts_df.columns = mars_facts_df.iloc[0]
    mf_2 = mars_facts_df.iloc[1:]
    mf_2




    #Setting our index with set index function 
    mf_2.set_index('Mars - Earth Comparison', inplace = True)




    #Use Pandas to convert the data to a HTML table string
    html_table = mars_facts_df.to_html()
    html_table


    #Export to html code
    #Note to future self, use the DATAFRAME not the previous table since it is already in html
    mf_2.to_html('table.html')



    #browser.quit()
    #Not done yet so I'm not running it


    # **Mars Hemisphere**



    #Retrieving data fron redplanetscience.com
    url = 'https://marshemispheres.com'
    browser.visit(url)



    #Starting the beautiful soup with html
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')



    #Finding the items
    items = soup.find_all('div', class_='item')




    #Dictionary created to store all items
    hemisphere = []



    #Running for function to go through all items
    for x in items: 
        #Finding our hemisphere title
        title_item = x.find('h3').text
        find_href =  x.find('a')['href']
        linksies = 'https://marshemispheres.com/' 
        image_url = linksies + find_href
        #Making sure our browser visits the image url we just created with the find function and the variable containing the link
        browser.visit(image_url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        image = soup.find('div', class_='downloads').find('ul').find('li').find('a')['href']
        final_image = linksies + image
        hemisphere.append({'Title':title_item, 'Image_Url':final_image})
        
    print(hemisphere)
    #Wow this for almost killed my spirit
    #Note to self, if you run it over and over it piles links ontop, so run it from the start each time



    #Directionary retry
    mars={
        'news_title': news_title,
        'news_p': news_p,
        'featured_image_url': featured_image_url,
        'mars_facts':html_table,
        'hemisphere_images': hemisphere
    }
    #Closing our browser
    browser.quit()

    return mars



