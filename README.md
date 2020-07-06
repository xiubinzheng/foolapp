# foolapp
## Motley Fool Developer Interview Project

Hello!

Below you will find guidelines for a small website you will create. Included are two JSON files, content_api.json and quotes_api.json, which you should use to populate the website. Also included are two wireframe designs for a homepage and an article page as well as some basic HTML templates if you wish to use them, however please feel free to use your own creativity for the design of this website.

We would like to thank you for taking the time to complete this project. We will schedule your in-person interview after we have received your completed project. We are looking forward to discussing ,your experience and the completed project!

### General project guidelines
* Host your project on github.
* Create a Django app.
* Use any publicly available python packages that you need.
* Use any front-end scaffolding framework and any JS libraries excluding JS frameworks (angular, react, etc) 
* Include a startup shell script that will install any dependencies and start the application.

### Homepage
* The top box on the homepage should be populated with the first article in the content API with the tag where slug=10-promise.
* The remaining three boxes should be populated with a random assortment of the remaining articles. 
* The headline's of each article should link to the article page.

### Article Page
* Use content_api.json and quotes_api.json to populate the details for the individual article page.
* Use a URL schema that makes sense to you.
* Create a button below the Stock Quotes sidebar that, when clicked, will use javascript to shuffle the order of the stock quote 
items.
* Ability to add comments at the bottom of an article by anonymous users.

### Evaluation criteria
List of possible evaluation criteria.
* Front-end structure - Use of partials, CSS and JS structure.
* Django Framework usage.
* URL Structure.
* Any database use.
* Possible areas for future additions, improvement, or optimization.
* Anything you did to make make the application your own.


### Running the application
* run the startup.sh, this will run below commands: 
* pip3 install -r requirements.txt 
* python3 manage.py migrate
* python3 manage.py runserver
* depeneding on your enviroment, your pip command might be pip or pip3, if it is different just change to pip3 or vise versa.
* samethig with python, depending on your config, it might be python3 or python on the comamnd line make sure to run it using python version 3.  
* PLEASE also note that with startup.sh, for some reason If you would run into permission issue, so if you ever run into a permission issue
* please run chmod 777 startup.sh then it should solve the problem





