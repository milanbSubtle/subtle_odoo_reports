from odoo import api, fields, models, _


class CustomerSalesList(models.TransientModel):
    _name = "customer.sales.list.wizard"

    all_customer = fields.Boolean(string="For All Customers")
    customer = fields.Many2one(comodel_name="res.partner", string="Customer", required=True)

    def print_customer_sales(self):
        form_data = self.read()[0]
        customer_id = self.customer.id
        customer_records = self.env['sale.order'].search([('id', '=', customer_id)])

        data_lines = []

        total_amount = 0
        for customer_record in customer_records:
            customer_sales = {}

            total_amount += customer_record.amount_total
        print(total_amount)
        customer_sales['name'] = customer_record.partner_id.name
        customer_sales['total_amount'] = total_amount
