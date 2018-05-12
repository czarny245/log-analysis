# Log-Analysis

This is a log analysis project made for Udacity web developer course.
The purpose of this exercise is to prove my skills with SQL.
The program will connect to the database end extract the information needed to answer
Three questions.
Then it will print it to the terminal.


    What are the most popular three articles of all time?
    Who are the most popular article authors of all time?
    On which days did more than 1% of requests lead to errors?


### Prerequisites and installation

To run this program you will need to have a virtual machine and vagrant installed on your machine
as well as python3.

* [python3](https://www.python.org/)
* [vagrant](https://www.vagrantup.com/)

 Download the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) anywhere on your machine.
 Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip into the same directory.

LOG INTO THE VIRTUAL MACHINE MACHINE

Start the terminal (recommending using Bash for Windows users)
cd into the directory containing "fullstack-nanodegree-vm" files.

use commands:   vagrant up
	        vagrant ssh
                cd /vagrant
  	        psql -d news -f newsdata.sql
		
### Create the following views

The following views are required for the program to run correctly:

create view pop_art as 
select title, count (*) as page_views 
from articles join log 
on log.path = concat('/article/', articles.slug) 
group by title order by page_views desc;


create view name_title as 
select name, title from articles, authors 
where authors.id = articles.author;

create view status_OK as 
select time, status, sum(count) from requests
where status ='200 OK' group by time, status;

create view status_notfound as 
select time, status, sum(count) from requests
where status ='404 NOT FOUND' group by time, status;

create view percentage as 
select status_OK.time, (status_notfound.sum/status_OK.sum*100) as percentage 
from status_OK join status_notfound
on status_OK.time = status_notfound.time;

##Run the program

While still in the virtual machine, run the program with command:

python report_tool.py

The answers will be printed into the terminal.
TYPE or PASTE your text here... Click the RED SPELL CHECK button above
