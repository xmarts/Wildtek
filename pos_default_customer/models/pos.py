# -*- coding: utf-8 -*-

from odoo import fields, models,tools,api

class pos_config(models.Model):
    _inherit = 'pos.config' 

    pos_defaut_customer = fields.Many2one("res.partner",string="Default Customer", domain=[('customer','=',True)])
