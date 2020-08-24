# MoneyTracking-Back

API that uses json for MoneyTracking.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Postgresql >= 12.1
Python >= 3.6.5
Pyenv || virtualenv
```

### Installing

Clone repository
```
git clone git@github.com:cxasper/money-traking-api.git
```

```
cd {{ project_name }}
```
Create virtualenv
```
pyenv virtualenv 3.6.5 name_env
```
Activate virtualenv
```
pyenv local name_env
```
Install environment dependencies
```
pip install --upgrade pip
```
```
pip install -r requirements.txt --no-cache-dir
```
Add environment dependencies
```
pip freeze > requirements.txt
```
Create .env and populate variables (database variables)
```
DB_HOST=db_host
DB_PORT=5432
DB_NAME=db_name
DB_USER=db_user
DB_PASSWORD=db_password
```
Run migration
```
python manage.py migrate
```

Create init user for project.
```
python manage.py createsuperuser
```

Run fixtures.
```
sh fixtures/create_metadata.sh
```

Run project
```
python manage.py runserver
```

## Running the tests

```
python manage.py test
```
