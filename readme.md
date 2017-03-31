# appserver-templatev10 - Odoo Celery Demo version

This repository is configured to build an Odoo 10 appserver ready to use with Odoo Celery.
It uses buildout and the anybox.recipe.odoo.

Please refer to https://bitbucket.org/cmorisse/inouk.odoo_celery for more detailed 
instructions about inouk.odoo_celery usage.

# Licence

Files in this repository are LGPL Licensed.

# Very brief description

Folder `./celery_app_project` contains the **celery_app** code shared between Odoo and Celery.

File `./project_addons/odoocelery_test/models/odoocelery_demo.py` defines a Model with a method
that can `a_task()`.

That task can be run either straight (debug mode) or asynchonously by Celery.

# Installation instructions

This repository is ready to use on Ubuntu 16.04 or in a Cloud9 Ubuntu 14.04 "blank" Workspace.

* Create a Clou9 workspace from this repository or clone and cd into it
* Open a Terminal window then enter:
  *  ./install.sh c9-trusty       # or ./install.sh on Ubuntu Xenial
  *  ./install.sh dependencies    # Installs rabbitmq
  *  ./install.sh openerp
* Now you can launch Odoo using `bin/start_openerp`

# Play with Odoo and Celery

## Ensure a broker is running

To experiments with tasks, a broker must be running. 

For rabbitmq enter `sudo service rabbitmq-server start` at your terminal prompt.

## Launch Tasks

The first time you launch Odoo, you must create a database named **odoocelery_db**. 
The database name is defined in the buildout configuration.
For that launch: `bin/start_openerp -i odoocelery_demo`
Note the -i param that installs the odoocelery_demo addon and setup the database with 
admin/admin as user password.
Once the database exists and has been setup, you can launch Odoo, with `bin/start_openerp``

The odoocelery_demo addon contains one model: "OdooCeleryLauncher" and one Task: "a_task".

Launch some tasks using the "Odoo Celery launcher" menu item:

* "Create" an object 
* enter some values 
* click on the "Run Task" button. 

If "debug mode" is not set, the tasks are enqueued and you must launch a Celery worker to execute 
them. For that, open a second terminal, then launch the worker using `bin/odoo_celery``

# Monitor the Queue

You can use Flower to monitor the Queue.

## Install flower

Open a third terminal, then enter (in repository root folder):

* virtualenv py27_flower
* source py27_flower/bin/activate
* pip install flower
* pip install git+https://bitbucket.org/cmorisse/inouk.odoo_celery.git

## Launch flower

Enter:

* cd celery_app_project
* flower --port=8081 -A celery_app 

On Cloud9, connect to flower using you workspace URL modified with the 8081 port.










