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

![dd](https://user-images.githubusercontent.com/84547558/158766829-8395d10a-ae1e-4cd2-9eb3-63ae6db5af70.png)


2. scrape_mars.py: Python script that uses the parsing methods from the Jupyter Notebook that returns a dictionary object to be inserted into 
   MongoDB. The script is in the repository.
   
![ff](https://user-images.githubusercontent.com/84547558/158883000-456fd56d-37b3-4e22-8f5f-5e6dac95206b.png)

   

3. app.py: Python Flask app that loads the Index.html as a template and runs the scrape_mars.py parsing script and loads the parsed info through
   MongoDB to be used by the template. The script is in the repository.

![app](https://user-images.githubusercontent.com/84547558/158883058-08222389-9a10-4aa2-9004-a53a598a9478.png)


4. Index.html: HTML page that displays the information parsed through various Mars websites and creates a dashboard with Mars Facts information.
   Styled using Bootstrap. The script is in the repository.
   
![index](https://user-images.githubusercontent.com/84547558/158883279-589d0a02-fee4-41bf-b241-f80e32175ea0.png)

Final dashboard with Mars Facts information.


![dd](https://user-images.githubusercontent.com/84547558/158882647-8e4c2ddb-bc6e-4d44-9c03-6985b8a15c0a.png)



Rubric
Unit 12 Rubric - Web Scraping Homework - Mission to Mars

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
