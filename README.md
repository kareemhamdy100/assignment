# assignment
note you must have : pip , virtualenv installed in your system
```
virtualenv env 
. env/bin/active 
pip install -r requirments.txt
python src/task/manage.py migrate
python src/task/manage.py collectstatic 
python src/task/manage.py runserver
```


# this is simple Restfull api for makeing CURD operation using django 
 ```
 1-you could chose which fields that appear on each object  by pass  fields list with url 
 2- you can filter data  
```
