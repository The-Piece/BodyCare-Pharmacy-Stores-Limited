# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Asset(models.Model):
    _inherit = 'account.asset'

    custom_number = fields.Char(
        string='Number',
        readonly=True,
    )
    custom_description = fields.Text(
        string='Description',
    )
    custom_record_brand = fields.Char(
        string='Record Brand',
    )
    custom_model_number = fields.Char(
        string='Model Number',
    )
    custom_serial_number = fields.Char(
        string='Serial Number',
    )
    custom_manufacturer_id = fields.Many2one(
        'res.partner',
        string='Manufacturer',
    )
    custom_purchase_id = fields.Many2one(
        'purchase.order',
        string='Purchase order',
    )
    custom_receive_date = fields.Date(
        string='Received Date',
    )
    custom_warranty_information = fields.Char(
        string='Warranty Information',
    )
    custom_warranty_expire_date = fields.Date(
        string='Warranty Date',
    )
    custom_warranty_service_provider = fields.Many2one(
        'res.partner',
        string='Warranty Service Provider',
    )

    custom_source_department_id = fields.Many2one(
        'hr.department',
        string="Source Location"
    )
    custom_source_partner_id = fields.Many2one(
        'res.partner',
        string="Source Custodian"
    )

    @api.model
    def create(self, vals):
        number = self.env['ir.sequence'].next_by_code('custom.account.seq')
        vals.update({ 'custom_number': number })
        return super(Asset, self).create(vals)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
