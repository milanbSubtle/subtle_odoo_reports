# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Subtle Odoo Reports',
    'version': '1',
    'website': 'https://www.subtletechs.com/',
    'author': 'Subtle Technologies (Pvt) Ltd',
    'depends': [
        'base',
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/sale/customer_order_details.xml',
        'wizard/sale/customer_sales_list.xml',
        'wizard/sale/customer_top10_list.xml',
        'report/customer_order_details_report_template.xml',
        'report/customer_sales_list_report_template.xml',
        'report/customer_top10_list_report_template.xml',
        'report/report.xml',
    ],

    'installable': True,
    'application': True,
}
