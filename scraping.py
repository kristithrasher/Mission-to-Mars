#!/usr/bin/env python
# coding: utf-8
# Import Splinter and BeautifulSoup and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
# searching for elements with a specific combination of tag (div) 
# and attribute (list_text). 
# telling our browser to wait one second before searching for components. 
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object 
html = browser.html
news_soup = soup(html, 'html.parser')

# assign the title and summary text to variables we'll reference later
slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p
# ### Featured Images

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse so we can continue and scrape the full-size image URL
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url we tell BeautifulSoup to look inside the img tag for an image with a class of 
# fancy box image. "This is where the image we want lives- use the links inside these tags"
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# Using Pandas' .read_html() function instead of having to scrape each row of data
# creating a new DataFrame from the HTML table. The Pandas function read_html() 
# By specifying an index of 0, we're telling Pandas to pull only the first table it 
# encounters, or the first item in the list. Then, it turns the table into a DataFrame.
df = pd.read_html('https://galaxyfacts-mars.com')[0]

# we assign columns to the new DataFrame for additional clarity.
df.columns=['description', 'Mars', 'Earth']

# By using the .set_index() function, we're turning the Description column into the DataFrame's
# index. inplace=True means that the updated index will remain in place, without having 
# to reassign the DataFrame to a new variable.
df.set_index('description', inplace=True)
df
# Mars Facts
 
# Pandas also has a way to easily convert our DataFrame back into HTML-ready code using the .to_html() function
df.to_html()

# To end the session
browser.quit()


