
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

###############################--> NASA Mars News 
def scrape():
    # Dependencies
    import os
    from bs4 import BeautifulSoup as bs
    import requests
    from splinter import Browser
    import pandas as pd
    import time
    browser = init_browser()
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




# Dependencies
import os
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import time

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)
    
def scrape():
    browser = init_browser()
    scraped_data={}

    # ******************************************************************************************************************************
    # Scraping Mars News
    # *****************************************************************************************************************************
    url = 'https://mars.nasa.gov/news/'
    print("Scraping Mars News...")
    
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = bs(html, 'html.parser')

    division_2 = soup.find('div', class_='list_text') 

    content_title = division_2.find('div', class_='content_title')

    news_title = content_title.text.strip()
    news_p = division_2.find('div', class_='article_teaser_body').text.strip()

    print("Mars News: Scraping Complete!")

   
    # *****************************************************************************************************************************
    # Scraping JPL Featured Image URL 
    # *****************************************************************************************************************************
    url_2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_2)
    time.sleep(1)

    print("Scraping JPL Featured Space Image...")

    html2 = browser.html
    soup = bs(html2, 'html.parser')

    picture_div = soup.find('div', class_='carousel_items')
    footer=picture_div.find('footer')
    data_url='https://www.jpl.nasa.gov' + footer.find('a')['data-link']
    
    url_3 = data_url
    browser.visit(url_3)
    time.sleep(1)

    html3 = browser.html
    soup = bs(html3, 'html.parser')
    figure = soup.find('figure', class_='lede')
    large_picture_url=figure.find('a')['href']

    featured_image_url='https://www.jpl.nasa.gov' + large_picture_url

    print("JPL Featured Space Image: Scraping Complete!")


    # *****************************************************************************************************************************
    # Scraping Mars Weather Tweet
    # *****************************************************************************************************************************
    
    url_4 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_4)
    time.sleep(1)

    print("Scraping Mars Weather's Twitter Account...")

    html4 = browser.html
    soup = bs(html4, 'html.parser')

    mars_weather = soup.find_all('span', class_ = 'css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')[27].text.replace('\n',' ')
 
    print("Mars Weather: Scraping Complete!")


    # *****************************************************************************************************************************
    #  Scraping Mars Facts
    # *****************************************************************************************************************************
    url_5 = 'https://space-facts.com/mars/'
    browser.visit(url_5)
    time.sleep(1)

    print("Scraping Mars Facts...")
    
    html5 = browser.html
    tables = pd.read_html(html5)

    mars_facts=tables[0]
    mars_facts.columns=['Mars Description', 'Value']
    mars_earth=tables[1]

    mars_facts=mars_facts.to_html(index=False, header=False, border=0, classes="table table-sm table-striped font-weight-light")

    mars_earth=mars_earth.to_html()

    print("Mars Facts: Scraping Complete!")


    # *****************************************************************************************************************************
    #  Scraping Mars Hemisphere images
    # *****************************************************************************************************************************
    url_6 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_6)
    time.sleep(1)

    html6 = browser.html
    soup = bs(html6, 'html.parser')
    hemisphere_results = soup.find_all('div', class_='item')

    hemisphere_image_data =[]

    for hemisphere in range(len(hemisphere_results)):

        # --- use splinter's browser to click on each hemisphere's link in order to retrieve image data ---
        link = browser.find_by_tag("h3")
        link[hemisphere].click()
        time.sleep(1)
        
        # --- create a beautiful soup object with the image detail page's html ---
        img_html = browser.html
        imagesoup = bs(img_html, 'html.parser')
        
        # --- retrieve the full-res image url and save into a variable ---
        img_li = imagesoup.find('li')
        img_url = img_li.find('a')['href']


        img_title = browser.find_by_tag("h2").text
        img_title

        # --- add the key value pairs to python dictionary and append to the list ---
        hemisphere_image_data.append({"title": img_title,
                                "img_url": img_url})
            # --- go back to the main page ---
        browser.back()
    
    # --- close the browser session ---    
    browser.quit()

    print("Mars Hemisphere Images: Scraping Complete!")



    # *****************************************************************************************************************************
    #  Store all values in dictionary
    # *****************************************************************************************************************************

    scraped_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featuredimage_url": featured_image_url,
        "mars_weather": mars_weather,
        "mars_fact_table": mars_facts, 
        "mars_earth_comparison":mars_earth,
        "hemisphere_images": hemisphere_image_data
    }

    # --- Return results --
    