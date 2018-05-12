#! /usr/bin/env python
import psycopg2


# Fetch information needed for question 1 from database and print them out
def get_articles():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select * from pop_art limit 3;")
    articles = c.fetchall()
    db.close()
    print("Most popular articles:")
    for data in articles:
            print('"'+data[0]+'"'+'--'+str(data[1])+'-veiws')
    print ('\n')


# Fetch information needed for question 2 from database and print them out
def get_authors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select name, "
              "sum(page_views) as views from name_title, "
              "pop_art where name_title.title = pop_art.title "
              "group by name order by views desc;")
    authors = c.fetchall()
    db.close()
    print("Most popular authors")
    for data in authors:
        print('"'+data[0]+'"'+'--'+str(data[1])+'-views')
    print ('\n')


# Fetch information needed for question 3 from database and print them out
def get_days():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select time, cast(percentage as numeric(10,2)) "
              "from percentage where percentage >1;")
    percentage = c.fetchall()
    db.close()
    print("Days with errors")
    for data in percentage:
            print('"'+str(data[0])+'"'+'--'+str(data[1])+'%')
    print ('\n')

# Call the functions above
get_articles()
get_authors()
get_days()

