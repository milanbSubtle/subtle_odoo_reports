from odoo import api, fields, models, _
from datetime import datetime


class CustomerTop10List(models.TransientModel):
    _name = "customer.top10.list.wizard"

    from_date = fields.Datetime(string="From")
    to_date = fields.Datetime(string="To", default=datetime.now())

    def print_top10_list(self):
        data = {}
        return self.env.ref('subtle_odoo_reports.customer_top10_list_records_wizard_action').report_action(self,
                                                                                                           data=data)
