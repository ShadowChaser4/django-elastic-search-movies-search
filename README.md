# django-elastic-search-movies-search
App to search movies name, elastic search practice app .

 Build using elastic search, django, django rest framework and sqlite db.


### To run the app 

> Create a python virtual environment. <br/>
> After that install dependencies using requirements.txt
```bash 
pip install -r requirements.txt
```

> Then create indices in elasticsearch using : 
```bash 
python manage.py serach_index --create
```
> Then run your app using: 
```bash 
python manage.py runserver
```
