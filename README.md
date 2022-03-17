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
   
 <img width="852" alt="sc" src="https://user-images.githubusercontent.com/84547558/158767116-61c14092-46c2-42bc-8f7b-b732f4d4805a.png">

   

3. app.py: Python Flask app that loads the Index.html as a template and runs the scrape_mars.py parsing script and loads the parsed info through
   MongoDB to be used by the template. The script is in the repository.

![app](https://user-images.githubusercontent.com/84547558/158767394-292c1574-12fb-43cf-a28e-10820917325c.png)


4. Index.html: HTML page that displays the information parsed through various Mars websites and creates a dashboard of information.
   Styled using Bootstrap. The script is in the repository.
   
![htm](https://user-images.githubusercontent.com/84547558/158767938-1b690459-08e7-49a9-8de3-e2c1ad111d9b.png)


Final dashboard with information.

![1](https://user-images.githubusercontent.com/84547558/158768455-8a4030f1-c8a1-4c29-9e7e-1419e6786a11.png)

![2](https://user-images.githubusercontent.com/84547558/158768502-9f72ac13-f845-4ce0-953f-430b28bf8a2b.png)



