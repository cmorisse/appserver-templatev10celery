# coding: utf-8
import sys
import os
import logging
from celery import Celery
from inouk.odoo_celery.api import CELERY_TASKS_MODULES

# Updated by RECIPE
CELERY_APPLICATION_MAIN_NAME = 'odoo_celery_demo'
ODOO_CONFIG_FILE = '/home/ubuntu/workspace/etc/openerp.cfg'
TASKS_FILE_NAME = 'celery_tasks'

_logger = logging.getLogger(__name__)

app = Celery(CELERY_APPLICATION_MAIN_NAME, 
             broker='pyamqp://guest@localhost//',
             #backend='amqp://',
             include=CELERY_TASKS_MODULES,
             )

app.conf.update(
    # Don't modify these as it will break Odoo Celery
    accept_content=['json', 'celery_odoo_json_serializer'],
    result_serializer='celery_odoo_json_serializer',
    task_serializer='celery_odoo_json_serializer',
    odoo_config_file=ODOO_CONFIG_FILE,
    
    # Optional configuration, see the application user guide.
    result_expires=3600,
    worker_redirect_stdouts=False,
)

# TODO: Implement an API to register packages that must be passed to autodiscover
# Manually insert below, packages where you want IROC to search tasks modules 
# named after TASKS_FILE_NAME
#app.autodiscover_tasks([
#    ...
#    ],
#    related_name=TASKS_FILE_NAME)