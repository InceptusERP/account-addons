# -*- coding: utf-8 -*-
# Part of Inceptus ERP Solutions Pvt.ltd.
# See LICENSE file for copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class AccountInvoice(models.Model):
    """docstring for AccountInvoice"""

    _inherit = 'account.invoice'

    @api.multi
    def action_cancel(self):
        res = super(AccountInvoice, self).action_cancel()
        moves = self.env['account.move']
        for inv in self:
            if inv.move_id:
                moves += inv.move_id
            if inv.payment_move_line_ids:
                raise UserError(_(
                    'You cannot cancel an invoice which is partially paid. You need to unreconcile related payment entries first.'))
        self.write({'state': 'cancel', 'move_id': False, 'move_name': False})
        if moves:
            moves.button_cancel()
            moves.unlink()
        return res
