#!/usr/bin/env python
# coding: utf-8
# Import Splinter and BeautifulSoup and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt


def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)
    img_url_title = mars_hemispheres(browser)
    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres" : img_url_title,
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):

    # Scrape Mars News
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
    # Add try/except for error handling
    try:
        # assign the title and summary text to variables we'll reference later
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find(
            'div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p

# ### Featured Images


def featured_image(browser):
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

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url

# Mars Facts


def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html(
            'https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns = ['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")


# Scrape Hemisphere Data

def mars_hemispheres(browser):

    # Use browser to visit the URL
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # Write code to retrieve the image urls and titles for each hemisphere. .find_by_css is method I can use
    links = browser.find_by_css('a.product-item img')

    # iterate through the 4 hemispheres and retrieve the url and titles
    for i in range(4):
        # create a dictionary to hold info for hemispheres
        hemispheres = {}

        # use browser and find by css method to go to the correct tag and class and click on using .click() method
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
    return hemisphere_image_urls
if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())
