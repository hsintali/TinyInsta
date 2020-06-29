# Tiny Instagram

### Install & Running

```sh
git clone
pipenv install
pipenv shell
python manage.py makemigrations TinyInstagram
python manage.py migrate
python manage.py runserver
# nohup python manage.py runserver& >> django.log  # daemon process and backup log
# exit  # quit pipenv virtualenv
