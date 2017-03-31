# -*- coding: utf-8 -*-
import sys
import datetime
import logging

import odoo
from odoo.exceptions import UserError
from odoo.tools.safe_eval import safe_eval
from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.modules import get_module_resource

# inouk.celery_odoo required import
from celery_app import app
from inouk.odoo_celery.bridge import OdooTask
from inouk.odoo_celery.api import celery_task

_logger = logging.getLogger(__name__)


class OdooCeleryLauncher(models.Model):
    _name = 'odoocelery_launcher'

    name = fields.Char()
    debug_mode = fields.Boolean()
    param = fields.Char()
    result = fields.Text()
    
    @api.multi
    def launch(self):
        """ Launch a task straight or asynchonously depending on debug_model """
        self.ensure_one()
        if self.debug_mode:
            a_task(self)
        else:
            a_task.delay(self)


@app.task(base=OdooTask)
@celery_task
def a_task(an_object):
    """ This a our task. It simplied inject param in value adding it current time """
    an_object.result = "%s @ %s" % (an_object.param, datetime.datetime.now(),) 
    # We use print to get a trace in celery
    print "Processed: %s" % an_object
    #_logger.info("Processed %s", an_object)
    
