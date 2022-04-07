from odoo import api, fields, models, _


class CustomerOrderDetailsWizard(models.TransientModel):
    _name = 'customer.order.details.wizard'

    customer = fields.Many2one(comodel_name="res.partner", string="Customer Name", required=True)

    def print_customer_records(self):
        form_data = self.read()[0]
        customer_id = self.read()[0]['customer'][0]
        sale_order_records = self.env['sale.order'].search_read([('partner_id', '=', customer_id)])
        print(sale_order_records)

        data = {}
        return self.env.ref('subtle_odoo_reports.customer_order_details_reports_wizard_action').report_action(self,
                                                                                                              data=data)
