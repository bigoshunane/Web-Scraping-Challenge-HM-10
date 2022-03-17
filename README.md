# Web-Scraping-Challenge-HM-10

# Mission to Mars

The main objective of this project is to develop web application that scrapes different websites to grap the latest information, news headlines and images of planet Mars and display the information gathered in a single responsive HTML web page. 

# Technologies used:

. Beautiful soup and splinter for scraping the target data from given websites.

. HTML and Bootstrap (CSS) for designing and styling the web page.

. Flask for building the web application.

. PyMongo for interacting with the Mongo Database and store gathered data for CRUD application of the database.

. Pandas for designing the Mars Facts table.

# Resources used:

. [https://redplanetscience.com/]()

. [https://spaceimages-mars.com/]()

. [https://galaxyfacts-mars.com/]()

. [https://marshemispheres.com/]()

# Steps

1. mission_to_mars.ipynb: Jupyter Notebook that performs the initial scraping of each site. The script is in repository.

2. scrape_mars.py: Python script that uses the parsing methods from the Jupyter Notebook that returns a dictionary object to be inserted into 
   MongoDB. The script is in the repository.  

3. app.py: Python Flask app that loads the Index.html as a template and runs the scrape_mars.py parsing script and loads the parsed info through
   MongoDB to be used by the template. The script is in the repository.

4. Index.html: HTML page that displays the information parsed through various Mars websites and creates a dashboard with Mars Facts information.
   Styled using Bootstrap. The script is in the repository.
   
# Results

1. Scraping

Nasa Mars News:

![1](https://user-images.githubusercontent.com/84547558/158887493-c92bb4f5-ec6b-45f1-89f2-0278758802ac.png)

JPL Mars Space Images-Featured Image:

![2](https://user-images.githubusercontent.com/84547558/158887648-a324cb42-2805-431f-804a-dd7875307099.png)

Mars Facts:

![3](https://user-images.githubusercontent.com/84547558/158887705-c338bf40-677b-4d23-99d6-e2bda1bf01ee.png)![31](https://user-images.githubusercontent.com/84547558/158887732-edb7b23f-8e39-4206-8d81-56909a2ac2f6.png)

Mars Hemispheres:

![4](https://user-images.githubusercontent.com/84547558/158887802-3e5144a9-a07c-4b16-885f-f4b321e7f6c2.png)![41](https://user-images.githubusercontent.com/84547558/158887818-307aea47-40b7-4eaf-9c35-8151ffc68072.png)

2. MongoDB and Flask Application

Final dashboard with Mars Facts information:


![dd](https://user-images.githubusercontent.com/84547558/158882647-8e4c2ddb-bc6e-4d44-9c03-6985b8a15c0a.png)



Rubric
Unit 12 Rubric - Web Scraping Homework - Mission to Mars

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
