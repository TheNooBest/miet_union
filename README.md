# miet_union

# установка проекта на локальную машину
1) git clone https://github.com/IMB-a/miet_union
2) python -m venv .venv
3) cd .venv/Scripts + activate # (для windows)
3) cd .venv/Scripts + source activate # (для linux)
4) cd ../..
5) pip install -r requirements.txt
6) python manage.py makemigrations
7) python manage.py migrate

# запуск проекта
python manage.py runserver
