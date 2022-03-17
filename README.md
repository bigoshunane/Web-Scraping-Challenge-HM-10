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

# Steps used

1. mission_to_mars.ipynb: Jupyter Notebook that performs the initial scraping of each site. The script is in repository.

2. scrape_mars.py: Python script that uses the parsing methods from the Jupyter Notebook that returns a dictionary object to be inserted into 
   MongoDB. The script is in the repository.

3. app.py: Python Flask app that loads the Index.html as a template and runs the scrape_mars.py parsing script and loads the parsed info through
   MongoDB to be used by the template. The script is in the repository.

4. Index.html: HTML page that displays the information parsed through various Mars websites and creates a dashboard of information.
   Styled using Bootstrap. The script is in the repository.

# Results




