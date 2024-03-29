WhereismyJojoTruck or Uber for JojoTank trucks.

## Setup development environment.
  The following libraries are required before running the project:

    `sudo apt-get install libpq-dev` - Solves (Error: pg_config executable not found.).

    `sudo apt install gdal-bin` - Solves (django.core.exceptions.ImproperlyConfigured: Could not find the GDAL library....).

## Init project.
    
The following command will install all project dependencies.

    `pip install -e .`

## Setup PostgreSQL(DB) + GIS for the project.

  `sudo apt update` - update local packages index.

  `sudo apt install postgresql postgresql-contrib` - install postgres package using -contrib

  `sudo systemctl start postgresql.service` - ensure the service has started.

  `sudo -u postgres createdb whereismyjojo_dev` - create project database.

  `sudo -u postgres create user thapelo with superuser password 'thapelo'` - create db user(role) for the project.

  `sudo apt install postgis` - Installs postgis extension.

  `django-admin createsuperuser thapelo` - create superuser for the admin page.


## Running the project using dev settings.
The following command is used to run the project, from the root project directory.

  `django-admin migrate --settings=project.settings_dev` - run migrations.

  `django-admin runserver --settings=project.settings_dev` - run dev server

  `http://127.0.0.1:8000/api` - project api url.


## Running tests.

    `pytest` or `pytest --ds=project.settings_test tests/`


## Renaming files.
    The following files needs to be renamed to suits your project. Check the boiler plate.
