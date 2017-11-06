# -*- coding: utf-8 -*-
# Part of Inceptus ERP Solutions Pvt.ltd.
# See LICENSE file for copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class MassCancelInvoiceWiz(models.TransientModel):
    """docstring for MassCancelInvoiceWiz"""

    _name = 'mass.cancel.invoice'

    confirm = fields.Boolean('Confirm')

    @api.multi
    def action_cancel_invoice(self):
        if not self.confirm:
            raise UserError(_('Please confirm before cancelling the invoice.'))
        acc_env = self.env[self._context.get('active_model')]
        for rec in self._context.get('active_ids'):
            invoice_id = acc_env.browse(rec)
            invoice_id.action_cancel()
            if self._context.get('unlink'):
                invoice_id.unlink()
