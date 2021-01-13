

###//////NASA Mars News###/// 
#  Collecting the latest news title and paragrpah text

# Dependencies
import os
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd
import time


def scrapeMars():

    nasa_scrape = {}

    ####////NASA Mars News Site URL\\\\####
    url= "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    requests.get(url)
    ##//NASA Mars News\\##

    #Creating the path and enabling the pages's js and creating the soup object
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path)
    browser.visit(url)
    time.sleep(2)

    #Creating BeautifulSoup object
    html = browser.html
    news_soup = bs(html, 'html.parser')

    print("News Title and Paragraph Scrape...")

    # Scraping the article parent
    div_id_parent = news_soup.select_one("ul.item_list")

    #Scraping the title
    news_title = div_id_parent.find_all('div', class_="content_title")
    
    #Scraping the body
    news_p = div_id_parent.find_all('div', class_="article_teaser_body")
    
    #Loop for all titles and body section
    news_titles = []
    news_paras = []
    for i in range(len(news_p)):
        news_titles.append(news_title[i].text)
        news_paras.append(news_p[i].text)
    
    print("News Title and Paragraph Scrape Completed")

    ####////JPL Mars Space Images - Featured Image\\\\####

    # Mars image link 
    images_url = "https://www.jpl.nasa.gov/images/rabe-crater-dunes-27/"
    requests.get(url)
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path)
    browser.visit(images_url)
    time.sleep(2)

    #Creating BeautifulSoup object
    html_img = browser.html
    images_soup = bs(html_img, 'html.parser')

    print("Mars Featured Image Scrape...")

    # Scraping the images parent
    div_pic_parent = images_soup.find('div',class_='relative bg-black border border-black')

    #Scraping the image link
    
    image_link = div_pic_parent.find('img', id="96272")

    image_link_src = image_link.get('src')
   
    featured_image_url = f'{image_link_src}'
    requests.get(featured_image_url)

    print("Mars Featured Image Scrape Completed")
   
    ####////Mars Weather\\\\####

    # Mars weather link
    weather_url = "https://twitter.com/marswxreport?lang=en"

    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path)

    browser.visit(weather_url)
    #Need wait function to allow the page to open
    time.sleep(2)

    print("Mars Weather Tweet Scrape...")

    #Creating BeautifulSoup object
    html_weather = browser.html
    weather_soup = bs(html_weather, 'html.parser')

    #Scraping the image link
    tweet_text = weather_soup.find('div', attrs={"dir": "auto", "lang": "en"})

    print("Mars Weather Tweet Scrape Completed")

    ####///Mars Facts\\\\####

    mars_fact_url = "https://space-facts.com/mars/"
    requests.get(mars_fact_url)
    print("Mars Facts Scrape...")

    mars_space_fact = pd.read_html(mars_fact_url)
    mars_Df = mars_space_fact[0]
    Mars_df = mars_Df.rename(columns={0:"Mars Description",1:"Value"})
    mars_html_table = pd.DataFrame.to_html(Mars_df)
    mars_html_table= mars_html_table.replace('\n', '')
    
    print("Mars Facts Scrape Completed")
    
    #####////Mars Hemispheres\\\\####
  
    print("Mars Hemisphere Scrape...") 

    #### Cerberus
    cerberus_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(cerberus_url)
    time.sleep(2)

    print("Cerberus...") 

    #Creating BeautifulSoup object
    html_cerberus = browser.html
    cerberus_soup = bs(html_cerberus, 'html.parser')

    #Scraping the images parent
    cerberus_parent = cerberus_soup.find("div", id="wide-image")
    cerbus_img_link = cerberus_parent.a['href']

    #Scraping the cerbus title
    cerberus_title = cerberus_soup.find("h2", class_="title")
    
    print("Cerberus Completed") 

    #### Schiaparelli 
    schiaparelli_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(schiaparelli_url)
    time.sleep(2)

    print("Schiaparelli...")

    #Creating BeautifulSoup object
    html_schiaparelli = browser.html
    schiaparelli_soup = bs(html_schiaparelli, 'html.parser')

    # Scraping the images parent
    schiaparelli_parent = schiaparelli_soup.find("div", id="wide-image")
    schiaparelli_img_link = schiaparelli_parent.a['href']
    
    #Scraping the cerbus title
    schiaparelli_title = schiaparelli_soup.find("h2", class_="title")
    
    print("Schiaparelli Completed")
    
    #####Syrtis

    #syrtis link
    syrtis_major_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
  
    #Creating BeautifulSoup object
    html_syrtis = browser.html
    syrtis_soup = bs(html_syrtis, 'html.parser')
    browser.visit(syrtis_major_url)
    time.sleep(2)

    print("Syrtis...")

    # Scraping the images parent
    syrtis_parent = syrtis_soup.find("div", id="wide-image")
 
    syrtis_img_link = syrtis_parent.a['href']
   
    #Scraping the syrtis title
    syrtis_title = syrtis_soup.find("h2", class_="title")
    
    print("Syrtis Completed")

    #### Valles Marineris 
    valles_marineris_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"

    #Creating BeautifulSoup object
    html_valles_marineris = browser.html
    valles_marineris_soup = bs(html_valles_marineris, 'html.parser')
    browser.visit(valles_marineris_url)
    time.sleep(2)

    print("Valles...")
    # Scraping the images parent
    valles_marineris_parent = valles_marineris_soup.find("div", id="wide-image")

    valles_marineris_img_link = valles_marineris_parent.a['href']
    
    #Scraping the syrtis title
    valles_marineris_title = valles_marineris_soup.find("h2", class_="title")
    print("Valles Completed")

    # image dictionary 
    hemisphere_image_urls = [
        {"title":cerberus_title,"img_url":cerbus_img_link},
        {"title":schiaparelli_title,"img_url":schiaparelli_img_link},
        {"title":syrtis_title,"img_url":syrtis_img_link},
        {"title":valles_marineris_title,"img_url":valles_marineris_img_link}]

    nasa_scrape = {
         "news_titile": news_title[0],
         "news_para": news_p[0],
         "mars_img": featured_image_url,
         "weather": tweet_text,
         "mars_facts": mars_html_table,
         "hemp_dict": hemisphere_image_urls
         }

    print("NASA Scrape Completed")

    return nasa_scrape

scrapeMars()


