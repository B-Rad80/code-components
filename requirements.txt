# Django_Test_Server
---SETUP---
This build is for LINUX but should work for MAC/Windows

This project uses Python 3.6 due to api wrapper dependencies @ RYAN pls do!

Install Python from https://www.python.org/downloads/

Check to make sure Python 3.6 is your default by using command line and using 'python -V'

If you have Python 2.X already installed either change your PATH environment variable to point to 3.6 or use python3 commands

Check to see if pip was installed alongside Python 3.6 by using the command 'pip -V'

You'll want to make sure that it's also pointing to Python 3.6 at the end of the response

Install virtualenv using 'pip install virtualenv'

Once you've pulled down the project from github create a virtual env for the project by using the command 'virtualenv venv' inside the project root directory

Navigate to ./Django_Test_Server/venv/bin/activate and run the activate command, this will start the virtual environment

Navigate back to the project root directory and then run 'pip install -r requirements.txt', this will install all the proper dependencies for the project




<><><><><><><><><><><>CREATING A DATABASE FOR DJANGO<><><><><><><><><><><>
If you are not familiar on how to create the DB in Postgresql follow the below commands in psql on your command line

linux commands:

//
sudo su - postgres
psql
//

Postrgres commands: Ill try to make this a script later when I can be more specific with the commands I want

//
CREATE DATABASE django;
CREATE USER djangouser WITH PASSWORD 'DUHJANGO';

ALTER ROLE djangouser SET client_encoding TO 'utf8';
ALTER ROLE djangouser SET default_transaction_isolation TO 'read committed';
ALTER ROLE djangouser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE django TO djangouser;

\q
quit
//




<><><><><><><><><><><>CONNECT DJANGO TO DATABASE<><><><><><><><><><><>
Next you need to connect your DB eiteher Postgresql or mysql to Django by editing the settings.py file in the mysite app folder
In settings .py change this code to point to your local server 
Defualt is using pointing to postgresql change django.db.backends.postgresql_psycopg2 to django.db.backends.mysql-connector -not sure about this one, but does include support for mysql through that plugin
//
'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'django',
                'USER': 'djangouser',
                'PASSWORD': 'DUHJANGO',
                'HOST': 'localhost',
                'PORT': '',
    }
}
//

python manage.py createsuperuser <user>

python manage.py makemigrations
python manage.py migrate

Now check out your super cool /admin page

Now you're ready to start working, the main code is stored inside the mysite folder

