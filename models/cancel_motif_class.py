# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class CancelMotifClass(models.AbstractModel):
    """ Cancel motif class is the base class of the cancel motif management,this will add the cancel_motif_id field
    to model so that al the cancel motif management be centralized"""
    _name = 'cancel.motif.class'
    _description = 'Cancel motif class'

    cancel_motif_id = fields.Many2one('cancel.motif',string='Cancel motif')
    cancel_date = fields.Date(string='Cancel date')

    def _action_cancel_motif_wizard(self):
        view = self.env.ref('cancel_motif.view_cancel_motif_confirmation')
        new_wizard = self.env['cancel.motif.confirmation'].create({
            'model':self.env.context.get('model',False)
        })
        return {
            'name': _('Cancellation motif'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'cancel.motif.confirmation',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'res_id':new_wizard.id,
            'context': dict(self.env.context),
        }



