# MOVIE TRAILER WEBSITE

Movie Trailer Website is a website where user can watch the trailer of their favorite movies.

Aim of this project is to learn how to write an application using object-oriented Python programming as well as how to serve HTML using a web server and how web servers receive requests, execute a block of code, and generate a response.

## SETUP

Python needs to be installed for this to work. It can be downloaded in the below mentioned website - 
https://www.python.org/downloads/

Python right now comes in two stable versions namely, Python v3.6.4 and Python v2.7.14.

## PROJECT REQUIREMENTS/FEATURES: 

* Writing server side code to store a list of movie titles, box art, poster images, and movie trailer URLs.
* The data will be expressed on the web page and allow users to review the movies and watch the trailers.
* Project works the way it's supposed to: movies and their poster images are displayed on the web page, there is a trailer link and it opens from the Python file error free.
* Code is organised and professional.
* Comments are used when needed.


### RUNNING

To generate the HTML file for the website, type the following command.
```python
    $ python database.py
```
This will generate an html file named ```fresh_tomatoes.html``` in the same folder or it will overwrite the existing one if it already exits. Also, it will open a new tab on the default browser and load the generated page.

Or instead, if you have Python and IDLE installed you can just double click on the 'database.py' file and it will open the Movie Trailer Website. 
Also, you can right click on the 'database.py' file and select 'Edit with IDLE' and then press F5.

### MODULES
There are three modules in the projects
  - ```database.py```: This module acts as a database for the project as ut contains all the information about various instances of the class 'Movie'. This file has all the information about every single movie that is displayed. This python file then calls the fresh_tomatoes.py file at the end to open the page in a web browser.
  - ```fresh_tomatoes.py```: This is related to the views that this model creates. fresh_tomatoes.py then generates an HTML file which runs and shows the Movie trailers.
  - ```main.py```: This is the data model file which defines the movie and it's various attributes(Title, Year, etc).
