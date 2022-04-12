from odoo import api, fields, models, _
from datetime import datetime, timedelta, date


class CustomerSalesList(models.TransientModel):
    _name = "customer.sales.list.wizard"

    all_customer = fields.Boolean(string="For All Customers", default=False)
    customer = fields.Many2one(comodel_name="res.partner", string="Customer")
    from_date = fields.Datetime(string="From")
    to_date = fields.Datetime(string="To", default=datetime.now())

    def print_customer_sales(self):
        order_details = []

        customer_ids = self.env['res.partner'].search([])

        # sale.order-> date_order
        # filter: from_date < date_order < to_date

        if self.all_customer:
            for customer_id in customer_ids:

                # order_ids_del = self.env['sale.order'].search([('partner_id', '=', customer_id.id)])
                # filter_ids = order_ids_del.search([('state', 'in', ['done', 'sale'])])
                if self.to_date and self.from_date:
                    customer_records = self.env['sale.order'].search([('partner_id', '=', customer_id.id),
                                                                      ('state', 'in', ['done', 'sale']),
                                                                      ('date_order', '>=', self.from_date),
                                                                      ('date_order', '<=', self.to_date)])

                else:
                    customer_records = self.env['sale.order'].search([('partner_id', '=', customer_id.id),
                                                                      ('state', 'in', ['done', 'sale'])])
                if customer_records:
                    total_amount = 0
                    for customer_record in customer_records:
                        customer_sales = {}

                        total_amount += customer_record.amount_total

                    customer_address = customer_record.partner_id.street
                    customer_sales['name'] = customer_record.partner_id.name
                    customer_sales['customer_address'] = customer_address
                    customer_sales['total_amount'] = total_amount
                    order_details.append(customer_sales)

        else:
            if self.to_date and self.from_date:
                customer_records = self.env['sale.order'].search([('partner_id', '=', self.customer.id),
                                                                  ('state', 'in', ['done', 'sale']),
                                                                  ('date_order', '>=', self.from_date),
                                                                  ('date_order', '<=', self.to_date)])

            else:
                customer_records = self.env['sale.order'].search([('partner_id', '=', self.customer.id),
                                                                  ('state', 'in', ['done', 'sale'])])

            if customer_records:
                total_amount = 0
                for customer_record in customer_records:
                    customer_sales = {}

                    total_amount += customer_record.amount_total

                    customer_address = customer_record.partner_id.street
                    customer_sales['name'] = customer_record.partner_id.name
                    customer_sales['customer_address'] = customer_address
                    customer_sales['total_amount'] = total_amount
                order_details.append(customer_sales)

        data = {
            'form_data': self.read()[0],
            'order_details': order_details
        }
        return self.env.ref('subtle_odoo_reports.customer_sales_list_records_wizard_action').report_action(self,
                                                                                                           data=data)
