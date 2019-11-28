# miet_union

# установка проекта на локальную машину

``` bash
git clone https://github.com/IMB-a/miet_union
```
``` bash
python -m venv .venv
```
``` cmd
cd .venv/Scripts + activate # (для windows)
```
``` bash
cd .venv/Scripts + source activate # (для linux)
```
``` bash
cd ../..
```
``` bash
pip install -r requirements.txt
```
``` bash
python manage.py makemigrations
```
``` bash
python manage.py migrate
```

# запуск проекта
``` bash
python manage.py runserver
```
