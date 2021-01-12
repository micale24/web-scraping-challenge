
 # Dependencies
import os
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd
import time

###############################--> NASA Mars News 
def scrape():
   
    nasa_scrape = {}

    # NASA Mars News Site URL
    nasa_url= "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    #Creating the path and enabling the pages's js and creating the soup object
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path)
    browser.visit(nasa_url)
    #Need wait function to allow the page to open
    time.sleep(20)

    #Creating BeautifulSoup object
    html = browser.html
    news_soup = bs(html, 'html.parser')

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

    #############################--> JPL Mars Space Images 

    # Mars image link
    images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(images_url)
    time.sleep(20)

    #Creating BeautifulSoup object
    html_img = browser.html
    images_soup = bs(html_img, 'html.parser')

    # Scraping the images parent
    div_ul_parent = images_soup.select_one("ul.articles")

    #Scraping the image link
    image_link = div_ul_parent.a['data-fancybox-href']

    featured_image_url = f'https://www.jpl.nasa.gov{image_link}'

    #############################--> Mars Weather

    # Mars weather link
    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)
    time.sleep(20)

    #Creating BeautifulSoup object
    html_weather = browser.html
    weather_soup = bs(html_weather, 'html.parser')

    #Scraping the image link
    tweet_text = weather_soup.find('div', attrs={"dir": "auto", "lang": "en"})

    #############################--> Mars Facts

    mars_facts_url = "https://space-facts.com/mars/"
    mars_tables = pd.read_html(mars_facts_url)
    mars_df = mars_tables[0]
    mars_html_table = pd.DataFrame.to_html(mars_df)
    mars_html_table= mars_html_table.replace('\n', '')

    #############################--> Mars Hemispheres

    ############# Cerberus

    cerberus_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(cerberus_url)
    time.sleep(20)

    #Creating BeautifulSoup object
    html = browser.html
    cerberus_soup = bs(html, 'html.parser')

    # Scraping the images parent
    cerberus_parent = cerberus_soup.find("div", id="wide-image")
    cerbus_img_link = cerberus_parent.a['href']

    #Scraping the cerbus title
    cerberus_title = cerberus_soup.find("h2", class_="title")

    ############ Schiaparelli 

    schiaparelli_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(schiaparelli_url)
    time.sleep(20)

    #Creating BeautifulSoup object
    html = browser.html
    schiaparelli_soup = bs(html, 'html.parser')

    # Scraping the images parent
    schiaparelli_parent = schiaparelli_soup.find("div", id="wide-image")
    schiaprarelli_img_link = schiaparelli_parent.a['href']

    #Scraping the cerbus title
    schiaprarelli_title = schiaparelli_soup.find("h2", class_="title")

    ############ Syrtis

    syrtis_major_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(syrtis_major_url)
    time.sleep(20)

    #Creating BeautifulSoup object
    html = browser.html
    syrtis_soup = bs(html, 'html.parser')

    # Scraping the images parent
    syrtis_parent = syrtis_soup.find("div", id="wide-image")
    syrtis_img_link = syrtis_parent.a['href']

    #Scraping the syrtis title
    syrtis_title = syrtis_soup.find("h2", class_="title")

    ############# Valles Marineris 

    valles_marineris_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(valles_marineris_url)
    time.sleep(20)

    #Creating BeautifulSoup object
    html = browser.html
    valles_marineris_soup = bs(html, 'html.parser')

    # Scraping the images parent
    valles_marineris_parent = valles_marineris_soup.find("div", id="wide-image")

    valles_marineris_img_link = valles_marineris_parent.a['href']

    #Scraping the syrtis title
    valles_marineris_title = valles_marineris_soup.find("h2", class_="title")

    # image dictionary 
    hemisphere_image_urls = [
        {"title":cerberus_title,"img_url":cerbus_img_link},
        {"title":schiaprarelli_title,"img_url":schiaprarelli_img_link},
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

    return nasa_scrape

    