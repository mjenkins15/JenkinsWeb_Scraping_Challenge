s# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd 
from bs4 import BeautifulSoup as bs 
from splinter import Browser
import requests
#import os
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys


# %%
executable_path = {"executable_path":"chromedriver.exe"}
browser = Browser('chrome', **executable_path, headless=False)


# %%
#NASA Mars News

url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)


# %%
html = browser.html

#Create a Beautiful Soup Object
soup = bs(html, "html.parser")


# %%
#NASA Mars News                                                                                 
# Extract the latest News Title 
articles = soup.find("ul", class_="item_list").find("div", class_="content_title")
#articles

#print(soup.prettify())


# %%
article = articles.find("a").text
article


# %%
#Extract Paragraph Text
paragraph = soup.find("div", class_="article_teaser_body").text


# %%
articles = soup.find_all("li", class_="slide")
first_article = articles[0]
first_title = first_article.find("div", class_="content_title").find("a").text
first_para = first_article.find("div", class_="article_teaser_body").text
print(first_title)
print(first_para)


# %%
#for article in articles:


# %%
#JPL Mars Space Images - Featured Image

featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(image_url)
html = browser.html
#Create a Beautiful Soup Object
soup = bs(html, "html.parser")


# %%
jpl_image = soup.find_all("article", class_= "carousel_item")
jpl_image


# %%
new_jpl_image = jpl_image[0].find("a")
new_jpl_image


# %%
new_jpl_image["data-fancybox-href"]


# %%
#Mars Weather on Twitter

twitter_url = "https://twitter.com/marswxreport?lang=en"
browser.visit(twitter_url)
#html = browser.html
#soup = bs(html, "html.parser")


# %%
html = browser.html
soup = bs(html, "html.parser")


# %%
#weather_tweet = soup.find_all("article")
#weather_tweet


# %%
mars_weather= weather_tweet[0].find_all("span", class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
mars_weather[4].text


# %%
#Mars Facts
#scrape the table containing facts about Mars

mars_facts_url = "https://space-facts.com/mars/"
browser.visit (mars_facts_url)


# %%
html = browser.html
soup = bs(html, "html.parser")


# %%
mars_facts = soup.find("table", class_= "tablepress tablepress-id-p-mars")
mars_facts


# %%
table = pd.read_html(mars_facts_url)
table


# %%
df = table[0]
df. columns = [0,1]
df.head


# %%
html_table = df.to_html()
html_table


# %%
html_table.replace("\n", "")


# %%
#Mars Hemispheres
mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(mars_hemispheres_url)
#browser.quit()


# %%
html = browser.html
soup = bs(html, "html.parser")


# %%
# Use Beautiful Soup's find_all() method to navigate and retrieve image attributes
hemisphere_img_class = soup.find_all('div', class_='item')

# Preview the first result in the list
hemisphere_img_class[0]


# %%
#Saving image url string for full resolution hemisphere

#url_list = [
#    "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced",
#    "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced",
#    "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced",
#    "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
#]


# %%
#Base url
base_url = "https://astrogeology.usgs.gov"
hemisphere_image_urls = []


# %%



# %%
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


# %%
#mars_hemispheres_dict = {}


# %%
#images = browser.find_by_css('a.product-item h3')


# %%
#for i in range(len(images)):
#    browser.find_by_css('a.product-item h3')[i].click()


# %%
#for url in url_list:
   


# %%
browser.quit()


# %%


