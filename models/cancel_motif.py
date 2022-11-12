# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class CancelMotif(models.Model):
    _name = 'cancel.motif'
    _description = 'Cancel motif'

    name = fields.Char(string='Name',required=True)
    description = fields.Text(string='Description')
    model = fields.Char(string='Model name')

