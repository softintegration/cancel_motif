# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.tools.float_utils import float_compare


class CancelMotifConfirmation(models.TransientModel):
    _name = 'cancel.motif.confirmation'
    _description = 'Cancel motif confirmation'

    cancel_motif_id = fields.Many2one('cancel.motif',string='Cancel motif')
    cancel_date = fields.Date(string='Cancel date',default=lambda self: fields.Datetime.now())
    display_cancel_date = fields.Boolean(default=False)
    display_cancel_motif_id = fields.Boolean(default=True)
    required_cancel_motif_id = fields.Boolean(default=True)
    model = fields.Char(string='Model name')

    def process(self):
        record_model = self.env.context.get('model')
        record_ids = self.env.context.get('model_ids')
        origin_method = self.env.context.get('method')
        cancel_date = self.env.context.get('cancel_date','cancel_date')
        records = self.env[record_model].browse(record_ids)
        records.write({'cancel_motif_id':self.cancel_motif_id.id,cancel_date:self.cancel_date})
        return getattr(records,origin_method)()



