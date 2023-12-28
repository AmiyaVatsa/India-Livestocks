# LIVESTOCKS INDIA
#### Video Demo:  https://youtu.be/jB7to18ktak
#### Description:

# Livestock-India

Hello everyone, my name is Amiya Vatsa. I'm an engineering student from the state of chattisgarh, India.

This project is a website where people can access the data about livestocks across every district in every state in India.

## Features

- [SQLite](https://www.sqlite.org/index.html)
- [Flask](https://palletsprojects.com/p/flask/)
- [Bootstrap](https://getbootstrap.com/)

## Credits
- [Unsplash](https://unsplash.com/)
- [Open Data India](https://data.gov.in/)

I used SQLite database for the backend of the website. The file "livestocks.db" is the sqlite3 database file. The schema for the file is

>CREATE TABLE livestocks (
>    ref_state_id INTEGER,
>    state_name TEXT,
>    ref_district_id INTEGER,
>    district_name TEXT,
>    cattle INTEGER,
>    buffalo INTEGER,
>    sheep INTEGER,
>    goat INTEGER,
>    horse INTEGER,
>    pony INTEGER,
>    mule INTEGER,
>    donkey INTEGER,
>    camel INTEGER,
>    pig INTEGER,
>   Total_poultry INTEGER
>);

## Layout

The CSV files taken from OGD website are stored in data_gov directory. The static directory contains a styles.css file containing the css code for the website and photos used in the project, which have been downloaded from Unsplash.com.

the templates directory contains the html files used in the project. These include:-
#### 1) layout.html
It is the basic layout page of the website. All other html files are extensions of it.

#### 2) about_us.html
This page contains the credits for the data and ways to reach the creator of this website.

#### 3) index.html
This page is the homepage of the website. It's a static webpage, with a quoatation from the Yajurveda.

#### 4) district.html and state.html
This files are the jinja templates for the data that is to be rendered, for districts and states respectively.

## app.py
This is the driver file of the entire project. It imports the libraries, flask, etc.
#### Routing
Routes have been created in the app.py file according to the layout of the directories and the need of the webpage.


The structure of the directory project is as follows

>- project
>
>   -data_gov
>
>       -contains raw csv files downloaded from OGD website.
>
>    -static
>
>        -contains images downloaded from unsplash.com
>
>        -styles.css
>
>    -templates
>
>        -about_us.html
>
>        -district.html
>
>        -index.html
>
>        -layout.html
>
>        -state.html
>
>    -app.py
>
>    -livestocks.csv
>
>    -livestocks.db
>
>    -readme.md(You're here)


# How to reach me?

-LinkedIn: @amiya-vatsa-031213218

-Instagram: @amiyavatsa

-email: amiyavatsa1807@gmail.com

Thank You!
