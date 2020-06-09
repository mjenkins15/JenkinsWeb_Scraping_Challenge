import time
from splinter import browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from selenium import webdriver
import requests as req



def scrape():

    #Step 1- Scraping
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")

    # NASA Mars News: latest news title and paragraph text. 
    articles = soup.find("ul", class_="item_list").find("div", class_="content_title")
    paragraph = soup.find("div", class_="article_teaser_body").text

    #JPL Mars Featured Image
    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html = browser.html
    soup = bs(html, "html.parser")

    jpl_image = soup.find_all("article", class_= "carousel_item")
    new_jpl_image["data-fancybox-href"]

    #Mars Weather (Twitter)
    twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)
    html = browser.html
    soup = bs(html, "html.parser")

    mars_weather= weather_tweet[0].find_all("span", class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
    mars_weather[4].text

    #Mars Facts
    mars_facts_url = "https://space-facts.com/mars/"
    browser.visit (mars_facts_url)
    html = browser.html
    soup = bs(html, "html.parser")

    mars_facts = soup.find("table", class_= "tablepress tablepress-id-p-mars")

    #Mars table (converting to pandas dataframe and replacing with /n to get html code)
    html_table = df.to_html()
    html_table.replace("\n", "") 

    #Mars Hemispheres (high resolution images of Mars' hemispheres)
    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemispheres_url)
    html = browser.html
    soup = bs(html, "html.parser")

    hemisphere_img_class = soup.find_all('div', class_='item')
    #Saving image url string for full resolution hemisphere

#url_list = [
#    "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced",
#    "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced",
#    "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced",
#    "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
#]

#Base url
    base_url = "https://astrogeology.usgs.gov"
    hemisphere_image_urls = []
    for i in hemisphere_img_class:
        img_title = i.find('h3').text
        partial_img_url = i.find('a')['href']

        # Visit link that contains full-sized image
        browser.visit(base_url+partial_img_url)

        # Store html from page visited
        img_html = browser.html
        
        # Create BeautifulSoup object; parse with 'html.parser'
        img_soup = bs(img_html, 'html.parser')
        
        # Retrieve image url
        individual_img_partial_url = img_soup.find('img', class_='wide-image')['src']
        
        # Attach partial link to main url
        individual_img_url = base_url + individual_img_partial_url

        # Append information into a list of dictionaries 
        hemisphere_image_urls.append({"title" : img_title, "img_url" : individual_img_url})
        
    hemisphere_image_urls

    #creating a python dictionary of all scraped data
    mars_data = {
        "articles": title, 
        "paragraph": paragraph,
        "new_jpl_image": featured_image_url,
        "mars_weather": mars_weather,
        "mars_facts": mars_facts,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    return mars_data

