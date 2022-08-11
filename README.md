# Python-Learning

## Overview 
This project includes - Python basics | ADT | Python Unit test cases | ORM -Django/SQLAlchemy

##Description
This project include python codes of the following topics:
1. Average of numbers using loop
2. Sum of number using loop
3. Counting number using loop
4. Finding largest number
5. A definite loop with strings
6. Using continue and break
7. Calculating Cost per hour using try except
8. Using Try and catch
9. Convert elevator floor
10. Program using class
11. Using stack
12. Numpy
13. Built-in module
14. Importing functions
15. Creating and using modules

## ORM details - 
ORM LEARNING
ORM - Object Relational Mappers.
•	This is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code.
•	ORMs provide a bridge between relational database tables, relationships and fields and python objects.
#Why ORMs are useful?
•	It provides high level abstraction upon a relational database that allows a developer to write python code instead of SQL create, read, update and delete data and schemas in their database.
Eg: Without ORM a developer has to write the following SQL statement.
	SELECT * FROM USERS WHERE zip_code = 94107;

With Django ORM query would look like following python code.
	users = Users.objects.filter(zip_code = 94107)
# Downside of using ORM:
1.	Impedance mismatch
2.	Potential for Reduced performance
3.	Shifting complexity from the database into the application code.
# Python ORM implementation:
1.	SQLAlchemy 
2.	Django ORM
3.	Peewee
4.	PonyORM
5.	SQLObject 
6.	Tortoise ORM

# Django ORM:
	Django web framework comes with its own built-in object-relational mapping module, generally referred to as “The Django ORM”.
	Django ORM works well for simple and medium complexity database operations.

# SQLAlchemy ORM:
	It is well regarded Python ORM because it gets the abstraction level accurately and make complex database queries easier to write than Django ORM in most cases.

# Django ORM – Inserting, Updating & Deleting data
Django let us interact with its database models i.e. add, delete =, modify, and query objects, using a database – abstraction API called ORM.

Eg:
class Album(models. Model):
  title = models.CharField(max_length =30)
  artist = models.CharField(max_length =30)
  genere = models.CharField(max_length =30)
  def __str__(self):
	  return self.title

class Song(models. Model):
	name = models.CharField(max_length = 100)
	album = models.ForeignKey(Album, on-delete = models.CASCADE)
	def __str__(self):
		return self.name

###Adding Objects:
o	To create an object of model album and save it into the database, we need to write the following code:
    a = album(title = “Divide” , artist = “Ed Sheeran” , genre = “Pop”)
    a.save()
o	To create an object of model song and save it into the database, we need to write the following command:
    s = Song(name = “Castle on the hill” , album = a)
    s = a

###	Retrieving Objects:
    a = Album(title = "Abbey Road", artist = "The Beatles", genre = "Rock")
    a.save()    
    a = Album(title = "Revolver", artist = "The Beatles", genre = "Rock")
    a.save()

###	To retrieve all objects:
    Album.objects.all()
    <QuerySet [<Album: Divide>, <Album: Abbey Road>, <Album: Revolver>]>
###	Modifying existing objects
    a = Album.objects.get(pk = 3)
    a.genre = "Pop"
    a.save()

###	Deleting objects
    a = Album.objects.get(pk = 2)
    a.delete()
    Album.objects.all()
    <QuerySet [<Album: Divide>, <Album: Revolver>]>

###	To delete multiple objects, we can use filter() or exclude() functions as follows:
    Album.objects.filter(genre = "Pop").delete()
    Album.objects.all()
    <QuerySet []>

# MVC Design Pattern:
•	The Model View Controller (MVC) design pattern specifies that an application consist of a data model, presentation information, and control information.

•	MVC mostly relates to the UI / interaction layer of an application.
 


# Repository Pattern:
It is a simplifying abstraction over data storage, allowing us to decouple our model layer from the data layer.
 
Framework we use to generate SQL for us based on model object are called ORM(Object relational Mappers). They exist to bridge the conceptual gap between the world of objects and domain modeling and the world of databases and relational algebra

# Repository in Abstract:
The simplest repository has just two methods:
    •	add() to put a new item in the repository.
    •	get() to return a previously added item.

We use these methods for data access in our domain and our service layer.
This self-imposed simplicity stops us from coupling our domain to the database.
    
    class AbstractRepository(abc.ABC):
        @abc.abstractmethod  #(1)
        def add(self, batch: model.Batch):
            raise NotImplementedError  #(2)
        @abc.abstractmethod
        def get(self, reference) -> model.Batch:
            raise NotImplementedError

1.	Python tip: @abc.abstractmethod is one of the only things that makes ABCs actually "work" in Python. Python will refuse to let you instantiate a class that does not implement all the abstractmethods defined in its parent class.

2.	Raise NotImplementedError is nice, but it’s neither necessary nor sufficient. In fact, your abstract methods can have real behavior that subclasses can call out to, if you really want.
 
# How to run SQL in Jupyter:
1.	import pandas as pd
    import sqlite3
2.	!pip install ipython-sql (optional step if sqlite not installed)
3.	df = pd.DataFrame({ ‘name’ : [‘A’ , ‘B’ , ‘C’],
                        ‘age’ : [‘20’ , ‘25’ , ‘30’],
                        ‘city’ : [ ‘D’ , ‘E’ , ‘F’ ]})
	   df
     Output – (Table)
4.	cnn = sqlite3.connect(‘jupyter_sql_tutorial.db’)
5.	df.to_sql(‘people’, cnn)
6.	%load_ext sql
7.	%sql sqlite///jupyter_sql_tutorial.db
8.	%%sql
    SELECT * FROM people
Output – sqlite:///jupyter_sql_tutorial.db
	  Done
	(Table output)
9.	%%sql
SELECT sum(age) as ‘Age_Sum’
FROM people
Output – Age_Sum
	   75

# SQLAlchemy with SQLite in Jupyter:
1.	create table & insert data.
If table exist then –
2.	import sqlalchemy as db
3.	engine = db.create_engine(‘sqlite:///jupyter_sql_tutorial.db’)
4.	connection = engine.connect()
metadata = db.MetaData()
shows = db.Table(‘people’ , metadata, autoload = True, autoload_with = engine)
query = db.select([shows])
5.	result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print(result_set)

# Join in SQLAlchemy:
query = db.select([people, people_details])
query = query.select_from(people.join(people_details, people.columns.name == people_details.columns.Name))
results = connection.execute(query).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(5)
# Load existing table in jupyter using SQLite & SQLAlchemy
1.	import pandas as pd 
import sqlite3
import sqlalchemy as db
2.	cnn = sqlite3.connect('jupyter_sql_tutorial.db')
3.	%load_ext sql
4.	%sql sqlite:///jupyter_sql_tutorial.db
5.	%%sql
Select * from people

