# Mission-to-Mars
## Background
Robin, who hopes to be noticed by NASA created a web app that functions well, but she wants to add more polish to it. She had been admiring images of Mars’s hemispheres online and realized that the site is scraping-friendly. She would like to adjust the current web app to include all four of the hemisphere images. To do this, you’ll I used BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and the titles of those images, stored the scraped data on a Mongo database, used a web application to display the data, and altered the design of the web app to accommodate the  four hemisphere images.

## Analysis
    1. Scrape Full-Resolution Mars Hemisphere Images and Titles
    ![hemisphereImagesTitles](https://user-images.githubusercontent.com/94208810/151027162-4513020f-35da-4e85-9c1e-47799c411f96.png)
        
        
    2. Update the Web App with Mars Hemisphere Images and Titles
    ![4hemisphereImgs](https://user-images.githubusercontent.com/94208810/151027156-907b9464-0aca-4941-98fb-eb7a7cfab7a7.png) 
       
        
       

    3. Add Bootstrap components
        - Added the following <meta> tag inside the <head> element and added 

            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" inside my index.html to make website mobile responsive and to use bootstrap components. 

        -   Used bootstrap component jupotron to create a header for webpage. 
            Example:  <div class = 'jumbotron text-center">

      -     Used bootstrap component to style the "Scrape New Data" button. 
            Example:  <a class="btn btn-primary btn-lg" href="/scrape" role="button">Scrape New Data</a><p>
        
      -     Added the hemisphere images as thumbnails. 
            <div class="thumbnail">




