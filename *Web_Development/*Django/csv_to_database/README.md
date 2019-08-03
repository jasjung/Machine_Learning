# csv to database 

[DJANGO: IMPORTING A CSV FILE TO DATABASE MODELS](http://abhishekchhibber.com/django-importing-a-csv-file-to-database-models/)


```py 
#################################################################
# model.py
#################################################################
class Country(models.Model):
	country = models.CharField(max_length=100)
	continent = models.CharField(max_length=100)

#################################################################
# python manage.py shell
#################################################################
import csv
import os

path =  [path to your csv file]
os.chdir(path) # changes the directory

from dashboard.models import Country # imports the model

with open('countries_continents.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		p = Country(country=row['Country'], continent=row['Continent'])
		p.save()
       
exit()
```

## Method 2: [Django CSV Importer](https://django-csv-importer.readthedocs.io/en/latest/index.html)

## Method 3: [MySQL Shell](https://medium.com/@AviGoom/how-to-import-a-csv-file-into-a-mysql-database-ef8860878a68)

