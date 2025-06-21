from odoo import api,fields,models
from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    total_cost = fields.Float('Total Cost',compute='_compute_total_cost',store=True)


    @api.depends('product_uom_qty','product_id.standard_price')
    def _compute_total_cost(self):
        for line in self:
            line.total_cost = line.product_uom_qty * line.product_id.standard_price


    @api.constrains('total_cost')
    def _check_total_cost_limit(self):
        for line in self:
            if line.total_cost > 50000:
                raise ValidationError("Total cost cannot exceed 50000.")
