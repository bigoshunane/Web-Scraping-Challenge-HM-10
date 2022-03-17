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

# Steps and Results:

1. mission_to_mars.ipynb: Jupyter Notebook that performs the initial scraping of each site. The script is in repository.

![1](https://user-images.githubusercontent.com/84547558/158886604-19ce56b8-8a24-475f-9204-c44d1ef38345.png)



2. scrape_mars.py: Python script that uses the parsing methods from the Jupyter Notebook that returns a dictionary object to be inserted into 
   MongoDB. The script is in the repository.
   
![2](https://user-images.githubusercontent.com/84547558/158886639-c56eab3e-9cf0-4c4b-a0c2-e862cea97bc3.png)
   

3. app.py: Python Flask app that loads the Index.html as a template and runs the scrape_mars.py parsing script and loads the parsed info through
   MongoDB to be used by the template. The script is in the repository.

![3](https://user-images.githubusercontent.com/84547558/158886677-fe02b8a7-2ba1-448a-ba61-b37ff9ff34b5.png)![31](https://user-images.githubusercontent.com/84547558/158886707-beb27cca-36d3-4533-986b-6dfa4c6d9577.png)


4. Index.html: HTML page that displays the information parsed through various Mars websites and creates a dashboard with Mars Facts information.
   Styled using Bootstrap. The script is in the repository.
   
![4](https://user-images.githubusercontent.com/84547558/158886751-8be2cc4e-805b-4231-91dd-ea04089425fd.png)![41](https://user-images.githubusercontent.com/84547558/158886787-5a1c88d6-eff5-4f58-84d1-1c1b44ba5481.png)


Final dashboard with Mars Facts information.


![dd](https://user-images.githubusercontent.com/84547558/158882647-8e4c2ddb-bc6e-4d44-9c03-6985b8a15c0a.png)



Rubric
Unit 12 Rubric - Web Scraping Homework - Mission to Mars

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
