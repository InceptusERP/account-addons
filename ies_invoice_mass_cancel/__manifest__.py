# -*- coding: utf-8 -*-
# Part of Inceptus ERP Solutions Pvt.ltd.
# See LICENSE file for copyright and licensing details.
{
    'name': "Invoice Mass Cancel",

    'summary': """
        Mass Cancel & Delete the invoice from the tree view action
    """,

    'description': """
        Mass Cancel & Delete the invoice from the tree view action
    """,

    'author': "Inceptus.io",
    'website': "http://www.inceptus.io",

    'category': 'Accounting',
    'version': '1.0',

    'depends': ['account_cancel'],

    'data': [
        'security/ir.model.access.csv',
        'wizard/mass_cancel_invoice_wizard_view.xml'
    ],
}