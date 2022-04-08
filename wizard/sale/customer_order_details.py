from odoo import api, fields, models, _


class CustomerOrderDetailsWizard(models.TransientModel):
    _name = 'customer.order.details.wizard'

    customer = fields.Many2one(comodel_name="res.partner", string="Customer Name", required=True)

    def print_customer_records(self):
        form_data = self.read()[0]
        customer_id = self.customer.id

        record_data_list = []
        sale_order_records = self.env['sale.order'].search([('partner_id', '=', customer_id)])

        for sale_order_record in sale_order_records:
            record_details = {}
            record_lines_list = []

            sale_order_sequence = sale_order_record.name
            sequence_date = sale_order_record.date_order
            sales_person = sale_order_record.user_id.name
            total = sale_order_record.amount_total

            record_lines = sale_order_record.order_line

            record_details['sale_order_sequence'] = sale_order_sequence
            record_details['sequence_date'] = sequence_date
            record_details['sales_person'] = sales_person
            record_details['total'] = total

            for record_line in record_lines:
                record_line_details = {}
                record_line.price_total
                product = record_line.name
                quantity = record_line.product_uom_qty
                unit_price = record_line.price_unit
                subtotal = record_line.price_total

                record_line_details['product'] = product
                record_line_details['quantity'] = quantity
                record_line_details['unit_price'] = unit_price
                record_line_details['subtotal'] = subtotal

                record_lines_list.append(record_line_details)

            record_details['line_items'] = record_lines_list
            record_data_list.append(record_details)

        data = {
            'form_data': form_data,
            'record_data_list': record_data_list,
        }
        return self.env.ref('subtle_odoo_reports.customer_order_details_reports_wizard_action').report_action(self,
                                                                                                              data=data)
