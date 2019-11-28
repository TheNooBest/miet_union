# miet_union

# Installation env

``` bash
git clone https://github.com/IMB-a/miet_union
python -m venv .venv
cd .venv/Scripts + activate # (for windows)
cd .venv/Scripts + source activate # (for linux)
cd ../..
```
# Installation app
``` bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

# Usage
``` bash
python manage.py runserver
```
