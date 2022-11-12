# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.tools.float_utils import float_compare


class CancelMotifConfirmation(models.TransientModel):
    _name = 'cancel.motif.confirmation'
    _description = 'Cancel motif confirmation'

    cancel_motif_id = fields.Many2one('cancel.motif',string='Cancel motif')

    def process(self):
        record_model = self.env.context.get('model')
        record_ids = self.env.context.get('model_ids')
        origin_method = self.env.context.get('method')
        records = self.env[record_model].browse(record_ids)
        records.write({'cancel_motif_id':self.cancel_motif_id.id})
        return getattr(records,origin_method)()



