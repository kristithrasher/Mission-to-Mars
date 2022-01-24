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


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


slide_elem.find('div', class_='content_title')


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup

# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere. .find_by_css is method I can use
links = browser.find_by_css('a.product-item img')

# iterate through the 4 hemispheres and retrieve the url and titles
for i in range(4):
    # create a dictionary to hold info for hemispheres
    hemispheres = {}
    
    #use browser and find by css method to go to the correct tag and class and click on using .click() method
    browser.find_by_css('a.product-item img')[i].click()
    
    # find sample image and extract
    element = browser.links.find_by_text("Sample").first
    
    # once found hold it in list
    hemispheres['img_url'] = element['href']

    # Retrieve the title for hemisphere
    hemispheres['title'] = browser.find_by_css('h2.title').text

    # update hemisphere list by saving title
    hemisphere_image_urls.append(hemispheres)

    # Go back to original page after retrieving data for the hemisphere and start the next scrape
    browser.back()


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# 5. Quit the browser
browser.quit()





